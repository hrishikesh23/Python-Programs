
# Reference - Page 
# https://docs.scipy.org/doc/numpy/user/quickstart.html

# Import the library numpy
import numpy as np


# You can create List as below 
my_list   = [1,2,3]
my_array  = np.array(my_list)
print(my_array)
# The Number of Dimension is rank of the array
# The shape of the array is tuple of the integer giving size of array along each dimension
print(my_array.shape)
# Create an array of 0 to 15 Elements. With Row = 3 and Column = 5
my_arr = np.arange(15).reshape(3,5)
# Print Array
print("\n My Array = \n",my_arr)
# Print the Rows and Column
print("\n (Row,Column) ",my_arr.shape)
print("\n How Many Dimensional: ",my_arr.ndim)
print("\n Data Type : ",my_arr.dtype.name)
print("\n Item Size : ",my_arr.size)
print("\n Type : ", type(my_arr))

# You can create and return an array to variable
# when you create an array the normal mistake is not putting square brackets within parenthesis
# var = np.array(10,20,30) --> Wrong
var = np.array([10,20,30])
print("\n new arr = ",var)

# Transform Sequences into two dimensional arrays
# Parenthesis within Square bracket to differentiate individual rows
var = np.array([(11,12,13),(22,33,44)])
print("\n Var Multi Dimensional Static =\n",var)

# We can also specify the type of array

var = np.array([[1,1.2],[2,2.2]],dtype=complex)
print("\n Var Dtype =\n",var)

# Create an array of zero
# Below command will call the function from library numpy
# Argument Passed to Zeros is (Row,Column)

var = np.zeros( (3,4) )
print("\n Zeroed Var = \n",var)

# Similarly We can do it for one
var = np.ones( (3,4), dtype = np.int16 )
print("\n Ones var = \n",var)

#Similary we can check the effect of creating an empty variable and not passing the data type for var created

var = np.empty( (2,3) )
print("\n Empty Var = \n ",var)




