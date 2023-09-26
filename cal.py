def add(num1, num2):
  """Returns the sum of two numbers."""
  return num1 + num2

def subtract(num1, num2):
  """Returns the difference of two numbers."""
  return num1 - num2

def multiply(num1, num2):
  """Returns the product of two numbers."""
  return num1 * num2

def divide(num1, num2):
  """Returns the quotient of two numbers."""
  return num1 / num2

def main():
  operator = input("Enter an operator (+, -, *, or /): ")
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operator.")
    return

  print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
  main()
