class Baby:
    def __init__(self,name,IQ):
        self.name=name
        self.IQ=IQ

    def __Display(self):
        print(self.name , " " , self.IQ)

    def accessPrivate(self):
        self.__Display()

Haseeb=Baby("Haseeb",100)
Haseeb.accessPrivate()

Zubair=Baby("Zubair",80)
Zubair.accessPrivate()

# print(Haseeb.name , " " , Haseeb.IQ)






