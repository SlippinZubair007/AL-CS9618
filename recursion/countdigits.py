Count = 0

def WeCount(number):
     if number == 0:
         return count
     else:
         count += 1
         return WeCount(number//10)
print(WeCount(100))