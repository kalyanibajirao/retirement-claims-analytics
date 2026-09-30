import pandas as pd
import numpy as np
group_df = pd.read_csv("../data/cleaned_group_death_claims.csv")

individual_df = pd.read_csv("../data/cleaned_individual_death_claims.csv")

print(group_df.head())
print(individual_df.head())

print("Group Death Claims Shape:", group_df.shape)

print("Individual Death Claims Shape:", individual_df.shape)

print("Group Dataset Columns:")

print(group_df.columns.tolist())

print("Individual Dataset Columns:")

print(individual_df.columns.tolist())

group_df.info()
individual_df.info()

# Check Missing Values

print("Group Dataset Missing Values:")

print(group_df.isnull().sum())

print("Individual Dataset Missing Values:")

print(individual_df.isnull().sum())

# Duplicate Records

print("\nGROUP DUPLICATES")

print(group_df.duplicated().sum())


print("\nINDIVIDUAL DUPLICATES")

print(individual_df.duplicated().sum())

# 8. Statistical Summary
print("\nGROUP STATISTICAL SUMMARY")

print(group_df.describe())


print("\nINDIVIDUAL STATISTICAL SUMMARY")

print(individual_df.describe())

# 9. Unique Insurers

print("\nUNIQUE GROUP INSURERS")

print(group_df["life_insurer"].nunique())


print("\nUNIQUE INDIVIDUAL INSURERS")

print(individual_df["life_insurer"].nunique())

# 10. Financial Years

print("\nGROUP FINANCIAL YEARS")

print(group_df["year"].unique())


print("\nINDIVIDUAL FINANCIAL YEARS")

print(individual_df["year"].unique())