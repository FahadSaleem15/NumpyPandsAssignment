import numpy as np
import random

grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94,77,90],[100,81,82]])


student2 = grades[1]
print(student2)


#get a specific test for a specific student
student1_test2 = grades[0,1]
print(student1_test2)

# to select multiple sequential rows use ':'
students1_2 = grades[0:2]
print(students1_2)

# to select multiple non-sequential rows, use ','
students1_and_3 = grades[[1,3]]
print(grades)
print(students1_and_3)

# to  select students 1 and 3 but only test 3
students1_3_test2 = grades[[1,3],2]
print(students1_3_test2)

all_students_test0 = grades[:,0]
print(all_students_test0)


#all rows and consecutive or sequential columns
all_students_test1_2 = grades[:,1:3]
print(all_students_test1_2)

#all rows and non-consecutive or non-sequential columns
all_students_test0_and_2 = grades[:,[0,2]]
print(all_students_test0_and_2)

'''
Use Numpy random-number generation to create an array of twelve random grades in the range 60 through 100, then
reshape the result inot a 3-by-4 array. Calculate the average of all the grades, the average of the grades for each test
and the averages of the grades for each student.
'''

grades = np.random.randint(60, 101, 12).reshape(3,4)
print(grades)

print(grades.mean())

#average for the test scores
print(grades.mean(axis=0))
#average for each student
print(grades.mean(axis=1))

numbers = np.arange(1,6)
print(numbers)
#shallow copy
numbers_view = numbers.view()
print(numbers_view)

numbers[1] *= 10
print(numbers)
print(numbers_view)

numbers_view[1] /= 10
print(numbers)
print(numbers_view)

numbers_slice_view = numbers[0:3]
print(numbers_slice_view)

numbers[1] *= 20
print(numbers_slice_view)

#deep copy
numbers_copy = numbers.copy()
print(numbers_copy)

numbers[1] *= 10
print(numbers)
print(numbers_copy)

grades = np.array([[87, 96, 70], [100, 87, 90]])
print(grades)

grades_reshaped = grades.reshape(1,6)
print(grades_reshaped)

grades_reshaped[0,1] = 100
print(grades)
print(grades_reshaped)

#grades.resize(1,6)
#print(grades)

#flatten creaets a deep copy
flattened = grades.flatten()
print(flattened)

#ravel creates a shallow copy
raveled = grades.ravel()
print(raveled)

#transpose
print(grades.T)

grades2 = np.array([[94, 77, 90], [100, 81, 82]])

#HSTACK - adding more columns to reach row
print(grades)

h_grades = np.hstack((grades,grades2))
print(h_grades)
print(grades)

#VTSACK - adding more rows
v_grades = np.vstack((grades, grades2))
print(v_grades)