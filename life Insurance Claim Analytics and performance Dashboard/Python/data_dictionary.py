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

print("Combined dataset loaded successfully!")
print("Dataset shape:", df.shape)

# 3. Create Data Dictionary

data_dictionary = pd.DataFrame({
    "column_name": df.columns,
    "data_type": [df[column].dtype for column in df.columns],
    "missing_values": [df[column].isnull().sum() for column in df.columns],
    "unique_values": [df[column].nunique() for column in df.columns]
})

# 4. Add Sample Values

sample_values = []

for column in df.columns:
    values = df[column].dropna().unique()[:5]
    sample_values.append(", ".join(map(str, values)))

data_dictionary["sample_values"] = sample_values

# 5. Display Data Dictionary

print("\nData Dictionary:")
print(data_dictionary.to_string(index=False))

# 6. Export Data Dictionary

output_file = OUTPUT_DIR / "data_dictionary.xlsx"

data_dictionary.to_excel(output_file, index=False)

print("\nData dictionary saved successfully!")
print("Saved at:", output_file)