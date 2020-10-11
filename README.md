# pandas-challenge
In [268]:
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

df = pd.DataFrame(school_data_complete, columns = ["Total Schools"])
In [318]:
#Counting number of schools
School_Count = len(school_data_complete["school_name"].unique())
In [319]:
#Counting number of students
Student_Count = len(school_data_complete["Student ID"])
In [320]:
#Calculated average math score
Average_Math_Score = sum(school_data_complete["math_score"])/Student_Count
In [321]:
#Calculated total budget for all schools
school_budget = sum(school_data_complete["budget"].unique())
In [322]:
#Calculated % passing math
math_pass_criteria = school_data_complete[school_data_complete.reading_score >= 70]
percent_pass_math = (math_pass_criteria['math_score'].count()/Student_Count)*100
In [323]:
#Calculated % passing reading
reading_pass_criteria = school_data_complete[school_data_complete.reading_score >= 70]
percent_pass_reading = (reading_pass_criteria['reading_score'].count()/Student_Count)*100
In [324]:
#Calculated average reading score
Average_Reading_Score = sum(school_data_complete["reading_score"])/Student_Count
In [325]:
#Calculated overall % passing
overall_passing_rate = school_data_complete[(school_data_complete['math_score'] >= 70) & (school_data_complete['reading_score'] >= 70)]['Student ID'].count()/Student_Count*100
In [326]:
#Put all district stats into dataframe and printed
district_summaryDF = pd.DataFrame({"School Count": [School_Count],
                                   "Student Count": Student_Count,
                                   "Total Budget": school_budget,
                                   "Average Math Score": Average_Math_Score,
                                   "Average Reading Score": Average_Reading_Score,
                                   "% Passing Math": percent_pass_math,
                                   "% Passing Reading": percent_pass_reading,
                                   "% Passing Overall": overall_passing_rate})
