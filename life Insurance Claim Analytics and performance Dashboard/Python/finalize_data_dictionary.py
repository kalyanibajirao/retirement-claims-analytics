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
print("Dataset shape:", df.shape)

# 3. Create Column Descriptions

column_descriptions = {

    "id": "Unique identifier for the record",

    "life_insurer": "Name of the life insurance company",

    "year": "Financial year of the claim data",

    "category": "Type of insurance claim: Group or Individual",

    "claims_pending_start_no":
        "Number of claims pending at the beginning of the period",

    "claims_pending_start_amt":
        "Total amount of claims pending at the beginning of the period",

    "claims_intimated_no":
        "Number of new claims reported during the period",

    "claims_intimated_amt":
        "Total amount of new claims reported during the period",

    "total_claims_no":
        "Total number of claims considered during the period",

    "total_claims_amt":
        "Total monetary value of claims considered during the period",

    "claims_paid_no":
        "Number of claims paid during the period",

    "claims_paid_amt":
        "Total amount paid for settled claims",

    "claims_repudiated_no":
        "Number of claims rejected due to repudiation",

    "claims_repudiated_amt":
        "Total amount associated with repudiated claims",

    "claims_rejected_no":
        "Number of rejected claims",

    "claims_rejected_amt":
        "Total amount associated with rejected claims",

    "claims_unclaimed_no":
        "Number of claims remaining unclaimed",

    "claims_unclaimed_amt":
        "Total amount associated with unclaimed claims",

    "claims_pending_end_no":
        "Number of claims pending at the end of the period",

    "claims_pending_end_amt":
        "Total amount of claims pending at the end of the period",

    "claims_paid_ratio_no":
        "Percentage of claims paid based on claim count",

    "claims_paid_ratio_amt":
        "Percentage of claims paid based on claim amount",

    "claims_repudiated_rejected_ratio_no":
        "Percentage of repudiated and rejected claims based on count",

    "claims_repudiated_rejected_ratio_amt":
        "Percentage of repudiated and rejected claims based on amount",

    "claims_pending_ratio_no":
        "Percentage of pending claims based on count",

    "claims_pending_ratio_amt":
        "Percentage of pending claims based on amount"
}

# 4. Define Business Categories

def assign_category(column_name):

    if column_name in ["id", "life_insurer", "year", "category"]:
        return "General Information"

    elif "pending_start" in column_name:
        return "Opening Pending Claims"

    elif "intimated" in column_name:
        return "New Claims"

    elif "total_claims" in column_name:
        return "Total Claims"

    elif "paid" in column_name:
        return "Paid Claims"

    elif "repudiated" in column_name or "rejected" in column_name:
        return "Rejected Claims"

    elif "unclaimed" in column_name:
        return "Unclaimed Claims"

    elif "pending_end" in column_name:
        return "Closing Pending Claims"

    elif "ratio" in column_name:
        return "Performance Ratios"

    else:
        return "Other"

# 5. Build Final Data Dictionary

data_dictionary = pd.DataFrame({
    "column_name": df.columns,
    "data_type": [df[column].dtype for column in df.columns],
    "missing_values": [
        df[column].isnull().sum()
        for column in df.columns
    ],
    "unique_values": [
        df[column].nunique()
        for column in df.columns
    ],
    "business_category": [
        assign_category(column)
        for column in df.columns
    ],
    "business_description": [
        column_descriptions.get(
            column,
            "Description not yet defined"
        )
        for column in df.columns
    ]
})

# 6. Add Sample Values

sample_values = []

for column in df.columns:

    values = df[column].dropna().unique()[:5]

    sample_values.append(
        ", ".join(map(str, values))
    )

data_dictionary["sample_values"] = sample_values

# 7. Display Final Data Dictionary

print("\nFinal Data Dictionary:\n")

print(
    data_dictionary.to_string(index=False)
)

# 8. Export to Excel

output_file = OUTPUT_DIR / "final_data_dictionary.xlsx"

data_dictionary.to_excel(
    output_file,
    index=False
)

print("\nFinal data dictionary created successfully!")

print("Saved at:", output_file)