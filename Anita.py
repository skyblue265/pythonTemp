from Car import Car

class Flower:
    Color = ""
    def ShowMyFlower(self):
        Print("My Flower is "+self.Color)
class Bag:
    Color = ""
    def ShowMyBag(self):
        Print("My Bag is "+self.Color)

class Anita:
    Name = "Anita"
    Country = ""
    Hobby = ""
    Height = 0
    Weight = 0
    MyCar = Car()
    MyFlower = Flower()
    MyBag = Bag()
    def intro(self):
        print("hello I'm"+self.Name+"my hobby is"+ self.Hobby + ", my weight is "+ str(self.Weight))

class Account:
    ID = "skyblue265"
    Password = "love1342"
