#Recursion is calling functions inside a function



#Runs infinitely  
def recurse(y):
    y=y+1
    print(y)

    recurse(y)

# Runs only 100 times 
def recurse(y):
    y=y+1
    print(y)
    if y<100:
        recurse(y)

recurse(0)





