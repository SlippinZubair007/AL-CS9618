FLAG = False

c = (input("Enter a number :"))
d = (input("Enter a number :"))

if type(c) == type(d) :
    if isinstance(c,int) and isinstance(b,int) :
        FLAG = True

while FLAG != True:                                          
    print("Both numbers must be integers!! Enter Again :")
    c = input("Enter first num :")
    d = input("Enter second num :")
    if type(c) == type(d):
        if isinstance(c,int) and isinstance(d,int):
            FLAG = True        

if c % d == 0 :
    print("The numbers are even")
elif c % d != 0 :    
    print("The numbers are not even")