import re, sys
import pandas as pd
import matplotlib.pyplot as plt

num = lambda s: float(re.match(r"-?[\d.]+", s.strip()).group())
rows = []
for line in open(sys.argv[1], errors="ignore"):
    p = [x.strip() for x in line.split("|")]
    if len(p) != 6:
        continue
    try:
        a_pop, a_unpop, beta = map(float, p[:3])
        rows.append((a_pop, a_unpop, beta, num(p[3]), num(p[4]), num(p[5])))
    except (ValueError, AttributeError):
        continue
df = pd.DataFrame(rows, columns=["a_pop","a_unpop","beta","ndcg","gini","cov"]).drop_duplicates()
df.to_csv("grid_results.csv", index=False)

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
for b, g in df.groupby("beta"):
    ax[0].scatter(g.ndcg, g["cov"], s=12, label=f"β={b}")
    ax[1].scatter(g.ndcg, g.gini, s=12, label=f"β={b}")
ax[0].set(xlabel="nDCG@10", ylabel="Item coverage"); ax[1].set(xlabel="nDCG@10", ylabel="Gini")
ax[0].legend(); plt.tight_layout(); plt.savefig("tradeoff.png", dpi=200)