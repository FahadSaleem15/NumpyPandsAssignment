## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------") 
array4x3 = np.full((4,3),2)
print(array4x3)

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
array3x4 = np.arange(0, 111, 10).reshape(3, 4)
print(array3x4) 

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")
new_array = np.arange(0, 111, 10).reshape(4, 3)

print(new_array)

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
new_arrayx3 = (np.arange(0, 111, 10)*3).reshape(4, 3)
print(new_arrayx3)

## Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")

## This errored out... why?
#print(np.multiply(array3x4*array4x3))
#It gave an error because both the arrays' shapes are different. A 3x4 array cannot be multiplied to a 4x3 array.

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")

## this worked! why?
print(np.multiply(array4x3, new_array))
#This worked because both arrays' shapes are same, 4x3.



