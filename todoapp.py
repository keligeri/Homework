import sys
command = input("Please specify a command [list, add, mark, archive or x]: ")
# file = open("todo.txt", "a")
x = 1

# add parancs hatására, beolvassa a fájlt, majd bele írja a fájlba az item-et
if command == "add":
    item = input("Add an item: ")
    file = open("todo.txt", "a")
    file.write(item + "\n")
    print ("Item added.")
    file.close()

# kilistázza a file-ban kévő line-okat
elif command == "list":
    file = open("todo.txt", "r+")
    print ("\n" + "You saved the following to-do items: ")
    for line in file:
        print (x, "[]", line, end='')
        x += 1
    file.close

# megnyitja újra írás módban a fájlt, tehát felülírja a régit és létrehoz egy üreset
elif command == "archive":
    file = open("todo.txt", "w+")
    print ("All completed tasks got deleted :)")
    file.close()

elif command == "mark":
# először is beolvassuk a fájlt
    file = open("todo.txt", "r")

# majd a fájl sorait belepakoljuk a lines változóba
    lines = file.readlines()
    print ("\n" + "You saved the following to-do items: ")
    
    # vissza kell állítani az elejére a kurzort!!!
    file.seek(0)
    for line in file:
        print (x, "[]", line, end="")
        x += 1
   
# bezárjuk a fájlt
    file.close()

    marked = int(input("Which one you want to mark as completed: "))

# megnyitjuk újra, írási módban
    f = open("todo.txt", "w+")
    
    x = 1
    for line in lines: 
        f.write(line)
        print (line)
    
    f.close()

# ha mást kap be, mint a kiírt szavak akkor kilép
else:
    exit()