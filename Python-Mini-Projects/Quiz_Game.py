print("Welcome to the quiz game")

play = input("Would you like to play? ")
score = 0
if play.lower() not in ['yes', 'y']:
    quit()

print("Okay! Let's start the quiz :)")

ans = input("What does CPU stand for? ")

if ans.lower() == "central processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

ans = input("What does GPU stand for? ")

if ans.lower() == "graphics processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

ans = input("What does HDD stand for? ")

if ans.lower() == "hard disk drive":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

ans = input("What does RAM stand for? ")

if ans.lower() == "random access memory":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

ans = input("What does PSU stand for? ")

if ans.lower() == "power supply unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print(f"Your scored is",score)
print(f"You got",((score/5)*100),"%.")

if score == 5:
    print("Remark : Outstanding")
elif score == 4:
    print("Remark : Good")
elif score == 3:
    print("Remark : Average")
elif score == 2:
    print("Remark : Work hard")
elif score == 1:
    print("Remark : Poor")
elif score == 0:
     print("Remark : Very Poor")