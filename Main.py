# Student Performance Analytics System
# Project using Python, Pandas and NumPy

# Step 1: Import required libraries
import pandas as pd
import numpy as np

# Step 2: Load the Students CSV file
df = pd.read_csv("/content/Students.csv")

# Step 3: Select subjects
subjects = ["Math", "Python", "AI"]

# Step 4: Calculate total and average marks
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

# Step 5: Create a function to assign grades
def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

# Step 6: Assign grades to students
df["Grade"] = df["Average"].apply(get_grade)

# Step 7: Determine pass or fail
# A student passes if every subject mark is at least 40
df["Result"] = np.where(
    (df[subjects] >= 40).all(axis=1),
    "Pass",
    "Fail"
)

# Step 8: Display student performance
print("===== STUDENT PERFORMANCE ANALYTICS =====")
print(df.to_string(index=False))

# Step 9: Display class statistics
print("\n===== CLASS STATISTICS =====")
print("Total Students:", len(df))
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", round(df["Average"].max(), 2))
print("Lowest Average:", round(df["Average"].min(), 2))
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())

# Step 10: Display subject-wise averages
print("\n===== SUBJECT-WISE AVERAGES =====")
print(df[subjects].mean().round(2))

# Step 11: Display the top 3 students
print("\n===== TOP 3 STUDENTS =====")
print(
    df.nlargest(3, "Average")[
        ["Name", "Average", "Grade"]
    ].to_string(index=False)
)

# Step 12: Display attendance analysis
print("\n===== ATTENDANCE ANALYSIS =====")
print("Average Attendance:",
      round(df["Attendance"].mean(), 2))

# Step 13: Finish the project
print("\nProject analysis completed successfully!")
