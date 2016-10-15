def addition(num_one, num_two):
    add = num_one + num_two
    return add

def substraction(num_one, num_two):
    subs = num_one - num_two
    return subs

def multiplication(num_one, num_two):
    mult = num_one * num_two
    return mult

def division(num_one, num_two):
    div = num_one / num_two
    return div

number1 = input("Enter a number (or a latter to exit): ")


while (number1.isnumeric() == True):

    sign = input("Enter an operation: ")
    # convert the output from string to integer
    number2 = int(input("Enter another number: "))

    if sign == "+":
        # convert number1 from string to integer before the function
        print ("Result: " + str(addition(int(number1), number2)), "\n")

    if sign == "-":
        print ("Result: " + str(substraction(int(number1), number2)), "\n")

    if sign == "*":
        # the next line is only 78 characters :)
        print ("Result: " + str(multiplication(int(number1), number2)), "\n")

    if sign == "/":
        print ("Result: " + str(division(int(number1), number2)), "\n")

    number1 = input("Enter a number (or a latter to exit): ")
    # the while loop is running while the number1.isnumeric() is True
