# importing time and sleep methods from time module
from time import time,sleep

# Implementation of time it method
def TimeIt(func):
    
    def Wrapper(*args,**kwargs):

        start=time()
        result=func(*args,**kwargs)

        # Sleeping function for .01 sec to avoid 0.0 s result for binary search
        sleep(.01)

        end=time()
        print("Time taken using "+func.__name__+" is : "+str(end-start)+" s")

        return result

    return Wrapper


# Binary Search Algorithm
@TimeIt
def BinarySearch(arr,n):
    l=0
    u=len(arr)-1

    while(l<=u):
        
        CurrentIndex=(l+u)//2
        CurrentValue=arr[CurrentIndex]

        if CurrentValue==n:
            return True
        else:
            if n < CurrentValue:
                u = CurrentIndex - 1
            else:
                l = CurrentIndex + 1

    return False

# Normal Search Algorithm
@TimeIt
def NormalSerch(arr,n):
    for i in arr:
        if i==n:
            return True
    
    return False


if __name__=="__main__":

    # Sample Sorted array for binary search
    arr = [i for i in range(99999999)]

    # Element to find
    element = 99989198


    if BinarySearch(arr,element):
        print("Found")
    else:
        print("Not Found")

    if NormalSerch(arr,element):
        print("Found")
    else:
        print("Not Found")

# Output

# Time taken using BinarySearch is : 0.01560211181640625 s
# Found

# Time taken using NormalSerch is : 2.053518295288086 s
# Found
            
