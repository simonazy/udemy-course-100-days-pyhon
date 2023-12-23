class CoffeeMaker:
    def __init__(self) -> None:
        self.resources = {
            "water":300,
            "milk": 200,
            "coffee":100
        } 

    def report(self):
        for resource in self.resources.items():
            print(f"{resource[0]}:{resource[1]}")  
        
        for resource in self.resources:
            print(f"{resource}: {self.resources[resource]}")


    def is_resource_sufficient(self, order):
        can_make = True 
        for i in order.ingredient:
            if order.ingredient[i] > self.resources[i]:
                print("Sorry there is not enough {i}") 
                can_make = False 
        return can_make  
    
    def make_coffee(self, order):
        for i in order.ingredient.item():
            self.resources[i[0]] -= i[1] 
        print(f"Here is your {order.name}. Enjoy!") 
