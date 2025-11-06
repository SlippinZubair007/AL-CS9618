#Write a code to calculate length of words in a file
count=0
try:
    with open("file2.txt","r") as f:
        for line in f:
            for word in line:
                count+=1
except Exception as e:
    print(f"{e}")
print("File Length: {count}")