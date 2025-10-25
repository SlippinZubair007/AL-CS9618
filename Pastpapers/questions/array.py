
arr=[]
def ReadData():
 file=input("Enter file name (e.g file.txt)\n")
 try:
  with open(file,'r') as f: #(while not EOF)
    for line in f: 
     arr.append(line.strip())
 except Exception as e:
  print(f"Error:{e}")
 return arr

def SplitData(DataArray):

    red=[]
    blue=[]
    green=[]
    yellow=[]
    pink=[]
    orange=[]
    for element in DataArray:
        color=element.split(',')[0]
        num=element.split(',')[1]

        if color=='red':
         red.append(num)
        elif color=='blue':
         blue.append(num)
        elif color=='yellow':
         yellow.append(num)
        elif color=='green':
         green.append(num)
        elif color=='orange':
         orange.append(num)
        else:
         pink.append(num)
    print(f"Red array: {red}")
    print(f"Blue array:{blue}")
    print(f"Green array:{green}")
    print(f"Yellow array:{yellow}")
    print(f"Orange array:{orange}")
    print(f"Pink array:{pink}")
  
   

ReadData()
print(f"Array after function ReadData()\n:{arr}")
SplitData(arr)