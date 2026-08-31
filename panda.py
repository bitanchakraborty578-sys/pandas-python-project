"""
pandas_demo.py
A beginner-friendly introduction to the pandas library in Python.

Run this in VS Code (make sure pandas is installed first):
    pip install pandas
"""

import pandas as pd

# ----------------------------------------------------------------------
# 1. Creating a DataFrame from a dictionary
# ----------------------------------------------------------------------
data = {
    "Name": ["Rick", "Priya", "Aman", "Sneha", "Karan"],
    "Age": [20, 21, 19, 22, 20],
    "Branch": ["ECE", "CSE", "IT", "ECE", "CSE"],
    "Marks": [78, 92, 65, 88, 74],
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------
# 2. Basic inspection
# ----------------------------------------------------------------------
print("Shape (rows, columns):", df.shape)
print("\nColumn names:", list(df.columns))
print("\nData types:\n", df.dtypes)
print("\nSummary statistics:\n", df.describe())
print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------
# 3. Selecting data
# ----------------------------------------------------------------------
print("Names column only:\n", df["Name"])
print("\nFirst 2 rows:\n", df.head(2))
print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------
# 4. Filtering rows
# ----------------------------------------------------------------------
high_scorers = df[df["Marks"] > 75]
print("Students with Marks > 75:\n", high_scorers)
print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------
# 5. Adding a new column
# ----------------------------------------------------------------------
df["Grade"] = df["Marks"].apply(lambda m: "A" if m >= 85 else ("B" if m >= 70 else "C"))
print("DataFrame with Grade column:\n", df)
print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------
# 6. Grouping and aggregating
# ----------------------------------------------------------------------
branch_avg = df.groupby("Branch")["Marks"].mean()
print("Average marks per branch:\n", branch_avg)
print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------
# 7. Sorting
# ----------------------------------------------------------------------
sorted_df = df.sort_values(by="Marks", ascending=False)
print("Sorted by Marks (descending):\n", sorted_df)
print("\n" + "-" * 50 + "\n")

# ----------------------------------------------------------------------
# 8. Saving to CSV and reading it back
# ----------------------------------------------------------------------
df.to_csv("students.csv", index=False)
print("Saved DataFrame to students.csv")

reloaded_df = pd.read_csv("students.csv")
print("\nReloaded from CSV:\n", reloaded_df)