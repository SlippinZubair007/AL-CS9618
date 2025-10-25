# #inefficient way of bubblesort

arr1=[1,4,9,10,5]
for x in range(len(arr1)):
    for y in range(len(arr1)-1):
        if arr1[y]>arr1[y+1]:
            temp=arr1[y]
            arr1[y]=arr1[y+1]
            arr1[y+1]=temp
print("Sorted array using bubble sort:", arr1)

#Efficient way of bubblesort
arr2=[1,4,9,10,5]
Noswaps=False
Boundary=len(arr2)-1
while Noswaps==False:
      Noswaps=True
for y in range(Boundary):
            if arr2[y]>arr2[y+1]:
              temp=arr2[y]
              arr2[y]=arr2[y+1]
              arr2[y+1]=temp
              Noswaps=False
Boundary-=1 # Reduce last element because its swapped after one cycle 

print("Sorted array using bubble sort:", arr2)


    