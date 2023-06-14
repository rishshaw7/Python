import random 
ran = int(input("Enter a number :\n"))

ran_num = random.randint(0,ran)
guesses = 0

while True:
    guesses += 1
    ran = input("Make a guess :\n")
    ran = int(ran)
    if ran == ran_num:
        print("You got it.")
        break
    else:
        if ran > ran_num:
            print("You are above the number :")
        else:
            print("You are below the number :")
        #print("You got'
        # 
        # \\65t7it;pppppppp;+ it wrong.")
        #continue

print("You got it in",guesses,"guesses.")