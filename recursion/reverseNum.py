def reverse(n,res=0):
    if n==0:
        return res
    else:
        return reverse(n//10,res*10+n%10)

print(reverse(25))


#Normal code 

n=125

res=0
while n>0:
    term=n%10  #1
    res=res*10 + term #521
    n=n//10 
print(res)
