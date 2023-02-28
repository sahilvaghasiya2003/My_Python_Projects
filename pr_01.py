#Q-1.  Wrte a program to open three files 1.txt, 2.txt, 3.txt. If any of this
# file are not present ,a message without exiting the program must be
# printed promotive  the same.

def readfile(fileName):
    try:
        with open (fileName, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {fileName} is not found")
readfile("file1.txt")
readfile("file2.txt")
readfile("file3.txt")

