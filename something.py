#NumPy - Numeric Python
#introduction to NumPy
import numpy as np  

#lists:
list1 = [1, 2, 3, 4, 5]
print(list1) #[1, 2, 3, 4, 5]
print(list1[0]) #1

#lists can have several various data types
list2 = ["John Elder", 41, list1, True]
print(list2) #['John Elder', 41, [1, 2, 3, 4, 5], True]

#NumPy arrays have all their elements the same data types
#ndarray = n-dimensional array
np1 = np.array([0, 1, 2, 3, 4, 5]) # creating numpy array
print(np1) #[0 1 2 3 4 5]

#numpy arrays have math methods
print(np1.shape) # (6,) #the size of an np array 

#creating an np arrays
np2 = np.arange(10) #creates a numpy array with 10 elements from 0 to 9 
print(np2) #[0 1 2 3 4 5 6 7 8 9]
np3 = np.arange(0, 10, 2) #from 0 to 10, but step 2
print(np3) #[0 2 4 6 8]
np4 = np.zeros(10) #np array with 10 zeros
print(np4) #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
np5 = np.zeros((2, 10)) #2-dimensional array, both arrays have 10 zeros
print(np5) #[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
           #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
np6 = np.full((10), 6) #an array of 10 6s
print(np6) #[6 6 6 6 6 6 6 6 6 6]
np7 = np.full((2, 10), 6)
print(np7)#[[6 6 6 6 6 6 6 6 6 6]
          #[6 6 6 6 6 6 6 6 6 6]]

#converting python lists to np
my_list = [1, 2, 3, 4, 5]
np8 = np.array(my_list)
print(np8) #[1, 2, 3, 4, 5]

#slicing numpy arrays: 
np9 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np9[1:5]) #from index 1 is inclusive and 5 is exlusive #[2 3 4 5]
print(np9[3:]) #[4 5 6 7 8 9]
print(np9[-3:-1]) #[7 8]
print(np9[1:5:2]) #1 through 5 with 2 steps #[2 4]
print(np9[::2]) #[1 3 5 7 9]
print(np9) #[1 2 3 4 5 6 7 8 9]

#slice a 2d array 
np10 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np10) #[[ 1  2  3  4  5]
            # [ 6  7  8  9 10]]
print(np10[1, 2]) #pulling single item - first row, second item #8
print(np10[0:1, 1:3]) #slicing one row 0 to 1 row, and 1 to 3 column #[[2 3]]
print(np10[0:2, 1:3]) #slicing both rows #[[2 3]
                                         #[7 8]]


#numpy universal function
np11 = np.array([0, 1, 2, 3, -4, -5, -6, 7, 8, 9])
print(np.sqrt(np11))#square root of each element ##[0.         1.         1.41421356 1.73205081 2.   
                                                #[0.         1.         1.41421356 1.73205081       
                                                # nan        nan
                                                #        nan 2.64575131 2.82842712 3.        ]   
print(np.absolute(np11)) #abolute value  #[0 1 2 3 4 5 6 7 8 9]
print(np.exp(np11)) #exponentials #[1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01
                                  # 1.83156389e-02 6.73794700e-03 2.47875218e-03 1.09663316e+03
                                  # 2.98095799e+03 8.10308393e+03]
print(np.max(np11)) #9
print(np.min(np11)) #-6
print(np.sign(np11)) #[ 0  1  1  1 -1 -1 -1  1  1  1]
print(np.sin(np11)) #sine of each element #[0.         0.84147098 0.90929743 0.14112001 0.7568025  0.95892427
                                          #0.2794155  0.6569866  0.98935825 0.41211849] 
print(np.log(np11)) #log #[      -inf 0.         0.69314718 1.09861229       
                         #nan        nan
                         #       nan 1.94591015 2.07944154 2.19722458]  

#Copy vs. View 
#copy - copy of your array 
#view - a copy of your array as well, but it holds a reference to it 
np12 = np.array([1, 2, 3, 4, 5])
np12 = np11.view() #np12 viewing np11
print(f"Original numpy array 1: {np11}") #Original numpy array 1: [ 0  1  2  3 -4 -5 -6  7  8  9]
print(f"Original numpy array 2: {np12}") #Original numpy array 2: [ 0  1  2  3 -4 -5 -6  7  8  9]
np11[0] = 41
print(f"Changed numpy array 1: {np11}") #Changed numpy array 1: [41  1  2  3 -4 -5 -6  7  8  9]
print(f"Original numpy 2: {np12}") #Original numpy 2: [41  1  2  3 -4 -5 -6  7  8  9] 

