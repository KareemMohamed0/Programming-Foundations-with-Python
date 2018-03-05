import os

# this function print all names of files  this directory


def rename_files():
    fil_list = os.listdir(
        r"G:\udacity nano degree\Programming-Foundations-with-Python\lesson2\files")
    print(fil_list)
    saved_path = os.getcwd()
    os.chdir(
        r"G:\udacity nano degree\Programming-Foundations-with-Python\lesson2\files")
    for file_name in fil_list:
        os.rename(file_name, file_name.strip("0123456789"))
    os.chdir(saved_path)


rename_files()
