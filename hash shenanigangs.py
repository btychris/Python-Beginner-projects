# Hashsets

s = set()
print(s)

# Add item into set -  O(1)
s.add(1)
s.add(2)
s.add(3)

print(s)

# Lookup if item in set -  O(1)
if 1 in s:
    print(True)

# Remove item from set - O(1)
s.remove(3)
print(s)

string = "slanasnajsnaknwufwqofno39neosidoias"
sett = set(string)  # set construction - O(s) - S is the length of the string
print(sett)

# loop over items in set - O(n)
for x in s:
    print(x)

# Hashmaps - Dictionaries

d = {"greg": 1, "steve":2, "chris":3}
print(d)

# Add key:val in dictionary: O(1)
d["arsh"] = 4
print(d)

# Check for presence of key in dictionary: O(1)
if "greg" in d:
    print(True)

# Check value corresponding to key in the dictionary: O(1)
print(d["greg"])

# Loop over the key:val pairs of the dictionary: O(n)

for key, val in d.items():
    print(f"key {key}: val {val}")

# Defaultdict

from collections import defaultdict

default = defaultdict(list)
default[2]

print(default)

# Counter

from collections import Counter

counter = Counter(string)
print(counter)