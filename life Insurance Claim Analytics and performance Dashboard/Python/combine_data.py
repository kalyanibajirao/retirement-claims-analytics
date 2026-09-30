import pandas as pd
from pathlib import Path


# 1. Define Project Paths

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_DIR / "data"

OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


# 2. Load Datasets

group_file = DATA_DIR / "cleaned_group_death_claims.csv"

individual_file = DATA_DIR / "cleaned_individual_death_claims.csv"


group_df = pd.read_csv(group_file)

individual_df = pd.read_csv(individual_file)


# 3. Check Dataset Columns

if list(group_df.columns) != list(individual_df.columns):

    raise ValueError(
        "The datasets have different column structures."
    )


# 4. Combine Datasets

combined_df = pd.concat(
    [group_df, individual_df],
    ignore_index=True
)


# 5. Display Combined Dataset

print("Combined dataset created successfully!")

print("\nCombined Shape:")
print(combined_df.shape)


print("\nCategory Distribution:")
print(combined_df["category"].value_counts())


# 6. Export Combined Dataset

output_file = OUTPUT_DIR / "combined_death_claims.csv"

combined_df.to_csv(
    output_file,
    index=False
)


print("\nCombined dataset saved at:")
print(output_file)