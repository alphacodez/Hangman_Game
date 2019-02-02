import random
i = 1
L = ["dogs", "part", "lego"]
w = random.choice(L)
s = ['-', '-', '-', '-']
print(len(w), "letters")
while i <= 5:
    g = input("Enter here a letter here: ")
    f = w.find(g)
    if f == -1:
        i += 1
        print("Your letter isn't here")
    else:
        s[f] = g
        for items in s:
            print(items, end=" ")
        if '-' not in s:
            print("\nYou WIN")
            quit()
if i == 6:
    print("Ran Out Of Tries")
    print("The word was " + w)
