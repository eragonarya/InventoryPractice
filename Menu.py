from Item import Food, Dish, Item
class Menu:
    def __init__(self, validFood,validDish,validView,validUpdate,validExit):
        self.validFood = validFood
        self.validDish = validDish
        self.validView = validView
        self.validUpdate = validUpdate
        self.validExit = validExit
        self.foodInv = []
        self.dishInv = []
        self.inventory = [self.foodInv,self.dishInv]

    def getValidFood(self):
        return self.validFood
    def getValidDish(self):
        return self.validDish
    def getValidView(self):
        return self.validView
    def getValidUpdate(self):
        return self.validView
    def getValidExit(self):
        return self.validExit
    def getFoodInv(self):
        return self.foodInv
    def getDishInv(self):
        return self.dishInv
    def getInventory(self):
        inv = '\nINVENTORY\n'+ '---------\n'+'Food:\tName\tQty\tPrice\n'
        for i in self.foodInv:
            inv += '\t' + i.getName()[:5] + "\t"+ str(i.getQuantity()) + "\t" + str(i.getPrice()) + '\n'
        inv += '\nDish Items:\n'
        for i in self.dishInv:
            inv += '\t' + i.getName()[:5] + "\t"+ str(i.getQuantity()) + "\t" + str(i.getPrice()) + '\n'
        return inv

    def validateCommand(self,userInput):
        if userInput == self.validFood:
            return 1
        elif userInput == self.validDish:
            return 2
        elif userInput == self.validView:
            return 3
        elif userInput == self.validUpdate:
            return 4
        elif userInput == self.validExit:
            return 5
        else:
            return 0

    def getUserInput(self):
        print(Menu.__str__(self))
        user = input("Which option do you need?")
        result = self.validateCommand(user)
        return result

    def displayNewItem(self,userInput):
        name = input("Name of the item?")
        name = name.lower()
        qty = ''
        price = 0
        while not qty.isdigit():
            qty = input("How many do you have?")
            if not qty.isdigit():
                print("That isn't a proper quantity value.")
        qty = int(qty)
        while price == 0:
            price = input("How much does the item cost?")
        if userInput == 1:
            foodType = input("What kind of food is it?")
            isCold = input("Does this food item need to be refridgerated?[True/False]\n")
            food = Food(name,qty,price,foodType,isCold)
            self.foodInv.append(food)
            print(food)
            return food
        elif userInput == 2:
            dishType = input("What kind of dish is it?")
            isClean = input("Is this dish clean?[True/False]\n")
            dish = Dish(name,qty,price,dishType,isClean)
            self.dishInv.append(dish)
            print(dish)
            return dish
    def invUpdate(self,userInput):
        cat = 0
        for i in self.inventory:
            items = 0
            for j in i:
                if self.inventory[cat][items].getName() == userInput:
                    place = [cat,items]
                items += 1
            cat += 1
        print(place[0])
        if place[0] == 0:
            user = input("What needs to be changed?[Quantity,Price,Refridgerated]")
            if user == 'Quantity':
                user = input("Enter new quantity: ")
                self.inventory[cat][items].setQuantity(user)
            elif user == 'Price':
                user = input("Enter the new price: ")
                self.inventory[place[0]][place[1]].setPrice(user)
            elif user == 'Refridgerated':
                user = bool(input("Is this item a cold item?[True/False]"))
        elif place[0] == 1:
            user = input("What needs to be changed?[Name,Quantity,Price,Clean or Dirty]")


    def __str__(self):
        return ("Create a food: "+ self.validFood + "\n" +
        "Create a dish: " + self.validDish + "\n" +
        "View the Inventory: " + self.validView + "\n" +
        "Update current Inventory: " + self.validUpdate + "\n" +
        "Exit: " + self.validExit + '\n'
        )

menu = Menu("food","dish","view","update","exit")
currentInput = menu.getUserInput()
while currentInput != 5:
    if currentInput == 1 or currentInput == 2:
        menu.displayNewItem(currentInput)
        currentInput = menu.getUserInput()
    elif currentInput == 3:
        print(menu.getInventory())
        currentInput = menu.getUserInput()
    elif currentInput == 4:
        user = input("What is the name of the item you want to update?")
        menu.invUpdate(user)
        currentInput = menu.getUserInput()
    else:
        currentInput = 0
        print("I'm sorry, that wasn't an available command.")
        currentInput = menu.getUserInput()
