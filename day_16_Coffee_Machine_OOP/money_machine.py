class MoneyMachine:
    # attributes : global
    CURRENCY = "$"
    COIN_VALUES = {
        "quarter": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    } 
    
    def __init__(self) -> None:
        self.profit = 0 
        self.money_received = 0 

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}") 

    def process_coins(self):
        print("Please insert coins: ")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin} do you insert? "))*self.COIN_VALUES[coin]
        return self.money_received 
    
    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            print(f"Here is you chage of {round(self.money_received-cost,2)}")
            self.profit += cost 
            self.money_received = 0 
        else:
            print("Not enough money. Money refunded")
            self.money_received = 0
            return False 

    

