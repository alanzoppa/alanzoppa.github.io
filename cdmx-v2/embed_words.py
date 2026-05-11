#!/usr/bin/env python3
"""Embed single words in multiple languages via OpenRouter (Qwen3 8b).

Collects raw embeddings + PCA / t-SNE / UMAP 3D projections,
pairwise similarities, language centroids, gender vectors, and norms.

Usage:
    .venv/bin/python embed_words.py "apple,manzana,りんご"
"""

from __future__ import annotations

import json
import os
import sys
import math
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


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb)


def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def pca_3d(embeddings: list[list[float]]) -> dict:
    import numpy as np
    X = np.array(embeddings, dtype=np.float32)
    X_mean = X.mean(axis=0)
    X_centered = X - X_mean
    cov = np.cov(X_centered, rowvar=False)
    eigvals, eigvecs = np.linalg.eigh(cov)
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


def tsne_3d(embeddings: list[list[float]], perplexity: float = 5.0, random_state: int = 42) -> list[list[float]]:
    from sklearn.manifold import TSNE
    import numpy as np
    X = np.array(embeddings, dtype=np.float32)
    tsne = TSNE(n_components=3, perplexity=perplexity, random_state=random_state, init="pca", learning_rate="auto")
    coords = tsne.fit_transform(X)
    return coords.tolist()


