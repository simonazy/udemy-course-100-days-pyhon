from art import logo 

def add(n1, n2):
    return n1+n2 

def subtract(n1, n2):
    return n1-n2 

def multiply(n1, n2):
    return n1*n2 

def divide(n1, n2):
    if n2 != 0:
        return float(n1/n2) 
    else:
        return "Error: Cannot divide by zero."

def get_operator():
    return input("Please choose your operator from: +, -, *, % ") 

def check_operator(operator):
    operators = {"+":add, "-":subtract, "*":multiply, "%":divide}
    while operator not in operators.keys():
        operator = get_operator()
    return operators[operator]


def main():
    print(logo)
    input1 = float(input("Please input first number: "))
    while True:
        input_operator = get_operator() 
        func = check_operator(input_operator)
        input2 = float(input("Please input a number: ")) 
        print(func(input1, input2)) 
        input1 = func(input1, input2)
        user_input = input("Do you want to continue: yes, no ") 
        if user_input.lower() == "no":
            main()
        else:
            True
    
main()