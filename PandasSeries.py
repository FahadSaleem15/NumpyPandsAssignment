import pandas as pd

grades = pd.Series([87,100,94])

#Pandas displays a Series in two-column format with the indices left aligned
#in the left column and the values right aligned in the right column.
#After listing the Series elements, pandas shows the data type (dtype) of
#the underlying array’s elements:

print(grades)



pd.Series(98.6, range(3))

#0    98.6
#1    98.6
#2    98.6
#dtype: float64


#You can access a Series’s elements by via square brackets containing an index:

grades[0]

grades.count()

grades.mean()

grades.min()

grades.max()

grades.std()


# Calling Series method describe produces all these stats and more:

#print(grades.describe())



# here is where the magic starts happening!
# You can specify custom indices with the index keyword argument:

grades = pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])


# If you initialize a Series with a dictionary, its keys become the Series’ indices, and its values become
# the Series’ element values:

grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})
print(grades)




# you can access individual elements via square brackets containing a custom index value:
grades['Eva']
#100


#If the custom indices are strings that could represent valid Python identifiers, pandas automatically adds
#them to the Series as attributes that you can access via a dot (.), as in:

grades.Wally
#87

#Series also has built-in attributes. For example, the dtype attribute returns the underlying array’s element type:

grades.dtype
#dtype('int64')


grades.values
#array([ 87, 100, 94])



#Series of Strings
hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

''' 0 Hammer
    1    Saw
    2 Wrench
    dtype: object'''


#calling string methods apply to each element
hardware.str.contains('a')

''' 0     True
    1     True
    2    False
    dtype: bool '''



hardware.str.upper()

''' 0    HAMMER
    1       SAW
    2    WRENCH  '''

#convert a series object to a python list
hardware_list = hardware.tolist()

print(hardware_list)

#compare 2 series
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])

print(ds1==ds2)

print(ds1>ds2)

print(ds1<ds2)

#convert a series of lists to one series

list_of_series = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])

print(list_of_series)

one_series = list_of_series.apply(pd.Series).stack().reset_index(drop=True)

print(one_series)

#Sort a series
s = pd.Series(['100','200','python','300.12','400'])
sorted_series = s.sort_values()
print(sorted_series)

#add to a series
added = s._append(pd.Series(['500','php']))

print(added
      )

#change the original
s = s._append(pd.Series(['500','php']))
print(s)

# to reset the indexes
s = s.reset_index(drop=True)
print(s)

#write code to calculate the frequency counts of each unique value of a given series
import random

list1 = [random.randrange(1,10) for i in range(0,101)]
s = pd.Series(list1)
print(s)
result = s.value_counts()
print(result)





























