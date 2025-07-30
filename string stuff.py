# Append at end of string - O(n)
s = "Hello"

b = s + "z"
print(b)

# Check something is in a string - O(n)
if "e" in s:
    print(True)

# Access positions
print(s[2])

# Check length of a string - O(1)
print(len(s))