np12 = np11.copy()
print(f"Original numpy array 1: {np11}") #Original numpy array 1: [41  1  2  3 -4 -5 -6  7  8  9]
print(f"Original numpy array 2: {np12}") #Original numpy array 2: [41  1  2  3 -4 -5 -6  7  8  9]
np11[0] = 58
print(f"Changed numpy array 1: {np11}") #Changed numpy array 1: [58  1  2  3 -4 -5 -6  7  8  9]
print(f"Original numpy 2: {np12}") #Original numpy 2: [41  1  2  3 -4 -5 -6  7  8  9] 

#shape and reshape numpy arrays
np13 = np.array([1, 2, 3, 4, 5])#create 1-dimensional and get shape
print(np13) #[1 2 3 4 5]
print(np13.shape) #(5,)

np14 = np.array([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8]])#create 2d array and get shape, (rows/columns)
print(np14) #[[1 2 3 4 5]
            #[4 5 6 7 8]]
print(np14.shape) #(2, 5)

np15 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
np16 = np15.reshape(3, 4)#reshape 2d
print(np16) #[[ 1  2  3  4]
            #[ 5  6  7  8]
            #[ 9 10 11 12]]
print(np16.shape) #(3, 4) -> (row, column)
np17 = np15.reshape(2, 3, 2)#reshape 3d- (2rows of 2)
print(np17) #[[[ 1  2]
            #[ 3  4]
            #[ 5  6]]

            #[[ 7  8]
            #[ 9 10]
            #[11 12]]]
print(np17.shape) #(2, 3, 2)
np18 = np17.reshape(-1)#flatten to 1d
print(np18) #[ 1  2  3  4  5  6  7  8  9 10 11 12]
print(np18.shape) #(12,)

#iterating through numpy arrays
#1-dimensional
np21 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for x in np21:
    print(x)
# 1 2 3 4 5 6 7 8 9 10, all in new lines
#2-dimensional 
np22 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
for x in np22: 
    for y in x: 
        print(y)
# 1 2 3 4 5 6 7 8 9 10, all in new lines
#3-dimensional 
np23 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np23: 
    for y in x: 
        for z in y: 
            print(z)
# 1 2 3 4 5 6 7 8 9 10 11 12, all in new lines
#use np.nditer() - to not make it countless nedted loops 
for x in np.nditer(np23): 
    print(x)
# 1 2 3 4 5 6 7 8 9 10 11 12, all in new lines

#sorting numpy arrays
#numerical
np31 = np.array([6, 7, 4 ,9, 5, 2, 6])
print(np.sort(np31)) #[2 4 5 6 6 7 9]
#alphabetical
np32 = np.array(["John", "Tyna", "Patrick", "Apple"])
print(np.sort(np32)) #['Apple' 'John' 'Patrick' 'Tyna']
#booleans
np33 = np.array([True, False, False, True])
print(np.sort(np33)) #[False False  True  True]
#the original isn't being changed when we sort it
#sorting 2-d arrays
np34 = np.array([[6, 7, 1, 9], [8, 1, 3, 5]])
print(np.sort(np34))#[[1 6 7 9]
                    #[1 3 5 8]]

#searching through numpy arrays              
np41 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3])
x = np.where(np41 == 3) # will return a tuple of the index number
print(x) #(array([ 2, 10]),)
print(x[0]) #[ 2 10] #just the index number
print(np41[x[0]]) #[3 3], will return how many of 3s we have # [3 3]
y = np.where(np41 % 2 == 0) #return even items
print(y) #(array([1, 3, 5, 7, 9]),) - all the indexes where even numbers are located
print(y[0]) #[1 3 5 7 9]
print(np41[y[0]]) #[ 2  4  6  8 10] - those even numbers themselves


#filterning numpy arrays (boolean index checking)
np51 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = [True, True, False, True, True, False, False, False, False, True]
print(np51) #[ 1  2  3  4  5  6  7  8  9 10]
print(np51[x]) #[ 1  2  4  5 10]
#or you can do
filtered = []
for thing in np51:
    if thing % 2 == 0: 
        filtered.append(True)
    else: 
        filtered.append(False)
print(filtered) #[False, True, False, True, False, True, False, True, False, True]
print(np51[filtered]) #[ 2  4  6  8 10] - these are elements
#or shortcut
filtered = np51 % 2 == 0
print(np51)
print(filtered)
print(np51[filtered])