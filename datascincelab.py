# #loops 


# #this program give your age in positive value
# age = int(input("Enter Your age : "))
# while(age<0):
#     age = int(input("Enter +ve age "))
#     #print("Enter +VE Age ")
# print(f'your age is {age}')

# #program to print numbers between 1 to 10
# i  = 1;
# while(i <= 10):
#     print(i)
#     i+=1

# #program to check this name is exists or no
# usernames = ['ali' , 'ali12' ,'ali123']
# user = input('Enter Your username : ')
# while user in usernames: 
#     user = input('this users already exists\nEnter New username : ')
# print(user)

#functions


# #this functions print name
# def getSum(name):
#     print('Welcome : {:s}'.format(name))
# getSum("wing")

#numpy library


# #defintion array
# import array as ar
# L = list(range(10))
# A = ar.array('i', L)
# print(A)

#start for numpy
# import numpy as np


# arr = np.array([1, 2, 3, 4, 5])    #type arr is array
# print(arr)

#when print numbers and string in the same statement
# arr1 = np.array([1, 2, 3, 4, 5], dtype='int') #we write dtype and use this sign''
# print(arr1)


#some operator in numpy
# #1
# arr2 = np.array ([i+3 for i in [2,4,6]])
# print(arr2)
# #2
# arr3 = np.array([range (i , i+3) for i in [2, 4, 6]])
# print(arr3)
# print(arr3[1])
# print(arr3[2][2])
# #3
# arr4 = np.zeros(10, dtype=int)
# print(arr4)
# arr4 = np.ones(10)
# print(arr4)
# #4
# arr8 = np.arange(0, 20, 4)
# print(arr8)
# #5
# arr9 = np.linspace(4, 5, 10)
# print((arr9))


#create matrix with numpy
#1
# arr5 = np.ones((3, 5), dtype='int')
# print(arr5)
#2
# arr6 = np.zeros((4, 4), dtype='float')
# print(arr6)
#3
# arr7 = np.full((3, 6), 80)
# print(arr7)


#explain random
# #1
# arr10 = np.random.random((3,3))
# print(arr10)
# #2
# arr11 = np.random.normal(10, 5, (3,4))
# print(arr11)
# #3
# arr12 = np.random.randint(1, 12, (3,4))
# print(arr12)
# #4
# x1 = np.random.randint(10, size=6) # One-dimensional array
# x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
# x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array
# print(x1)
# print(x2)
# print(x3)

#explain eye and empty
# #1
# arr13 = np.eye(3) #gives the unit matrix
# print(arr13)
# #2
# arr14 = np.empty(4) #gives the row
# print(arr14)

import numpy as np

# print (np.identity(5)) #this statement print matrix content 5 ones

# print(np.eye(3,#number of rows
#              5,#number of columns
#              1))#index off the diagonal























