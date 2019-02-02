import random
i = 0
L = ["dogs", "part", "lego", "acid", "army"]
w = random.choice(L)
s = ['-', '-', '-', '-']
print(len(w), "letters")
while i <= 6:
    g = input("Enter here a letter here: ")
    f = w.find(g)
    if f == -1:
        i += 1
        print("Your letter isn't here")
        print(i, "out of 7 tries")
    else:
        s[f] = g
        for items in s:
            print(items, end=" ")
        if '-' not in s:
            print("\nYou WIN")
            quit()
if i == 7:
    print("Ran Out Of Tries")
    print("The word was " + w)
