#write a code that calculates the sum of all individual numbers in file2.txt

try:
 flag=True
 num=""
 total=0
 with open("file2.txt","r") as f:
    for line in f:
       for word in line:
          if word>='0' and word<='9':
             num+=word
          
          else:
             if num:
              total+=int(num)
              num=""
    print(f"Sum is : {total}")
except Exception as e:
    print(f"Error : {e}")
