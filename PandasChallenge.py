# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "/Users/sambarton/pandas-challenge/Resources/schools_complete.csv"
student_data_to_load = "/Users/sambarton/pandas-challenge/Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

School_Count = len(school_data_complete["school_name"].unique())

Student_Count = len(school_data_complete["Student ID"])

#Need To Figure Out A Way Of Taking Budget From Each School, Then Add

Average_Math_Score = sum(school_data_complete["math_score"])/Student_Count

Average_Reading_Score = sum(school_data_complete["reading_score"])/Student_Count

