import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiplay(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {"+": add,
             "-": subtract,
             "*": multiplay,
             "/": divide,
    }
def calculator():
    print(art.logo)
    num1 = float(input("What is the first number?:"))
    for symbol in operations:
        print(symbol)
    end_calculation = False
    while not end_calculation:
        #calculation_function = 0
        operation_symbol = input(" Pic an opration :")
        num2 = float(input("What is the next number?:"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f" {num1} {operation_symbol} {num2} = {answer}")
        countinue = input(f"Type 'y' to continue calculating with {answer} type 'r' to restart or type 'no' to exit: ").lower()
        if countinue == "n":
            print("Goodbye")
            end_calculation = True
        elif countinue == "r":
            end_calculation = True
            calculator()
        else:
            num1 = answer
calculator()       
