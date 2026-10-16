import pandas as pd
import numpy as np

Step 1: Load student dataset

df = pd.read_csv("Students.csv")

subjects = ["Math", "Python", "AI"]

Step 2: Calculate total and average marks

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = np.mean(df[subjects], axis=1)

Step 3: Assign grades using a function

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

df["Grade"] = df["Average"].apply(get_grade)

Step 4: Determine pass or fail

df["Result"] = np.where(
(df[subjects] >= 40).all(axis=1),
"Pass",
"Fail"
)

Step 5: Display complete student analysis

print("===== STUDENT PERFORMANCE ANALYTICS =====")
print(df.to_string(index=False))

Step 6: Overall class statistics

print("\n===== CLASS STATISTICS =====")
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())

Step 7: Subject-wise performance

print("\n===== SUBJECT-WISE AVERAGES =====")
print(df[subjects].mean().round(2))

Step 8: Find top 3 performing students

print("\n===== TOP 3 STUDENTS =====")
print(
df.nlargest(3, "Average")[
["Name", "Average", "Grade"]
].to_string(index=False)
)

Step 9: Attendance analysis

print("\n===== ATTENDANCE ANALYSIS =====")
print("Average Attendance:", round(df["Attendance"].mean(), 2))

print("\nProject analysis completed successfully!")
