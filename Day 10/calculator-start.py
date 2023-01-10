from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


oprations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculate():
  end_cal = False
  num1 = float(input("What's the first number?:"))
  for oprator in oprations:
      print(oprator)
  
  while not end_cal:
      opration_symbol = input("Pick an opration:")
      new_num = float(input("What's the next number?:"))
      function = oprations[opration_symbol]
      result = function(num1, new_num)
      print(f"{num1} {opration_symbol} {new_num} = {result}")
      choice = input(
          f"Type 'y' to continue calculating with {result},or type 'n' to exit.")
      if (choice == 'y'):
          num1 = result
      else:
          end_cal = True
          calculate()

calculate()