district_summaryDF
Out[326]:
School Count    Student Count    Total Budget    Average Math Score    Average Reading Score    % Passing Math    % Passing Reading    % Passing Overall
0    15    39170    24649428    78.985371    81.87784    85.805463    85.805463    65.172326
In [327]:
#grouping by the school name
school_name = school_data_complete.set_index('school_name').groupby(['school_name'])
In [328]:
#calculating total number of students by school
numberOfStudent = school_name['Student ID'].count()
In [329]:
#calculating total budget of each school
totalBudgetBySchool = school_data.set_index('school_name')['budget']
In [330]:
#assigning the school type
schoolType = school_data.set_index('school_name')['type']
In [331]:
#assigning the school type
schoolType = school_data.set_index('school_name')['type']
In [332]:
#calculating total budget of each student
budgetPerStudent = school_data.set_index('school_name')['budget']/school_data.set_index('school_name')['size']
In [333]:
#calculating average math score
averageMathScore = school_name['math_score'].mean()
In [334]:
#calculating average reading score
averageReadingScore = school_name['reading_score'].mean()
In [335]:
#calculating percent passing math by school
percentPassMathBySchool = school_data_complete[school_data_complete['math_score'] >= 70].groupby('school_name')['Student ID'].count()/numberOfStudent*100
In [336]:
#calculating percent passing reading by school
percentPassReadBySchool = school_data_complete[school_data_complete['reading_score'] >= 70].groupby('school_name')['Student ID'].count()/numberOfStudent*100
In [337]:
#calculating overall passing rate by school
percentPassOverallBySchool = school_data_complete[(school_data_complete['math_score'] >= 70) & (school_data_complete['reading_score'] >= 70)].groupby('school_name')['Student ID'].count()/numberOfStudent*100
In [338]:
#creating dataframe to hold all varaibles we just created & testing it
school_summary = pd.DataFrame({
    "School Type": schoolType,
    "Total Students": numberOfStudent,
    "Total School Budget": totalBudgetBySchool,
    "Per Student Budget": budgetPerStudent,
    "Average Math Score": averageMathScore,
    "Average Reading Score": averageReadingScore,
    '% Passing Math': percentPassMathBySchool,
    '% Passing Reading': percentPassReadBySchool,
    "% Overall Passing": percentPassOverallBySchool
})
school_summary
Out[338]:
School Type    Total Students    Total School Budget    Per Student Budget    Average Math Score    Average Reading Score    % Passing Math    % Passing Reading    % Overall Passing
Bailey High School    District    4976    3124928    628.0    77.048432    81.033963    66.680064    81.933280    54.642283
Cabrera High School    Charter    1858    1081356    582.0    83.061895    83.975780    94.133477    97.039828    91.334769
Figueroa High School    District    2949    1884411    639.0    76.711767    81.158020    65.988471    80.739234    53.204476
Ford High School    District    2739    1763916    644.0    77.102592    80.746258    68.309602    79.299014    54.289887
Griffin High School    Charter    1468    917500    625.0    83.351499    83.816757    93.392371    97.138965    90.599455
Hernandez High School    District    4635    3022020    652.0    77.289752    80.934412    66.752967    80.862999    53.527508
Holden High School    Charter    427    248087    581.0    83.803279    83.814988    92.505855    96.252927    89.227166
Huang High School    District    2917    1910635    655.0    76.629414    81.182722    65.683922    81.316421    53.513884
Johnson High School    District    4761    3094650    650.0    77.072464    80.966394    66.057551    81.222432    53.539172
Pena High School    Charter    962    585858    609.0    83.839917    84.044699    94.594595    95.945946    90.540541
Rodriguez High School    District    3999    2547363    637.0    76.842711    80.744686    66.366592    80.220055    52.988247
Shelton High School    Charter    1761    1056600    600.0    83.359455    83.725724    93.867121    95.854628    89.892107
Thomas High School    Charter    1635    1043130    638.0    83.418349    83.848930    93.272171    97.308869    90.948012
Wilson High School    Charter    2283    1319574    578.0    83.274201    83.989488    93.867718    96.539641    90.582567
Wright High School    Charter    1800    1049400    583.0    83.682222    83.955000    93.333333    96.611111    90.333333
In [339]:
#Top 5 Best Schools
school_summary.sort_values('% Overall Passing',ascending=False).head()
Out[339]:
School Type    Total Students    Total School Budget    Per Student Budget    Average Math Score    Average Reading Score    % Passing Math    % Passing Reading    % Overall Passing
Cabrera High School    Charter    1858    1081356    582.0    83.061895    83.975780    94.133477    97.039828    91.334769
Thomas High School    Charter    1635    1043130    638.0    83.418349    83.848930    93.272171    97.308869    90.948012
Griffin High School    Charter    1468    917500    625.0    83.351499    83.816757    93.392371    97.138965    90.599455
Wilson High School    Charter    2283    1319574    578.0    83.274201    83.989488    93.867718    96.539641    90.582567
Pena High School    Charter    962    585858    609.0    83.839917    84.044699    94.594595    95.945946    90.540541
In [340]:
#Top 5 Worst Schools
school_summary.sort_values('% Overall Passing',ascending=True).head()
Out[340]:
School Type    Total Students    Total School Budget    Per Student Budget    Average Math Score    Average Reading Score    % Passing Math    % Passing Reading    % Overall Passing
Rodriguez High School    District    3999    2547363    637.0    76.842711    80.744686    66.366592    80.220055    52.988247
Figueroa High School    District    2949    1884411    639.0    76.711767    81.158020    65.988471    80.739234    53.204476
Huang High School    District    2917    1910635    655.0    76.629414    81.182722    65.683922    81.316421    53.513884
Hernandez High School    District    4635    3022020    652.0    77.289752    80.934412    66.752967    80.862999    53.527508
Johnson High School    District    4761    3094650    650.0    77.072464    80.966394    66.057551    81.222432    53.539172
In [341]:
#Filtering Grades Math Scores
sortByGrade9 = school_data_complete[school_data_complete.grade == '9th']
grade9MathScores = sortByGrade9.groupby('school_name')['math_score'].mean()
sortByGrade10 = school_data_complete[school_data_complete.grade == '10th']
grade10MathScores = sortByGrade10.groupby('school_name')['math_score'].mean()
sortByGrade11 = school_data_complete[school_data_complete.grade == '11th']
grade11MathScores = sortByGrade11.groupby('school_name')['math_score'].mean()
sortByGrade12 = school_data_complete[school_data_complete.grade == '12th']
grade12MathScores = sortByGrade12.groupby('school_name')['math_score'].mean()
In [342]:
#Putting Grades Into Dataframe And Printed
gradeSummary = pd.DataFrame({
    "9th Grade Math Score": grade9MathScores,
    "10th Grade Math Score": grade10MathScores,
    "11th Grade Math Score": grade11MathScores,
    "12th Grade Math Score": grade12MathScores,
})
gradeSummary
Out[342]:
9th Grade Math Score    10th Grade Math Score    11th Grade Math Score    12th Grade Math Score
school_name                
Bailey High School    77.083676    76.996772    77.515588    76.492218
Cabrera High School    83.094697    83.154506    82.765560    83.277487
Figueroa High School    76.403037    76.539974    76.884344    77.151369
Ford High School    77.361345    77.672316    76.918058    76.179963
Griffin High School    82.044010    84.229064    83.842105    83.356164
Hernandez High School    77.438495    77.337408    77.136029    77.186567
Holden High School    83.787402    83.429825    85.000000    82.855422
Huang High School    77.027251    75.908735    76.446602    77.225641
Johnson High School    77.187857    76.691117    77.491653    76.863248
Pena High School    83.625455    83.372000    84.328125    84.121547
Rodriguez High School    76.859966    76.612500    76.395626    77.690748
Shelton High School    83.420755    82.917411    83.383495    83.778976
Thomas High School    83.590022    83.087886    83.498795    83.497041
Wilson High School    83.085578    83.724422    83.195326    83.035794
Wright High School    83.264706    84.010288    83.836782    83.644986
In [343]:
#Filtering Grades Reading Scores
grade9ReadScores = sortByGrade9.groupby('school_name')['reading_score'].mean()
grade10ReadScores = sortByGrade10.groupby('school_name')['reading_score'].mean()
grade11ReadScores = sortByGrade11.groupby('school_name')['reading_score'].mean()
grade12ReadScores = sortByGrade10.groupby('school_name')['reading_score'].mean()
In [344]:
#Putting Grades Into Dataframe And Printed
gradeSummaryRead = pd.DataFrame({
    "9th Grade Read Score": grade9ReadScores,
    "10th Grade Read Score": grade10ReadScores,
    "11th Grade Read Score": grade11ReadScores,
    "12th Grade Read Score": grade12ReadScores,
})

