class Menu:
    def __init__(self, validFood,validDish,validView,validExit):
        self.validFood = validFood
        self.validDish = validDish
        self.validView = validView
        self.validExit = validExit

    def getValidFood(self):
        return self.validFood
    def getValidDish(self):
        return self.validDish
    def getValidView(self):
        return self.validView
    def getValidExit(self):
        return self.validExit

    def validateCommand(self,userInput):
        if userInput == self.validFood:
            return 1
        elif userInput == self.validDish:
            return 2
        elif userInput == self.validView:
            return 3
        elif userInput == self.validExit:
            return 4
        else:
            return 0

    def getUserInput(self):
        print(Menu.__str__(self))
        user = input("Which option do you need?")
        result = self.validateCommand(user)
        return result

    def __str__(self):
        return ("Create a food: "+ self.validFood + "\n" +
        "Create a dish: " + self.validDish + "\n" +
        "View the Inventory: " + self.validView + "\n" +
        "Exit: " + self.validExit
        )

menu = Menu("food","dish","view","exit")
print(menu.getUserInput())
