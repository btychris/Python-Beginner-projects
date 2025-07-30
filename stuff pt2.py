# password = input("Enter thy password: ")
#
# if len(password) < 8:
#     print("Yo password wack!")
# else:
#     print("Yo password strong fr fr gang")

# string[position]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
FirstCharacter = alphabet[0]
LastCharacter = alphabet[25]

# string[start:end]

# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print("The first 5 letters of the alphabet are: " + alphabet[:5])
# print("The last 5 letters of the alphabet are: " + alphabet[-5:])
# print("The letters in between are: "  + alphabet[5:-5])

date = "05 January 2019"
day = date[:2]  #First 2 characters
year = date[-4:] #Last 4 characters
month = date[3:-5] #The remaining characters in the middle


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pos = alphabet.find("C")
print("Letter C is at position: " + str(pos))