i = 1
w = "words"
while i <= 5:
    g = input("Enter here: ")
    if w == g:
        print("yay")
        break
    else:
        i += 1
if i == 6:
    print("Ran Out Of Tries")
else:
    print("That's All Folks")
