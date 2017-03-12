class Item:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def getName(self):
        return self.name
    def setName(self,newValue):
        self.name = newValue
    def getQuantity(self):
        return self.quantity
    def setQuantity(self,newValue):
        self.quantity = newValue
    def getPrice(self):
        return self.price
    def setPrice(self,newValue):
        self.price = newValue
    def __str__(self):
        return ("Item Name: " + self.getName() + "\n" +
        "Amount of Items: " + str(self.getQuantity()) + "\n" +
        "Price of Item: " + str(self.getPrice())
        )

class Food(Item):
    def __init__(self,name,quantity,price,food_type,isCold):
        super(Food,self).__init__(name,quantity,price)
        self.type = food_type
        self.cold = isCold
    def getType(self):
        return self.type
    def getCold(self):
        return self.cold

    def eat(self):
        self.quantity -= 1
        if self.getQuantity() == 1:
            return ("You just ate an " + self.getName() + '! There are ' + str(self.getQuantity()) + ' ' + self.getName() + " left.")
        else:
            return ("You just ate an " + self.getName() + '! There are ' + str(self.getQuantity()) + ' ' + self.getName() + "'s left.")

    def spoil(self,quantity):
        self.quantity -= quantity
        return ("You have lost " + str(self.getQuantity()) + ' ' + self.getName() + "'s because they have spoiled.")
    def __str__(self):
        return (Item.__str__(self) + '\nFood Type: ' + self.getType() + "\nNeed Refridgeration: " + str(self.getCold())+'\n')
class Dishes(Item):
    def __init__(self,name,quantity,price,dishType,isClean):
        super(Dishes,self).__init__(name,quantity,price)
        self.dish = dishType
        self.clean = isClean
        self.stored = 0
    def getDishType(self):
        return self.dish
    def getIsClean(self):
        return self.clean
    def putAway(self, Amount):
        self.stored += Amount
        return "You have put away " + str(Amount) + ' ' + self.getName() + "'s "
    def broke(self):
        self.quantity -= 1
        return "You broke a " + self.getName() + '. You have ' + str(self.getQuantity()) + ' left.'
    def __str__(self):
        return (Item.__str__(self) + '\nDish Type: ' + self.getDishType() + '\nCurrently Clean: ' + str(self.getIsClean()) + '\n')
# newApple = Food('apple',10,2.25,'fruit',False)
# print(newApple)
# newPlate = Dishes('Orange Plate', 5,8.00,'Plate',True)
# print(newPlate)
# print(newApple.eat())
# print(newApple.spoil(3))
# print(newPlate.putAway(2))
# print(newPlate.broke())
