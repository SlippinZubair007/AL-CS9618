#Sum of first N numbers
#be.g 1+2+3+4..+N
result=0
def sum(N):
    if N==0:
        return 0
    else:
        return N+sum(N-1)

result=(sum(10))
print(result)