gradeSummaryRead
Out[344]:
9th Grade Read Score    10th Grade Read Score    11th Grade Read Score    12th Grade Read Score
school_name                
Bailey High School    81.303155    80.907183    80.945643    80.907183
Cabrera High School    83.676136    84.253219    83.788382    84.253219
Figueroa High School    81.198598    81.408912    80.640339    81.408912
Ford High School    80.632653    81.262712    80.403642    81.262712
Griffin High School    83.369193    83.706897    84.288089    83.706897
Hernandez High School    80.866860    80.660147    81.396140    80.660147
Holden High School    83.677165    83.324561    83.815534    83.324561
Huang High School    81.290284    81.512386    81.417476    81.512386
Johnson High School    81.260714    80.773431    80.616027    80.773431
Pena High School    83.807273    83.612000    84.335938    83.612000
Rodriguez High School    80.993127    80.629808    80.864811    80.629808
Shelton High School    84.122642    83.441964    84.373786    83.441964
Thomas High School    83.728850    84.254157    83.585542    84.254157
Wilson High School    83.939778    84.021452    83.764608    84.021452
Wright High School    83.833333    83.812757    84.156322    83.812757
In [345]:
#Creating Bins and label bins
SpendingRangesPerStudent = [0,584,629,644,680]

group_labels = ["<$584", "$585-629", "$630-644", "$645-675"]
In [346]:
#Putting Binned Data Into Dataframe
school_summary['SpendingRangesPerStudent'] = pd.cut(school_summary['Per Student Budget'], SpendingRangesPerStudent, labels = group_labels)
school_summary.groupby('SpendingRangesPerStudent')['Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','% Overall Passing'].mean()
<ipython-input-346-9554b9e80ca5>:3: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
  school_summary.groupby('SpendingRangesPerStudent')['Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','% Overall Passing'].mean()
