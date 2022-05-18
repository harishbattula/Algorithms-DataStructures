# Collect cash in a dimonty colony
# Given an array n*m dimensions, where each element is considered as building
# there will be cash in each building which is array[i][j]
# where i is row and j is column

# initially we are at the first column in array, but can be at any row
# we can move right ->, or diagonally top right / or diagonally bottom right \
# our job is to collect maximum cash from dimonty colony

# getting max cash using recurssion

def GetMaxCash(Demontecolony, NoofRows, NoofColumns):
    MaxCash = 0
    for i in range(NoofRows):
        CashCollected = CollectCash(Demontecolony, i, 0, NoofRows, NoofColumns)
        MaxCash = max(MaxCash, CashCollected)
    return MaxCash

def CollectCash(Demontecolony, Row, Column, NoofRows, NoofColumns):
    if (Row < 0 or Column < 0 or Row == NoofRows or Column == NoofColumns):
        return 0
    TopRight = CollectCash(Demontecolony, Row -1, Column + 1, NoofRows, NoofColumns)
    Right = CollectCash(Demontecolony, Row, Column + 1, NoofRows, NoofColumns)
    BottomRight = CollectCash(Demontecolony, Row + 1, Column + 1, NoofRows, NoofColumns)

    return Demontecolony[Row][Column] + max(TopRight, Right, BottomRight)

DemonteColony = [
    [16, 85, 12, 52],
    [58, 92, 73, 32],
    [81, 0, 2, 37],
    [16, 6, 158, 70]
]

print("MaxCash using normal recursion : ",GetMaxCash(DemonteColony, 4, 4))


# In the above process we calculate MaxCash at particular positions multiple times
# What if we store Max cash at all possible positions in Colony
# The second way is to take an extra space of size m*n and start computing values of states using memoization

# In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs
# by storing the results of expensive function calls and returning the cached result when the same inputs occur again.


def MaxCashUsingDP(DemonteColony, NoofRows, NoofColumns):

    # Create M * N space for storing None values initially
    DP = [[None for i in range(NoofRows)] for j in range(NoofColumns)]

    # Initilize MaxCash to 0
    MaxCash = 0

    # For each row in DemonteColony
    for i in range(NoofRows):

        # CollectCash for each row by calling CollectCashusingDP
        CashCollected = CollectCashUsingDP(DemonteColony, i, 0, NoofRows, NoofColumns, DP)
        # Keep track max of MaxCash from previous rows
        MaxCash = max(MaxCash, CashCollected)

    return MaxCash

print("MaxCash using Dynamic Programming : ",MaxCashUsingDP(DemonteColony, 4, 4))


def CollectCashUsingDP(DemonteColony, Row, Column, NoofRows, NoofColumns, DP):
    # Conditions for recursion to exit
    if Row < 0 or Row == NoofRows or Column == NoofColumns:
        return 0

    # If we already computed the Max at Row, Column position
    # Then we need not to compute it again
    # We can just return it
    if DP[Row][Column] != None:
        return DP[Row][Column]
    
    # Otherwise compute maxcash at position
    TopRight = CollectCashUsingDP(DemonteColony, Row - 1, Column + 1, NoofRows, NoofColumns, DP)
    Right = CollectCashUsingDP(DemonteColony, Row, Column + 1, NoofRows, NoofColumns, DP)
    BottomRight = CollectCashUsingDP(DemonteColony, Row + 1, Column + 1, NoofRows, NoofColumns, DP)

    # Store maxcash at Row, Column at DP[Row][Column]
    # So that if we encounter it again, we can just simply return it in the second step 
    DP[Row][Column] = DemonteColony[Row][Column] + max(TopRight, Right, BottomRight)
    
    return DP[Row][Column]


# Output

# MaxCash using normal recursion :  315
# MaxCash using Dynamic Programming :  315
# 81 + 6 + 158 + 70
