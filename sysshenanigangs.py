import sys
import sys as s

# s.stdout.write("Hello World")  # standard out is used to output a statement

sys.platform  # outputs platform e.g. win32 (a string that contains a platform identifier)

# print(sys.copyright)  # A string containing the copyright of the python interpreter

# print(sys.version)  # a string that contains the version name of the python interpreter plus additional information on the build name and compiler used

# print(sys.stderr("Error?")) # standard error is used to output an error (colour = red)

# print(sys.getsizeof())  # get size of the variable in bytes
# a = 15
# b = 12.78
# c = "Helloooo world"
# d = ["list", 123, 123.56]
# print(sys.getsizeof(a))  # get size of the variable in bytes
# print(sys.getsizeof(b))  # get size of the variable in bytes
# print(sys.getsizeof(c))  # get size of the variable in bytes
# print(sys.getsizeof(d))  # get size of the variable in bytes

print(s.argv)  # list of command line arguments passed to a Python Script


