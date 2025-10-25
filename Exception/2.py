try: 
    num=int(input("Enter a value: "))
    print(num)
except ValueError:
    print("Error : Integer only accepted")