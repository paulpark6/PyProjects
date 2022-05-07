import os
import shutil
import glob
print("This program will clean your laptop!")
user_want = input("what do you want to do with your file?\n 'delete' , 'move' , 'copy'\nType Here: ") # asks the user for copy, move, delete
if user_want == 'move':
    # program to move the file
    file_type = input("what type of file do you want to move.\nexample: (.txt, .bat, .jpg, .pdf ...)\nType Here: ") # type of file
    print("Type in the location where the files are. ")
    source = input("example:"+r'C:\Users\Paul Park\Desktop' + "\nType Here: ") # location of the "file_type"
    print("Type in where you want to move the files")
    print(r"example: C:\Users\Paul Park\Desktop\FileOrganizer")
    print("Type specific folder you want to put the files in")
    destination = input("Type Here:") # destination
    destination = destination + r"\files"
    print(os.list(source))

    # starts to move files
    # shutil.move(src=source, dst=destination)

# program to delete files
elif user_want == 'delete':
    # start writing here for deleting files
    file_type = input(
        "what type of file do you want to delete.\nexample: (.txt, .bat, .jpg...)\nType Here: ")  # type of file
    print("Type in the location where the files are. ")
    source = input("example:" + r'C:\Users\Paul Park\Desktop' + "\nType Here: ")  # location of the "file_type"
# program to copy files
elif user_want == 'copy':
    # start writing here for copying files
    file_type = input("what type of file do you want to copy.\nexample: (.txt, .bat, .jpg...)\nType Here: ")  # type of file
    print("Type in the location where the files are. ")
    source = input("example:" + r'C:\Users\Paul Park\Desktop' + "\nType Here: ")  # location of the "file_type"
    print("Type in where you want to copy the files")
    print(r"example: C:\Users\Paul Park\Desktop\FileOrganizer")
    print("Type specific folder you want to copy the files in")
    destination = input("Type Here:") # destination
# exit page
