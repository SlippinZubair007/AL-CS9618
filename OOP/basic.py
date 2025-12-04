#Create a class named "Flareprep"
class Flareprep:
    def __init__(self,name,age,batch,student):
        self.name=name
        self.age=age
        self.batch=batch
        self.student=student

    def display(self):
        if self.student:
            print("Student Information:")
            print("Name: " ,self.name ," Age: ",self.age," Batch: ",self.batch)
        else:
             print("Teacher Information:")
             print("Name:" ,self.name ," Age:",self.age," Batch:",self.batch)
    
Zubair=Flareprep("Zubair","21","2019",False)
Zubair.display()
Amna=Flareprep("Amna","21","2019",False)
Amna.display()
Ali=Flareprep("Ali","15","2025",True)
Ali.display()