## 1. Get the single-line user input
expression = input("What is your arithmetic expression? ")

# 2. Split the input string into three parts: x, y, z
x_str, y_operator, z_str = expression.split()

# 3. Convert the numbers from strings to floats
x = float(x_str)
z = float(z_str)

# 4. Use a match statement to check the operator and perform the calculation
match y_operator:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z
    case _:
# This case will handle any invalid operator
        result = "Error: Invalid operator" 

# This part of the code is going to print the answer to one decimal place.
print(f"{result:.1f}") 

