
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv("Dataset.csv")
print(f"Raw shape: {df.shape}")

df.columns = [
    "customer_id", "age", "gender", "item_purchased", "category",
    "purchase_amount_usd", "location", "size", "color", "season",
    "review_rating", "subscription_status", "shipping_type",
    "discount_applied", "promo_code_used", "previous_purchases",
    "payment_method", "frequency_of_purchases"
]

print(f"\nNulls before: {df['review_rating'].isnull().sum()}")

df["review_rating_imputed"] = df["review_rating"].isnull().astype(int)  # flag
df["review_rating"] = df["review_rating"].fillna(df["review_rating"].median())

print(f"Nulls after:  {df['review_rating'].isnull().sum()}")
print(f"Imputed rows flagged: {df['review_rating_imputed'].sum()}")


binary_cols = ["subscription_status", "discount_applied", "promo_code_used"]
for col in binary_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0}).astype(int)

frequency_map = {
    "Weekly":          52,
    "Bi-Weekly":       26,
    "Fortnightly":     26, 
    "Monthly":         12,
    "Every 3 Months":   4,
    "Quarterly":        4,  
    "Annually":         1,
}
df["purchase_frequency_annual"] = df["frequency_of_purchases"].map(frequency_map)


unmapped = df["purchase_frequency_annual"].isnull().sum()
print(f"\nUnmapped frequency values: {unmapped}")  

str_cols = ["gender", "category", "season", "shipping_type",
            "payment_method", "location", "color", "size",
            "item_purchased", "frequency_of_purchases"]
for col in str_cols:
    df[col] = df[col].str.strip().str.title()

numeric_cols = {
    "age":                  (18, 70),   
    "purchase_amount_usd":  (20, 100),  
    "review_rating":        (1.0, 5.0),  
    "previous_purchases":   (1, 50),     
}

print("\n--- Outlier Check (IQR method) ---")
outlier_flags = pd.DataFrame(index=df.index)

for col, (expected_min, expected_max) in numeric_cols.items():
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    out_of_iqr   = ((df[col] < lower) | (df[col] > upper)).sum()
    out_of_range = ((df[col] < expected_min) | (df[col] > expected_max)).sum()

    print(f"  {col}:")
    print(f"    IQR bounds:      [{lower:.1f}, {upper:.1f}]   {out_of_iqr} flagged")
    print(f"    Expected range:  [{expected_min}, {expected_max}]   {out_of_range} out of range")

    outlier_flags[f"{col}_outlier"] = (
        (df[col] < lower) | (df[col] > upper)
    ).astype(int)

df = pd.concat([df, outlier_flags], axis=1)
df["any_outlier"] = outlier_flags.any(axis=1).astype(int)
print(f"\nRows with at least one outlier flag: {df['any_outlier'].sum()}")

print("\n--- Validation ---")

assert df["customer_id"].nunique() == len(df), "Duplicate customer IDs found!"
print("All customer_ids are unique")

core_cols = ["age", "purchase_amount_usd", "review_rating",
             "previous_purchases", "purchase_frequency_annual"]
assert df[core_cols].isnull().sum().sum() == 0, "Nulls remain in core columns!"
print(" No nulls in core columns")

# Binary columns should only be 0/1
for col in binary_cols:
    assert set(df[col].unique()).issubset({0, 1}), f"Unexpected values in {col}"
print(" Binary columns are clean (0/1)")

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Distribution of Key Numeric Columns (Post-Cleaning)", fontsize=14)

df["age"].hist(ax=axes[0, 0], bins=20, color="steelblue", edgecolor="white")
axes[0, 0].set_title("Age")

df["purchase_amount_usd"].hist(ax=axes[0, 1], bins=20, color="steelblue", edgecolor="white")
axes[0, 1].set_title("Purchase Amount (USD)")

df["review_rating"].hist(ax=axes[1, 0], bins=15, color="coral", edgecolor="white")
axes[1, 0].set_title("Review Rating (imputed nulls marked)")

df["previous_purchases"].hist(ax=axes[1, 1], bins=20, color="steelblue", edgecolor="white")
axes[1, 1].set_title("Previous Purchases")

plt.tight_layout()
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/distributions.png", dpi=150)
plt.close()
print("\nDistribution plot saved to outputs/distributions.png")

output_path = "outputs/cleaned_dataset.csv"
df.to_csv(output_path, index=False)
print(f"\nCleaned dataset saved: {output_path}")
print(f"Final shape: {df.shape}")
print(f"\nColumns added:")
print("  - review_rating_imputed     : 1 if row had null rating (filled with median)")
print("  - purchase_frequency_annual : numeric purchases/year from frequency label")
print("  - <col>_outlier flags       : IQR-based outlier flag per numeric column")
print("  - any_outlier               : 1 if any numeric column is flagged")
print("  - discount_applied          : converted Yes/No  1/0")
print("  - promo_code_used           : converted Yes/No  1/0")
print("  - subscription_status       : converted Yes/No  1/0")
