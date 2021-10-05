import numpy as np    #import numpy library

#integers

i = 10       #integer
print(type(i))  #print out the data type of i

a_i = np.zeros(i,dtype=int)     #declare an array of ints
print(type(a_i))          #will return an array
print(type(a_i[0]))             #will return int64

#floats
x = 199.0       #floating point number with some precision
print(type(x))  #print out the data type of x

y = 1.92e2      #float 119 in scientific notation
print(type(y))  #print out the data type of y

z = np.zeros(i,dtype=float) #declare an array of flaots
print(type(z))              #print type of array
print(type(z[0]))   #floats