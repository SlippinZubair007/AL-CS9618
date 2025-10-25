
def fibonacci(n):
    num1=0
    num2=1
    num3=0

    for x in range(n):
        print(num1)
        num3=num1+num2
        num1=num2
        num2=num3
        

fibonacci(9)

def fibonacci(n):
    if n<=1: 
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

n=int(input("Enter the length of fibonacci: "))

for x in range(n):
   print(fibonacci(x))

