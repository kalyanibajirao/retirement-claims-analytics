import pandas as pd

group_df = pd.read_csv("../data/cleaned_group_death_claims.csv")

individual_df = pd.read_csv("../data/cleaned_individual_death_claims.csv")


# Negative Value Validation


group_numeric = group_df.select_dtypes(include="number")

individual_numeric = individual_df.select_dtypes(include="number")


print("\nGROUP NEGATIVE VALUES")

print((group_numeric < 0).sum())


print("\nINDIVIDUAL NEGATIVE VALUES")

print((individual_numeric < 0).sum())

# Data Type Validation
print(group_df.dtypes)

print(individual_df.dtypes)

#Financial Year Validation
print("\nGROUP FINANCIAL YEARS")

print(sorted(group_df["year"].dropna().unique()))


print("\nINDIVIDUAL FINANCIAL YEARS")

print(sorted(individual_df["year"].dropna().unique()))


# Column Structure Validation


group_columns = set(group_df.columns)

individual_columns = set(individual_df.columns)


print("\nCOLUMNS ONLY IN GROUP DATASET")

print(group_columns - individual_columns)


print("\nCOLUMNS ONLY IN INDIVIDUAL DATASET")

print(individual_columns - group_columns)

# Claim Count Consistency

required_columns = [
    "claims_pending_start_no",
    "claims_intimated_no",
    "total_claims_no"
]


if all(column in group_df.columns for column in required_columns):

    group_df["calculated_total_no"] = (
        group_df["claims_pending_start_no"]
        + group_df["claims_intimated_no"]
    )

    group_df["count_difference"] = (
        group_df["total_claims_no"]
        - group_df["calculated_total_no"]
    )

    print("\nGROUP COUNT DIFFERENCES")

    print(group_df["count_difference"].value_counts())

else:

    print("\nRequired columns are missing.")

# Quality Summary

quality_report = pd.DataFrame({
    "Dataset": [
        "Group Death Claims",
        "Individual Death Claims"
    ],

    "Rows": [
        group_df.shape[0],
        individual_df.shape[0]
    ],

    "Columns": [
        group_df.shape[1],
        individual_df.shape[1]
    ],

    "Missing_Values": [
        group_df.isnull().sum().sum(),
        individual_df.isnull().sum().sum()
    ],

    "Duplicate_Rows": [
        group_df.duplicated().sum(),
        individual_df.duplicated().sum()
    ]
})


print("\nQUALITY SUMMARY")

print(quality_report)

# 11. Export Quality Report

quality_report.to_excel(
    "../Output/data_quality_report.xlsx",
    index=False
)


print("\nQuality report saved successfully!")

# Identify Negative Value Rows


def find_negative_values(df, dataset_name):

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    negative_records = []

    for column in numeric_columns:

        negative_rows = df[df[column] < 0]

        for index, row in negative_rows.iterrows():

            negative_records.append({
                "Dataset": dataset_name,
                "Row_Index": index,
                "Life_Insurer": row["life_insurer"],
                "Year": row["year"],
                "Column": column,
                "Negative_Value": row[column]
            })

    return pd.DataFrame(negative_records)


group_negative_df = find_negative_values(
    group_df,
    "Group Death Claims"
)


individual_negative_df = find_negative_values(
    individual_df,
    "Individual Death Claims"
)


negative_report = pd.concat(
    [
        group_negative_df,
        individual_negative_df
    ],
    ignore_index=True
)


print("\nNEGATIVE VALUE DETAILS")

print(negative_report)


# Export Negative Value Report


negative_report.to_excel(
     "../Output/negative_value_report.xlsx",
    index=False
)

print("\nNegative value report saved successfully!")


# Identify Missing Value Rows


def find_missing_values(df, dataset_name):

    missing_records = []

    for column in df.columns:

        missing_rows = df[df[column].isnull()]

        for index, row in missing_rows.iterrows():

            missing_records.append({
                "Dataset": dataset_name,
                "Row_Index": index,
                "Life_Insurer": row["life_insurer"],
                "Year": row["year"],
                "Column": column
            })

    return pd.DataFrame(missing_records)


group_missing_df = find_missing_values(
    group_df,
    "Group Death Claims"
)

individual_missing_df = find_missing_values(
    individual_df,
    "Individual Death Claims"
)


missing_report = pd.concat(
    [
        group_missing_df,
        individual_missing_df
    ],
    ignore_index=True
)


print("\nMISSING VALUE DETAILS")

print(missing_report)


# 15. Export Missing Value Report


missing_report.to_excel(
  "../Output/missing_value_report.xlsx",
    index=False
)

print("\nMissing value report saved successfully!")