def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}") # this line will return the answer to two decimal places.


def dollars_to_float(d):# accepts str as input formatted as $##.##, wherein each # is a decimal digit
    d = d.replace("$", "")  # is going to remove the leading $
    return float(d)         # converts the string into float


def percent_to_float(p): # accepts a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float
    p = p.replace("%", "")  # will remove the trailing %
    return float(p) / 100   # will return the % as a float.


main()