def umap_3d(embeddings: list[list[float]], n_neighbors: int = 3, min_dist: float = 0.1, random_state: int = 42) -> list[list[float]]:
    import umap
    import numpy as np
    X = np.array(embeddings, dtype=np.float32)
    reducer = umap.UMAP(n_components=3, n_neighbors=n_neighbors, min_dist=min_dist, random_state=random_state, metric="cosine")
    coords = reducer.fit_transform(X)
    return coords.tolist()


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
    dim = len(embeddings[0]) if embeddings else 0

    print(f"Raw dimensions: {dim}")

    # --- Compute derived metrics ---

    # 1. Pairwise similarities & distances
    print("Computing pairwise similarities...")
    similarities = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            similarities.append({
                "word1": words[i],
                "word2": words[j],
                "cosine": round(cosine(embeddings[i], embeddings[j]), 6),
                "euclidean": round(euclidean(embeddings[i], embeddings[j]), 6),
            })

    # 2. Vector norms
    norms = {words[i]: round(math.sqrt(sum(x * x for x in embeddings[i])), 6) for i in range(len(words))}

    # 3. Language centroids
    print("Computing language centroids...")
    translations = {
        "en": ["man", "woman", "uncle", "aunt"],
        "es": ["hombre", "mujer", "tío", "tía"],
        "zh": ["男人", "女人", "叔叔", "阿姨"],
    }
    lang_idx = {lang: [words.index(w) for w in ws if w in words] for lang, ws in translations.items()}
    centroids = {}
    for lang, idxs in lang_idx.items():
        if not idxs:
            continue
        c = [sum(embeddings[i][d] for i in idxs) / len(idxs) for d in range(dim)]
        centroids[lang] = [round(v, 6) for v in c]

    # 4. Gender vectors
    print("Computing gender vectors...")
    gender_pairs = [
        ("man", "woman"), ("hombre", "mujer"), ("男人", "女人"),
        ("uncle", "aunt"), ("tío", "tía"), ("叔叔", "阿姨"),
    ]
    gender_vectors = {}
    base_diff = None
    for a, b in gender_pairs:
        if a not in words or b not in words:
            continue
        i, j = words.index(a), words.index(b)
        diff = [embeddings[j][k] - embeddings[i][k] for k in range(dim)]
        diff_norm = math.sqrt(sum(x * x for x in diff))
        if base_diff is None:
            base_diff = diff
            parallelism = 1.0
        else:
            dot = sum(x * y for x, y in zip(diff, base_diff))
            parallelism = dot / (diff_norm * math.sqrt(sum(x * x for x in base_diff)))
        gender_vectors[f"{a}->{b}"] = {
            "from": a,
            "to": b,
            "norm": round(diff_norm, 6),
            "parallelism_to_first": round(parallelism, 6),
        }

    # 5. PCA
    print("Computing PCA...")
    pca_result = pca_3d(embeddings)
    pca_points = [
        {"word": words[i], "x": round(pca_result["coordinates"][i][0], 6),
         "y": round(pca_result["coordinates"][i][1], 6),
         "z": round(pca_result["coordinates"][i][2], 6)}
        for i in range(len(words))
    ]

    # 6. t-SNE
    print("Computing t-SNE...")
    tsne_coords = tsne_3d(embeddings)
    tsne_points = [
        {"word": words[i], "x": round(tsne_coords[i][0], 6),
         "y": round(tsne_coords[i][1], 6),
         "z": round(tsne_coords[i][2], 6)}
        for i in range(len(words))
    ]

    # 7. UMAP
    print("Computing UMAP...")
    umap_coords = umap_3d(embeddings)
    umap_points = [
        {"word": words[i], "x": round(umap_coords[i][0], 6),
         "y": round(umap_coords[i][1], 6),
         "z": round(umap_coords[i][2], 6)}
        for i in range(len(words))
    ]

    # 8. PCA distortion check for key pairs
    print("Checking PCA distortion...")
    key_pairs = [("man", "hombre"), ("man", "男人"), ("man", "woman"), ("uncle", "tío")]
    distortions = []
    for a, b in key_pairs:
        if a not in words or b not in words:
            continue
        i, j = words.index(a), words.index(b)
        d_high = euclidean(embeddings[i], embeddings[j])
        pca_i = pca_result["coordinates"][i]
        pca_j = pca_result["coordinates"][j]
        d_pca = euclidean(pca_i, pca_j)
        distortions.append({
            "word1": a,
            "word2": b,
            "high_dim": round(d_high, 6),
            "pca_3d": round(d_pca, 6),
            "ratio": round(d_pca / d_high, 6) if d_high else None,
        })

    # 9. Semantic groups
    groups = {
        "male_adult": [w for w in ["man", "hombre", "男人", "uncle", "tío", "叔叔"] if w in words],
        "female_adult": [w for w in ["woman", "mujer", "女人", "aunt", "tía", "阿姨"] if w in words],
        "parent_generation": [w for w in ["man", "woman", "hombre", "mujer", "男人", "女人"] if w in words],
        "older_generation": [w for w in ["uncle", "aunt", "tío", "tía", "叔叔", "阿姨"] if w in words],
    }

    result = {
        "model": "qwen/qwen3-embedding-8b",
        "provider": "openrouter",
        "words": words,
        "embeddings": embeddings,
        "dimensions": dim,
        "norms": norms,
        "similarities": similarities,
        "language_centroids": centroids,
        "gender_vectors": gender_vectors,
        "distortions": distortions,
        "groups": groups,
        "projections": {
            "pca": {
                "components": 3,
                "explained_variance_ratio": [
                    round(pca_result["explained_variance_ratio"][0], 6),
                    round(pca_result["explained_variance_ratio"][1], 6),
                    round(pca_result["explained_variance_ratio"][2], 6),
                ],
                "points": pca_points,
            },
            "tsne": {
                "perplexity": 5.0,
                "points": tsne_points,
            },
            "umap": {
                "n_neighbors": 3,
                "min_dist": 0.1,
                "points": umap_points,
            },
        },
    }

    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"Saved to {out_path}")
    print(
        f"PCA variance explained: "
        f"{result['projections']['pca']['explained_variance_ratio'][0]:.2%}, "
        f"{result['projections']['pca']['explained_variance_ratio'][1]:.2%}, "
        f"{result['projections']['pca']['explained_variance_ratio'][2]:.2%}"
    )
    print(
        f"t-SNE: computed for {len(words)} points"
    )
    print(
        f"UMAP: computed for {len(words)} points"
    )


if __name__ == "__main__":
    main()
