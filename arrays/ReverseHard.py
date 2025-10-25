#Update an element in an array
Games=["Uncharted","God of War","Call of Duty","Tekken","Last of Us"]
ReverseGame=["","","","",""]


#Reverse an array without using new arr
for x in range((len(Games)-1)//2):
    temp=Games[x]
    Games[x]=Games[len(Games)-1-x]
    Games[len(Games)-1-x]=temp
print("Reversed array without using new arr:", Games)


# WRITE A NOT SO SIMPLE PROGRAM TO REVERSE AN ARRAY
import random
arr=[]

try:
    Length = int(input("Enter the amount of elements you want in the array "))
except:
    print("Invalid syntax! Opting for a random length....")
    Length=random.randint(5,15)
    print("The random length is : ", Length )

for x in range(Length):
    arr.append(input("Enter the element of the array "))

    NewLength =((Length-1)//2)
if (NewLength==0):
    NewLength=1    
ReverseIndex = Length - 1

# arr =  [A , B , D , E , F , G , H]
# i       0   1   2   3   4   5   6
# L       1   2   3   4   5   6   7
for x in range(NewLength):  # o to 3
    temp = arr[x]
    arr[x] = arr[(ReverseIndex - x)]
    arr[(ReverseIndex - x)] = temp
print("The reversed array is:",arr)
