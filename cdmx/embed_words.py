#!/usr/bin/env python3
"""Embed single words in multiple languages via OpenRouter (Qwen3 8b).

Reads OPENROUTER_API_KEY from ~/Code/mnestic/.env
Stores raw embeddings + PCA 3D projection as JSON.

Usage:
    .venv/bin/python embed_words.py "apple,manzana,りんご"
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from pathlib import Path


def get_api_key() -> str:
    env_path = Path.home() / "Code" / "mnestic" / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                return line.split("=", 1)[1].strip()
    key = os.getenv("OPENROUTER_API_KEY")
    if key:
        return key
    raise RuntimeError("OPENROUTER_API_KEY not found in mnestic/.env or env")


def embed_texts(texts: list[str], api_key: str) -> list[list[float]]:
    url = "https://openrouter.ai/api/v1/embeddings"
    payload = json.dumps({"model": "qwen/qwen3-embedding-8b", "input": texts}).encode()
    req = urllib.request.Request(
        url, data=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode())
    embeddings = data["data"]
    embeddings.sort(key=lambda x: x["index"])
    return [item["embedding"] for item in embeddings]


def pca_3d(embeddings: list[list[float]]) -> dict:
    import numpy as np
    X = np.array(embeddings, dtype=np.float32)
    X_mean = X.mean(axis=0)
    X_centered = X - X_mean
    cov = np.cov(X_centered, rowvar=False)
    eigvals, eigvecs = np.linalg.eigh(cov)
    # descending order
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]
    components = eigvecs[:, :3]
    coords = X_centered @ components
    total_var = eigvals.sum()
    explained = eigvals[:3] / total_var
    return {
        "coordinates": coords.tolist(),
        "explained_variance_ratio": explained.tolist(),
        "components": components.T.tolist(),
    }


def main() -> None:
    out_dir = Path.cwd()
    out_path = out_dir / "word_embeddings.json"

    if len(sys.argv) > 1:
        raw = sys.argv[1]
        words = [w.strip() for w in raw.split(",") if w.strip()]
    else:
        words_file = out_dir / "words.txt"
        if words_file.exists():
            words = [w.strip() for w in words_file.read_text().splitlines() if w.strip()]
        else:
            print("Usage: python embed_words.py 'word1,word2,word3'")
            sys.exit(1)

    if not words:
        print("No words provided.")
        sys.exit(1)

    print(f"Embedding {len(words)} words...")
    api_key = get_api_key()
    embeddings = embed_texts(words, api_key)

    print("Computing PCA to 3D...")
    pca_result = pca_3d(embeddings)

    points = [
        {
            "word": words[i],
            "x": round(pca_result["coordinates"][i][0], 6),
            "y": round(pca_result["coordinates"][i][1], 6),
            "z": round(pca_result["coordinates"][i][2], 6),
        }
        for i in range(len(words))
    ]

    result = {
        "model": "qwen/qwen3-embedding-8b",
        "provider": "openrouter",
        "words": words,
        "embeddings": embeddings,
        "dimensions": len(embeddings[0]) if embeddings else 0,
        "pca": {
            "components": 3,
            "explained_variance_ratio": [
                round(pca_result["explained_variance_ratio"][0], 6),
                round(pca_result["explained_variance_ratio"][1], 6),
                round(pca_result["explained_variance_ratio"][2], 6),
            ],
            "points": points,
        },
    }

    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"Saved to {out_path}")
    print(f"Dimensions: {result['dimensions']}")
    print(
        f"PCA variance explained: "
        f"{result['pca']['explained_variance_ratio'][0]:.2%}, "
        f"{result['pca']['explained_variance_ratio'][1]:.2%}, "
        f"{result['pca']['explained_variance_ratio'][2]:.2%}"
    )


if __name__ == "__main__":
    main()
