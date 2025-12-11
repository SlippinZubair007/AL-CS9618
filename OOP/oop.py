class Character:
    def __init__(self,CharacterName,DateOfBirth,Intelligence,Speed):
        self.__CharacterName = CharacterName
        self.__DateOfBirth = DateOfBirth
        self.__Intelligence = Intelligence
        self.__Speed = Speed

    def SetIntelligence(self,Intelligence):
        self.__Intelligence = Intelligence

    def GetIntelligence(self):
        return self.__Intelligence
    
    def GetName(self):
        return self.__CharacterName
    
    def Learn(self):
        self.__Intelligence=self.__Intelligence * 110/100
    
    def ReturnAge(self):
        currentYear=2023
        age=currentYear-int(self.__DateOfBirth.split("/")[2])
        return age

Zubair=Character("Zubair","12/05/2004",100,80)
print(Zubair.GetName())
print("Intelligence before learning: ",Zubair.GetIntelligence())
Zubair.Learn()
print("Intelligence after learning: ",Zubair.GetIntelligence())
print("Age: ",Zubair.ReturnAge())




