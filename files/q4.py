count=0
try:
 with open("file1.txt","r") as f:
    for line in f:
       for word in line:
          if word.upper()=='A' or word.upper()=='E' or word.upper()=='I' or word.upper()=='O' or word.upper()=='U':
             count+=1
except Exception as e:
    print(f"Error: {e}")
print(f"Number of vowels: {count}")