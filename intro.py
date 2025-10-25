
#No need to need to declare variables
name='Zubair Khan'
age=18

#Print is used to output
print("Name: ", name)
print("Age: ",age)

# returns datatype of variable
print(type(name))
print(type(age))

#Input 
age=int(input("Enter your age: "))
print(type(age))

print (f"Hello you are {age} years old.")

# if else conditions 
if age>18: 
    print("Ypu are an adult")
elif age==18:
    print("You are 18 years old")
else:
    print("You are a minor")


# Write a code that takes two inputs and reverses them 
num1=int(input("Enter Number 1: ")) 
num2=int(input("Enter Number 2: ")) 

temp=num1
num1=num2
num2=temp
print("Number 1: ", num1)
print("Number 2: ", num2)


# Write a basic calculator that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding operation
# Write a code that takes a string as input and prints it in reverse order
# Write a code that checks if a number is even or odd








