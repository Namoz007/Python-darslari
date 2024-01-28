class student:
    def __init__(self,name,lastname,dateofbirth,rates:int) -> None:
        self.name = name
        self.lastname = name
        self.dateofbirth = dateofbirth
        self.rates = list(rates)

    def setName(self):
        self.name = input("Enter your new name: ")
        print("You are name update succes.")
    
    def getName(self):
        print(f"You are name: {self.name}")
    
    def addRAde(self):
        self.rates.append(int(input("Enter yuor rates: ")))
    
    def removeRate(self):
        self.rates.remove(int(input("You remove rates: ")))
    
    def getAge(self):
        print(f"Your age: {2023 - self.dateofbirth}")    