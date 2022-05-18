# Finding Min and Max in a list using Divide and Conquer Technique
def MinMax(List, Left, Right, Min, Max):
 
    # if the list contains only one element
    if Left == Right:       
 
        if Min > List[Right]:
            Min = List[Right]

        if Max < List[Left]:
            Max = List[Left]
 
        return Min, Max
 
    # if the list contains only two elements
 
    if Right - Left == 1:
 
        if List[Left] < List[Right]:
            if Min > List[Left]:
                Min = List[Left]
 
            if Max < List[Right]:
                Max = List[Right]
 
        else:
            if Min > List[Right]:
                Min = List[Right]
 
            if Max < List[Left]:
                Max = List[Left]
 
        return Min, Max
 

    # Find the middle element
    Mid = (Left + Right) // 2
 
    # Recurr for the Left sublist
    Min, Max = MinMax(List, Left, Mid, Min, Max)
 
    # Recurr for the Right sublist
    Min, Max = MinMax(List, Mid + 1, Right, Min, Max)
 
    return Min, Max
 
 
if __name__ == '__main__':
 
    List = [18, 39, -156, 247, 85, -12, 4, 255, 1, -11, 987, -76]

    # initilizing and assigning values to minimum, maximum
    minimum = List[0]
    maximum = List[0]
 
    (Min, Max) = MinMax(List, 0, len(List) - 1, minimum, maximum)
 
    print("Minimum : ",Min)
    print("Maximum : ",Max)
 
# Output

# Minimum : -156
# Maximum : 987
