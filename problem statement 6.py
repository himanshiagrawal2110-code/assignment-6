
import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# For Excel file, use:
# df = pd.read_excel("data.xls")

# Display original dataset
print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values with column mean (numeric columns)
df = df.fillna(df.mean(numeric_only=True))

# Fill remaining missing values with mode
for col in df.columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

# Display cleaned dataset
print("\nPreprocessed Dataset:")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nData preprocessing completed successfully!")
