import random
i = 1
L = ["Word", "Part", "Parts"]
w = random.choice(L)
while i <= 5:
    g = input("Enter here: ")
    if w == g:
        print("yay")
        break
    else:
        i += 1
if i == 6:
    print("Ran Out Of Tries")
    print("Your word was " + w)
else:
    print("That's All Folks")
