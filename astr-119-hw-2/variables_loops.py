import numpy as np # we use numpy for many things

def main():
	i = 0 # i is an integer, declared with number 0= 3
	n = 10 # n is another integer
	x = 119.0 #floating point numbers are declared with a.


	# we can use numpy to declare arrays quickly
	y = np.zeros(n,dtype=float) #declares 10 zeros as floats using np

	# we can use for loops to iterate with variable

	for i in range (n):       # i in rang [0, n-1]
		y[i] = 2.0 * float(i) + 1.0 # set y = 2*i+1 as floats

	#we can simply iterate through a variable array
	for y_element in y:
		print(y_element) 

#execute the main function
if __name__== "__main__":
	 main()

