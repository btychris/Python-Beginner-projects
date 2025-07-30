A = [1, 2, 3]
print(A)

# Append - insert element at the end of an array - On average: O(1)
A.append(5)
print(A)

# Pop - Deleting an element at the end of an array - O(1)
A.pop()
print(A)

# Insert (not at end of an array) - O(n)
A.insert(2, 5)
print(A)

# Modify an element -  O(1)
A[0] = 7
print(A)

# Accessing an element given an index i - O(1)
print(A[2])

# Checking if an array has an element - O(n)
if 6 in A:
    print(True)
else:
    print(False)

# Check length of an array - O(1)
print(len(A))