import numpy as np
import pandas as pd

# 1. Read data file
file_path = r"C:\Users\thaol\OneDrive\Documents\GitHub\Mini-project-1-EDA\1. data\raw\churn_prediction.csv"
df = pd.read_csv(file_path)

print("Initial shape:", df.shape)

# 2. Handle duplicates
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)

# 3. Handle missing values (Using median to be robust against outliers[cite: 1])
num_missing_cols = [
    "Tenure",
    "WarehouseToHome",
    "HourSpendOnApp",
    "OrderAmountHikeFromlastYear",
    "CouponUsed",
    "OrderCount",
    "DaysSinceLastOrder",  # Chú ý kiểm tra đúng tên cột DaysSinceLastOrder / DaySinceLastOrder
]

for col in num_missing_cols:
  if col in df.columns:
    median_val = df[col].median()
    # Sửa từ inplace=True thành gán trực tiếp để tránh ChainedAssignmentError
    df[col] = df[col].fillna(median_val)

# 4. Clean categorical string inconsistencies
cat_cols = df.select_dtypes(include=["object", "string"]).columns
for col in cat_cols:
  df[col] = df[col].astype(str).str.strip()

# Verify missing values after cleaning
print("\nRemaining Missing Values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# 5. Save processed data
output_path = r"C:\Users\thaol\OneDrive\Documents\GitHub\Mini-project-1-EDA\1. data\processed\churn_cleaned.csv"
df.to_csv(output_path, index=False)
print("\nSuccessfully saved cleaned data to:", output_path)