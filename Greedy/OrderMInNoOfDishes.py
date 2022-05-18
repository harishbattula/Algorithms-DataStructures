# Chef and Receipt

MenuAndPrices = {
    "Manchooria" : 1 ,
    "Biryani Rice" :2,
    "eel fried rice": 4,
    "grilled eel over rice":8,
    "deep fried eel bones":16,
    "Chicken Biryani":32,
    "Mutton Dhum Biryani":64,
    "France Biryani": 128,
    "OOL Meal":256,
    "Apollo big natoo": 512,
    "deluxe grilled eel over rice":1024,
    "eel full-course":2048
}

# Note that the i-th menu has the price 2i-1 (1 ≤ i ≤ 12).

# find the minimum number of menus whose total price is exactly p. 
# Note that if we orders the same menu twice, then it is considered as two menus are ordered.

N = int(input("Enter no of test cases : "))
arr = []
for i in range(N):
    arr.append(int(input(f"Enter price of dish{i+1} : ")))

# Above dict values in to a list using condition that we mentioned as note above
prices = [2**(i-1) for i in range(1, 13)]

# Initilize zeros no of orders for each amount entered by user
minnooforders = [0] * N

# For each test case we need to print the minimum no of dishes ordered
for i in range(N):
    # Last dish cost # 2048
    j = 11
    # If price is not equal to zero
    while(arr[i] != 0):
        # we loop through prices from last
        # if amount is greater than the price of the dish, we order it
        if arr[i] >= prices[j]:
            # If we order the dish, we need to minus amount from price entered by user
            arr[i] -= prices[j]
            # And increase the no of orders by 1
            minnooforders[i] += 1
        else:
            # if amount is less than price then we go to less price dish, repeat the same
            j -= 1

# Print the output
for i in minnooforders:
    print(i)

# Sample input

# Enter no of test cases : 5
# Enter price of dish1 : 156
# Enter price of dish2 : 2048
# Enter price of dish3 : 5
# Enter price of dish4 : 1500
# Enter price of dish5 : 256

# Output

# 4
# 1
# 2
# 7
# 1
