# Two types of loops in python
# 1. for loop 
# 2. while loop

#syntax for counter controlled loop
for x in range(100):
    print("Hello World")

for x in range(10):
    name=input("Enter your name: ")
    print(name)

# Pre condition loop
while x<10: 
    print("Hello World")
    x+=1


# Write a code that takes 3 numbers as input and calculates their sum , average and outputs the highest and lowest number
sum=0
x=0
high=-10000
while x<3:
    num=int(input("Enter number "))
    sum += num
    x+=1
if num>high:
    high=num

    print("Sum: ", sum)
    print("Average: ",sum/3)
    print("Highest: ", high)

#Write a code that takes 5 numbers as input from user and prints how many are negative and positive
pos=0
neg=0

for x in range(5):
    num=int(input("Enter number: "))
    if num>0: 
        pos+=1
    elif num<0:
        neg+=1

print("Positive : ",pos , "Negative: ",neg)

#arrays 
arr=[2,3,6,10]

for x in range(len(arr)):
    print(arr[x])

# # Write a code that checks if a number is prime or not
# # Write a linear search code 
# # Write an ineffcient bubble sort 
# # Write an effcient bubble sort 

