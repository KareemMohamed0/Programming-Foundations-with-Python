import os

# this function print all names of files at this directory


def rename_files():
    fil_list = os.listdir(
        r"G:\udacity nano degree\Programming-Foundations-with-Python\lesson2\files")
    print(fil_list)


rename_files()
