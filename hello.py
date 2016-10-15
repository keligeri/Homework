import sys

def argument():

    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"

    return name

def welcome():
    print ("Hello " + argument() + "!")

welcome()
