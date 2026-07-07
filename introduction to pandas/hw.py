import pandas as pd
import numpy as np

# ----------------------------------------------------
# 1. Create a Labelled Series
# ----------------------------------------------------
print("--- 1. Creating Labelled Series ---")
# Simulating a single student's marks across subjects
subject_marks = pd.Series([85, 92, np.nan, 78], index=["Maths", "Science", "English", "History"])
print(subject_marks)
print("\n")

# ----------------------------------------------------
# 2. Build a DataFrame Table
# ----------------------------------------------------
print("--- 2. Building DataFrame ---")
data = {
    "Student_ID":,
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Maths": [85, 92, np.nan, 78, 90],
    "Science": [90, np.nan, 85, 88, 95],
    "English": [78, 82, 80, np.nan, 85]
}
df = pd.DataFrame(data)
print(df)
print("\n")

# ----------------------------------------------------
# 3. Save and Read a CSV File
# ----------------------------------------------------
print("--- 3. Saving and Reading CSV ---")
# Save DataFrame to a CSV file
df.to_csv("student_marks.csv", index=False)
print("Data saved to 'student_marks.csv'")

# Read the CSV file back into a new DataFrame
df_loaded = pd.read_csv("student_marks.csv")
print("Data successfully loaded from CSV.")
print("\n")

# ----------------------------------------------------
# 4. View Rows and Inspect Data Information
# ----------------------------------------------------
print("--- 4. Inspecting Data ---")
print("First 3 rows:")
print(df_loaded.head(3))

print("\nDataframe Information:")
print(df_loaded.info())
print("\n")

# ----------------------------------------------------
# 5. Clean Missing Values
# ----------------------------------------------------
print("--- 5. Cleaning Missing Values ---")
# Fill missing (NaN) marks with 0 so calculation doesn't break
df_cleaned = df_loaded.fillna(0)
print("Cleaned DataFrame (NaN replaced with 0):")
print(df_cleaned)
print("\n")

# ----------------------------------------------------
# 6. Calculate Total and Average Marks
# ----------------------------------------------------
print("--- 6. Calculating Totals and Averages ---")
# Select only the subject columns for calculation
subjects = ["Maths", "Science", "English"]

# Calculate total marks per student
df_cleaned["Total_Marks"] = df_cleaned[subjects].sum(axis=1)

# Calculate average marks per student
df_cleaned["Average_Marks"] = df_cleaned[subjects].mean(axis=1)

print("Final Analyzed Data:")
print(df_cleaned[["Name", "Total_Marks", "Average_Marks"]])
