try:
    file=open("file.txt","r")
except IOError:
    print("File does not exist")