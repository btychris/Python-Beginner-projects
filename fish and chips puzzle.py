# The Fish and Chips Puzzle - www.101computing.net/the-fish-and-chips-puzzle/
# Complete lines 9,10 and 11, so that line 6 outputs “fish and chips”.
# You must comply with the following rules:
# You are only allowed to use 4 keys on your keyboard: a, b, c and =. You can use these keys as many times as necessary.
# You are not allowed to change lines 7,8 or 12.

a = "chips"
b = "fish"
c = b  # c is now fish
b = a  # b is now chips
a = c # a is now fish
print(a + " and " + b)