# Create a list with 100 items
list = [0] * 100

# make a for loop, which run from 1 to 101
for x in range(1, 101):

    # make a for loop which run from 0 to the length of the list
    for y in range(len(list)):

        # if the ((y + 1) % x) is equal with 0, then change 0 to 1 
        # and 1 to 0
        if ((y + 1) % x == 0):
            if (list[y] == 0):
                list[y] = 1
            elif (list[y] == 1):
                list[y] = 0

print ("The following doors are open: ", end = "")

# print every list items, which is equal with 1
for x in range(len(list)):
    if (list[x] == 1):
        print ((x + 1), end=", ")

print()
