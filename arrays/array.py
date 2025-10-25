
#Declare 1D array
Games=["Uncharted","God of War","Call of Duty","Tekken"]

#Access/print a specific element inside an array 
print(Games[1])

#Find the length of an array
print(len(Games))

#Print all element in an array
print("Print all elements in an array:") 
for gameNumber in range(len(Games)):     
    print(Games[gameNumber])

#Append an element to an array
print("Append an element to an array:")
Games.append("Last of us")
print(Games[len(Games)-1])

#Input an element to an array
print("Input an element to an array:")
Games.append(input("Enter another game name: "))


Games=input("Enter a game name: ").split() # This will replace the entire Games list

#Implement a linear search code in an array
Students=["Ahmad","Fahad","Haseeb","Aleena"]
size=len(Students)
flag=False

target=input("Enter the name of the student you want to search: ")
x=0
while flag==False & x<=size:
    if (Students[x]==target):
        print("Student found at index:",x)
        flag=True
    x=x+1




