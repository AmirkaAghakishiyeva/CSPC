import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

df = pd.read_csv("Heart_disease_cleveland_new.csv")

print(df.shape)
print(df.head())

cols = ["age", "chol", "trestbps", "thalach"]
data = df[cols]

print(data.describe())
df = pd.read_csv("Heart_disease_cleveland_new.csv")
print(df.shape)
print(df.head())
print(data.describe())
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for ax, col in zip(axes.flat, cols):
    ax.hist(data[col], bins=20, edgecolor="black")
    ax.set_title(col)
    ax.set_xlabel(col)
    ax.set_ylabel("Count")

plt.tight_layout()
plt.savefig("distributions.png", dpi=150)
plt.close()
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for ax, col in zip(axes.flat, cols):
    stats.probplot(data[col].dropna(), dist="norm", plot=ax)
    ax.set_title(col)

plt.tight_layout()
plt.savefig("qqplots.png", dpi=150)
plt.close()


for col in cols:
    x = data[col].dropna()
    w, p = stats.shapiro(x)

    print(col, "W =", round(w, 3), "p =", round(p, 4))

    if p < 0.05:
        print("Evidence against normality")
    else:
        print("Insufficient evidence against normality") 
disease = df[df["target"] == 1]["thalach"].dropna()
healthy = df[df["target"] == 0]["thalach"].dropna()

print("Number with disease:", len(disease))
print("Number without disease:", len(healthy))

p_disease = stats.shapiro(disease).pvalue
p_healthy = stats.shapiro(healthy).pvalue

if p_disease >= 0.05 and p_healthy >= 0.05:
    test = stats.ttest_ind(disease, healthy, equal_var=False)
    print("Test: Welch's t-test")
else:
    test = stats.mannwhitneyu(disease, healthy, alternative="two-sided")
    print("Test: Mann-Whitney U test")

print("Statistic:", round(test.statistic, 3))
print("p-value:", round(test.pvalue, 5))

print("Mean thalach with disease:", round(disease.mean(), 2))
print("Mean thalach without disease:", round(healthy.mean(), 2))

fig, ax = plt.subplots(figsize=(7, 5))

ax.boxplot([disease, healthy], tick_labels=["Disease", "Healthy"])
ax.set_ylabel("Maximum heart rate (thalach)")
ax.set_title("Thalach comparison")

plt.tight_layout()
plt.savefig("thalach_comparison.png", dpi=150)
plt.close()

groups = [disease, healthy]
means = [group.mean() for group in groups]

intervals = []

for group in groups:
    sem = stats.sem(group)
    margin = stats.t.ppf(0.975, len(group) - 1) * sem
    intervals.append(margin)

print("95% CI margin for disease:", round(intervals[0], 2))
print("95% CI margin for healthy:", round(intervals[1], 2))

plt.figure(figsize=(7, 5))
plt.errorbar(
    ["Disease", "Healthy"],
    means,
    yerr=intervals,
    fmt="o",
    capsize=6
)

plt.ylabel("Mean thalach")
plt.title("Mean thalach with 95% confidence intervals")
plt.tight_layout()
plt.savefig("thalach_means.png", dpi=150)
plt.close()
data_corr = df[["age", "thalach"]].dropna()

r, p = stats.pearsonr(data_corr["age"], data_corr["thalach"])
rho, p_spearman = stats.spearmanr(
    data_corr["age"],
    data_corr["thalach"]
)

print("Pearson correlation:", round(r, 3))
print("Pearson p-value:", round(p, 5))

print("Spearman correlation:", round(rho, 3))
print("Spearman p-value:", round(p_spearman, 5))

plt.figure(figsize=(7, 5))

plt.scatter(
    data_corr["age"],
    data_corr["thalach"],
    alpha=0.6
)

plt.xlabel("Age")
plt.ylabel("Maximum heart rate (thalach)")
plt.title("Age vs thalach")

plt.tight_layout()
plt.savefig("age_vs_thalach.png", dpi=150)
plt.close()
chem = pd.read_csv("chemicals_cancer.csv")

chem.columns = (
    chem.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("Chemicals dataset shape:", chem.shape)
print("Columns:", chem.columns.tolist())
print(chem.head())

benzene = "benzene"
cadmium = "cadmium"
malignancy = "malignancy"
pollution = "pollution_index"

print("Benzene and malignancy:")
print(chem[benzene].corr(chem[malignancy]))

print("Cadmium and malignancy:")
print(chem[cadmium].corr(chem[malignancy]))

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].scatter(
    chem[benzene],
    chem[malignancy],
    alpha=0.5
)
axes[0].set_xlabel("Benzene")
axes[0].set_ylabel("Malignancy")
axes[0].set_title("Benzene vs malignancy")

axes[1].scatter(
    chem[cadmium],
    chem[malignancy],
    alpha=0.5
)
axes[1].set_xlabel("Cadmium")
axes[1].set_ylabel("Malignancy")
axes[1].set_title("Cadmium vs malignancy")

plt.tight_layout()
plt.savefig("chem_naive.png", dpi=150)
plt.close()
controlled = chem[
    (chem[pollution] >= 40) &
    (chem[pollution] <= 60)
]

print("Original number of observations:", len(chem))
print("Observations after controlling pollution:", len(controlled))

print("Before controlling pollution:")
print("Benzene:", chem[benzene].corr(chem[malignancy]))
print("Cadmium:", chem[cadmium].corr(chem[malignancy]))

print("After controlling pollution:")
print("Benzene:", controlled[benzene].corr(controlled[malignancy]))
print("Cadmium:", controlled[cadmium].corr(controlled[malignancy]))

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].scatter(
    chem[benzene],
    chem[malignancy],
    alpha=0.5
)
axes[0, 0].set_title("Benzene: all observations")

axes[0, 1].scatter(
    chem[cadmium],
    chem[malignancy],
    alpha=0.5
)
axes[0, 1].set_title("Cadmium: all observations")

axes[1, 0].scatter(
    controlled[benzene],
    controlled[malignancy],
    alpha=0.5
)
axes[1, 0].set_title("Benzene: controlled pollution")

axes[1, 1].scatter(
    controlled[cadmium],
    controlled[malignancy],
    alpha=0.5
)
axes[1, 1].set_title("Cadmium: controlled pollution")

for ax in axes.flat:
    ax.set_xlabel("Chemical concentration")
    ax.set_ylabel("Malignancy")

plt.tight_layout()
plt.savefig("chem_controlled.png", dpi=150)
plt.close()
target_counts = df["target"].value_counts(normalize=True)

entropy = -(target_counts * np.log2(target_counts)).sum()

print("Target proportions:")
print(target_counts)

print("Target entropy:", round(entropy, 3))