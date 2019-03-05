import os

a = "+"
b = "-"
c = "--"
count = 0

def Restart() :
    global count
    clear = lambda: os.system("cls")
    print("Please use + to add 1 to the counter,")
    print("Please use - to subtract 1 from the counter,")
    print("Please use -- to reset the counter,")
    print(" ")
    print("Current Count: " + str(count))
    print(" ")

    Symbol = input()
    if Symbol == a:
        count = count + 1
        clear()
        Restart()
    elif Symbol == b:
        count = count - 1
        clear()
        Restart()
    elif Symbol == c:
        count = 0
        clear()
        Restart()
    else:
        clear()
        Restart()

Restart()