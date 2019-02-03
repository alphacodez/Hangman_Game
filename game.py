import random
i = 0
L = ["apple", "fruit", "food", "supercalifragilisticexpialidocious", "human", "game", "word"]
w = random.choice(L)
s = []
for letter in w:
    s.append("-")
print(len(w), "letters")
while i <= 6:
    g = input("Enter a letter here: ")
    f = w.find(g)
    if f == -1:
        i += 1
        print("Your letter isn't here")
        print(i, "out of 7 tries used")
    else:
        for n in range(len(w)):
            if w[n] == g:
                s[n] = g
        for items in s:
            print(items, end=" ")
        if '-' not in s:
            print("\nYou WIN")
            quit()
if i == 7:
    print("Ran Out Of Tries")
    print("The word was " + w)
