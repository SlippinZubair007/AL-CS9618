#Generate a binary number of any given number 
#4 = 0100
#3 = 0011

#2=0010
def binary(n,result=""):
    if n==0:
        return "0"
    if n==1:
        return "1"
    else:
      return str(binary(n//2)) + str(n%2)

print(binary(3))


    