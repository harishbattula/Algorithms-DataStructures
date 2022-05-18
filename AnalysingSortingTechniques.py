# To find time complexity of each method we import time from time
from time import time

# To generete random lists
from numpy.random import randint

# Importing sys to increase recurssion depth for quicksort algorithm
import sys

# Increasing recurssion depth
# By default limit is 1000
sys.setrecursionlimit(99999)


# For timting functions, using decerator
def TimeIt(func):
    def Wrapper(*args,**kwargs):
        start = time()
        func(*args,**kwargs)
        end = time()
        print("Time taken for "+func.__name__+" is :" +str(end-start)+" s")
    return Wrapper

# Bubble sort method implementation
@TimeIt
def BubbleSort(arr):

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                (arr[i],arr[j])=(arr[j],arr[i])
    
    return arr


# Selection Sort method implementation
@TimeIt
def SelectionSort(arr):

    for i in range(len(arr)-1):
        low=arr[i]
        lowindex=i
        for j in range(i+1,len(arr)):
            if low > arr[j]:
                low = arr[j]
                lowindex = j

        (arr[i],arr[lowindex]) = (arr[lowindex] ,arr[i])
    return arr


# Quick sort method implementation
def QuickSort(arr,low,high):
    if low < high:
        pi = Partition(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr, pi+1, high)

    return arr

# To make partitions of array in quicksort
def Partition(arr,low,high):

    pivot = arr[high]

    i=low-1

    for j in range(low,high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])

    return i+1


# Count sort method implementation, it is also called as frequency sort Technique
@TimeIt
def CountSort(arr):
    Counts = [0] * (max(arr)+1)

    for i in arr:
        Counts[i] += 1
    
    SortedArr = []

    for i in range(len(Counts)):
        for j in range(Counts[i]):
            SortedArr.append(i)
    
    return SortedArr

# Initilizing array
arr = []

# Creating  some random arrays using numpy.random.randint()

arr1 = randint(low = 0, high = 999999, size = 999)

arr2 = randint(low = 0, high = 9999, size = 99999)

arr3 = randint(low = 0, high = 99, size = 9999999)

# Appending random arrays to arr
arr.append(arr1)
arr.append(arr2)
arr.append(arr3)


for i in range(len(arr)):

    # Since Bubble and selected are not much efficient we skip this two methods for large lists
    if(i==0):
        SelectionSort(arr[i]) 
        BubbleSort(arr[i]) 

    # We skip quick sort for 3rd dataset
    # Because it is crashing our programm by taking more time
    if(i!=2):
        start = time()
        QuickSort(arr[i], 0, len(arr[i])-1) 
        end = time()
        print("Time Taken for Quick Sort is : "+str(end-start)+" s")

    CountSort(arr[i])

    start = time() 
    sorted(arr[i])
    end = time() 
    print("Time taken for inbuilt sort method is : "+str(end - start)+" s")

# Result that i got on quadcore cpu with 8gb memory

'''
    First Iteration:
    Time taken for SelectionSort is :0.04690074920654297 s
    Time taken for BubbleSort is :0.10406661033630371 s
    Time Taken for Quick Sort is : 0.24161028861999512 s
    Time taken for CountSort is :0.12830686569213867 s
    Time taken for inbuilt sort method is : 0.0 s

    Second Iteration:
    Time Taken for Quick Sort is : 0.709204912185669 s
    Time taken for CountSort is :0.04014468193054199 s
    Time taken for inbuilt sort method is : 0.008000373840332031 s

    Third Iteration:
    Time taken for CountSort is :1.965980052947998 s
    Time taken for inbuilt sort method is : 3.0012428760528564 s
'''
