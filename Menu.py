from Item import Food, Dish, Item
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

    def displayNewItem(self,userInput):
        name = input("Name of the item?")
        qty = input("How many do you have?")
        price = input("How much does the item cost?")
        if userInput == 1:
            foodType = input("What kind of food is it?")
            isCold = input("Does this food item need to be refridgerated?[True/False]")
            food = Food(name,qty,price,foodType,isCold)
            print(food)
            return food
        elif userInput == 2:
            dishType = input("What kind of dish is it?")
            isClean = input("Is this dish clean?[True/False]")
            dish = Dish(name,qty,price,dishType,isClean)
            print(dish)
            return dish


    def __str__(self):
        return ("Create a food: "+ self.validFood + "\n" +
        "Create a dish: " + self.validDish + "\n" +
        "View the Inventory: " + self.validView + "\n" +
        "Exit: " + self.validExit
        )

menu = Menu("food","dish","view","exit")
currentInput = menu.getUserInput()
while currentInput != 4:
    if currentInput == 1 or currentInput == 2:
        menu.displayNewItem(currentInput)
        currentInput = menu.getUserInput()
    elif currentInput == 3:
        print("View")
        currentInput = menu.getUserInput()
    else:
        currentInput = 0
        print("I'm sorry, that wasn't an available command.")
        currentInput = menu.getUserInput()
