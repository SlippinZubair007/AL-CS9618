#Write a code that takes 50 inputs , calculates min , max and prints avg

sum=0
max=-10000
min=10000
for x in range(0,3):
    marks=int(input("Enter your marks\n"))

    if marks>max:
        max=marks

    if marks<min:
        min=marks
    
    sum=sum+marks #(sum+=num)

avg=sum/50

print(f"Total sum: {sum}\n")
print(f"Total min: {min}\n")
print(f"Total max: {max}\n")
print(f"Total avg: {avg}\n")




