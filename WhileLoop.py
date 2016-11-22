num = 45
run = True
while run:
    guess = int(input("Enter the number: "))
    if guess == num:
        print("Congratulaions u guessed it.")
        run = False
    elif guess < num:
        print ("less, the number is little higher than that")
    else:
        print ("no its little lower than that")
else:
    print ("the loop is over")

print ("Done")
