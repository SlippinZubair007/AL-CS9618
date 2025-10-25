def POWER(Number, Power):
        if Power == 0:
            return 1
        else:
            Power = Power - 1
            return POWER(Number, Power) * Number
print(POWER(3,2))

