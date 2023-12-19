# datatypes

def day_2_project():
    print("====Welcome to the tip calculator====")
    total_bill = input("What was the total bill? ")
    tip_perc = input("What is the percentage of tip? ")
    num_persons = input("How many persons? ")
    price = round(int(total_bill)*(1+int(tip_perc)/100)/int(num_persons),2)
    print(f"Everyone should pay {price}")

if __name__ == "__main__":
    day_2_project()