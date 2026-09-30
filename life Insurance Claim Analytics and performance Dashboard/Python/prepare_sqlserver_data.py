import pandas as pd
from pathlib import Path


# 1. Define Project Paths


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


# 2. Load Combined Dataset


input_file = OUTPUT_DIR / "combined_death_claims.csv"

df = pd.read_csv(input_file)

print("Dataset loaded successfully!")
print("Original shape:", df.shape)


# 3. Remove Duplicate Records


duplicate_count = df.duplicated().sum()

print("\nDuplicate records:", duplicate_count)

df = df.drop_duplicates().copy()


# 4. Check Missing Values


print("\nMissing values:")
print(df.isnull().sum())


# 5. Convert ID to Integer


if "id" in df.columns:
    df["id"] = pd.to_numeric(
        df["id"],
        errors="coerce"
    ).astype("Int64")


# 6. Convert Text Columns


text_columns = [
    "life_insurer",
    "year",
    "category"
]

for column in text_columns:

    if column in df.columns:
        df[column] = df[column].astype("string")


# 7. Validate Numeric Columns


numeric_columns = df.select_dtypes(
    include=["number"]
).columns

print("\nNumeric columns:")
print(list(numeric_columns))


# 8. Export SQL Server-Ready CSV


output_file = OUTPUT_DIR / "sqlserver_ready_claims.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nSQL Server-ready dataset created!")
print("Final shape:", df.shape)
print("Saved at:", output_file)