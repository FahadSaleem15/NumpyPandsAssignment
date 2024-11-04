import pandas as pd

grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam':[94,77,90],
               'Katie':[100,81,82],
               'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)


grades.index = ['Test1','Test2','Test3']
print(grades)

print(grades['Eva'])

print(grades.Sam)

print(grades.loc['Test2'])

#for consecutive row
print(grades.loc['Test1':'Test3'])

#doing the same with iloc
print(grades.iloc[0:2])


#for non-consecitive rows
print(grades.loc[['Test1','Test3']])

#VIew Eva and Katie's grades for test 1 and test 2
print(grades.loc[:'Test2',['Eva','Katie']])

#View onlt Sam's THRU BOB's grades for test1 and test3
print(grades.loc[['Test1','Test3'],'Sam':'Bob'])

#Boolean indexing
grades_A = grades[grades>=90]
print(grades_A)

#create a dataframe of everyone with a B grade
grades_B = grades[(grades>=80) & (grades < 90)]
print(grades_B)

#create a dataframe for everyone with an A or B grade
grades_A_or_B = grades[(grades>=90) | (grades>=80)]
print(grades_A_or_B)


#pd.set_option('precision',2)
#by student
print(grades.describe())

#by test
print(grades.T.describe())

#average of student grades for each test
print(grades.T.mean())

#SORTING
#sort row by their indices (Test name)
r_sorted_grades = grades.sort_index(ascending=False)
print(r_sorted_grades)

#sort columns by their column names (student names)
# axis = 1 indicates to sort by column indices
# axis = 0 indicates to sort by row indices

c_sorted_grades = grades.sort_index(axis=1,ascending=False)
print(c_sorted_grades)

#sort by column values (showing grades for test 1 with student name highest to lowest)
c_sorted_grades_v = grades.sort_values(by='Test1',axis=1, ascending=False)
print(c_sorted_grades_v)

c_sorted_grades_v = grades.T.sort_values(by='Test1', ascending=False)
print(c_sorted_grades_v)
#show only test 1 grades
test1_sorted = grades.loc['Test1'].sort_values(ascending=False)
print(test1_sorted)