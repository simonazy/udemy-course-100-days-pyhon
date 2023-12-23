class MenuItem:
    def __init__(self, name, water, milk, coffee, cost) -> None:
        self.name = name 
        self.cost = cost 
        self.ingredient = {"water":water, 
                           "milk":milk, 
                           "coffee":coffee} 
        
class Menu:
    def __init__(self) -> None:
        self.menu = [
        MenuItem("latte", 200, 150, 24, 2.5),
        MenuItem("espresso", 50, 0, 18, 1.5),
        MenuItem("cappuccino", 250, 50, 24, 3)] 

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}" 
        return options 
    
    def find_drink(self, order_name):
        for item in self.menu:
            if order_name == item.name:
                return item 
        print("Sorry the item is unavailable.")



    
        
