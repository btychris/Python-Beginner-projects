import os
from datetime import datetime

# print("\n\n\n")
# print(os.getcwd())
#
os.chdir("C:/Users/chris/PycharmProject/")
# print(os.getcwd())


# os.mkdir("osdemo")  # makes the directory, but you cant make a sub-directory
# os.makedirs("os-demo/subdir")  # makes the directory, but you can make a sub-directory

# os.rmdir("osdemo")
# os.rmdir("os-demo/subdir")

# os.rename("osdemo", "demo")

# mod_time = os.stat("demo").st_mtime # gives you stats and if you copy the variable name and put .something, it will print thy stat
# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filename in os.walk("C:/Users/chris/PycharmProject/"):
#     print("Current path:", dirpath)
#     print("Directories:", dirnames)
#     print("Files:", filename)

#    print(os.environ.get("HOME"))
#
# file_path = os.path.join(os.environ.get("HOME"), "text.txt")

# print(os.path.exists("/temp/test.txt"))
print(os.path.splitext("/temp/test.txt")) # removes the extentions

# print(os.listdir())  # shows files in the Pycharm Project directory