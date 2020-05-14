import numpy as np

#creating 1-Dimensional array having elements from 0 to 119
my_array = np.arange(120)
#converting above 1-Dimensional array to 4-Dimensional array
my_array=my_array.reshape(2,3,4,5)
#Accessing the value 91 using indexing
my_array[1,1,2,1]
#Obtaining values in the range from 35-39 from this ndarray
my_array[0][1][3]
#making another 1-Dimensional array called "an_array" from "my_array"
an_array = my_array.reshape(120)
#removing elements from "my_array" which are not multiple of 5
an_array = an_array[an_array%5==0]
#obtaining mean value on axis-3 of "my_array"
for i in range(0,2):
    for j in range(0,3):
        for k in range(0,4):
            print(np.mean(my_array[i][j][k]))
