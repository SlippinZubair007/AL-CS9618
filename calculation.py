sum=0
a = int(input("Enter first: "))
b = int(input("Enter second number: "))
c = int(input('enter third number: '))
sum=a+b+c
print("The sum is:", sum)
average = sum / 3
print("The average is:", average)

if a>b and  a >c: 
    print("Max : ", max)
elif b>a and b>c:
    print("Max : ", b)
else:
    print("Max : ", c)    