Out[346]:
Average Math Score    Average Reading Score    % Passing Math    % Passing Reading    % Overall Passing
SpendingRangesPerStudent                    
<$584</th> <td>83.455399</td> <td>83.933814</td> <td>93.460096</td> <td>96.610877</td> <td>90.369459</td> </tr> <tr> <th>$585-629    81.899826    83.155286    87.133538    92.718205    81.418596
$630-644</th> <td>78.518855</td> <td>81.624473</td> <td>73.484209</td> <td>84.391793</td> <td>62.857656</td> </tr> <tr> <th>$645-675    76.997210    81.027843    66.164813    81.133951    53.526855
In [347]:
#Creating Bins and label bins
SchoolSize = [0,1000,2000,5000]

group_labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
In [348]:
#Putting Into Dataframe and Print
school_summary['SchoolSize'] = pd.cut(school_summary['Total Students'], SchoolSize, labels = group_labels)
school_summary.groupby('SchoolSize')['Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','% Overall Passing'].mean()
<ipython-input-348-c1072b6e6d06>:3: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
  school_summary.groupby('SchoolSize')['Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','% Overall Passing'].mean()
Out[348]:
Average Math Score    Average Reading Score    % Passing Math    % Passing Reading    % Overall Passing
SchoolSize                    
Small (<1000)    83.821598    83.929843    93.550225    96.099437    89.883853
Medium (1000-2000)    83.374684    83.864438    93.599695    96.790680    90.621535
Large (2000-5000)    77.746417    81.344493    69.963361    82.766634    58.286003
In [349]:
#group by school type
school_type = school_data_complete.set_index('type').groupby(['type'])
In [350]:
#Sorting By Type
averageMathScoreByType = school_type['math_score'].mean()
averageReadingScoreByType = school_type['reading_score'].mean()
numberOfStudentByType = school_type['Student ID'].count()
percentPassMathByType = school_data_complete[school_data_complete['math_score'] >= 70].groupby('type')['Student ID'].count()/numberOfStudentByType*100
percentPassReadingByType = school_data_complete[school_data_complete['reading_score'] >= 70].groupby('type')['Student ID'].count()/numberOfStudentByType*100
percentPassOverallBySchoolType = school_data_complete[(school_data_complete['math_score'] >= 70) & (school_data_complete['reading_score'] >= 70)].groupby('type')['Student ID'].count()/numberOfStudentByType*100
In [351]:
#Putting Into Dataframe and Printing
scoresBySchoolType = pd.DataFrame({
    "Average Math Score": averageMathScoreByType,
    "Average Reading Score": averageReadingScoreByType,
    "% Passing Math": percentPassMathByType,
    "% Passing Reading": percentPassReadingByType,
    "% Overall Passing": percentPassOverallBySchoolType,
})
scoresBySchoolType
Out[351]:
Average Math Score    Average Reading Score    % Passing Math    % Passing Reading    % Overall Passing
type                    
Charter    83.406183    83.902821    93.701821    96.645891    90.560932
District    76.987026    80.962485    66.518387    80.905249    53.695878
In [352]:
#Obseravable Trends
#1. Charter schools offer far greater chance of passing overall. 90% of students pass at charter schools and only 53% pass at a district school.
#2. Schools that have between 2000 & 5000 students have a very low overall passing rate. At smaller to medium schools, passing rate is high.
