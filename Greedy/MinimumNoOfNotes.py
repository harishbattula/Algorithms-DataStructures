# Consider a currency system in which there are notes of six denominations,
# namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
# If the sum of Rs. N is input, Find the smallest number of notes that will combine to give Rs. N.


N = int(input("Enter no of test cases : "))
arr = list()
for i in range(N):
    arr.append(int(input(f"Enter Amount {i+1} : ")))

# Intitilize zero no of notes for each amount
counts=[0] * N

# loop through each amount
for i in range(len(arr)):
    
    # if amount is not equal to zero
    while(arr[i] != 0):
        # Here we follow descending order of notes, because we want minimum no of notes 
        # that sums amount entered by user
        if arr[i] >= 100 :
            # if amount greater than specific note, then increase that
            # notecounts by 1
            counts[i] += 1
            # Decrease amount by note
            arr[i] -= 100
            # Continue the loop by skipping below steps
            continue
        if arr[i] >= 50 :
            counts[i] += 1
            arr[i] -= 50
            continue
        if arr[i] >= 10:
            counts[i] += 1
            arr[i] -= 10
            continue
        if arr[i] >= 5:
            counts[i] += 1
            arr[i] -= 5
            continue
        if arr[i] >= 2:
            counts[i] += 1
            arr[i] -= 2
            continue
        if arr[i] >= 1:
            counts[i] += 1
            arr[i] -= 1
            continue
    
# Output

# Enter no of test cases : 5
# Enter Amount 1 : 1254
# Enter Amount 2 : 350
# Enter Amount 3 : 129
# Enter Amount 4 : 2412
# Enter Amount 5 : 4432

# Output

# 15
# 4
# 6
# 26
# 48

for i in counts:
    print(i)
