def drink(money):
    if money >= 2:
        return print("You have got drink for yourself.")
    else:
        return print("You haven't got drink for yourself.")
    
drink(2)
drink(5)
drink(1)

def alcohol(age,money):
    if(age>=21) and (money>=2):
        return print("You're getting drink.")
    elif(age<21) and (money>=2):
        return print("According to US federation law kids weren't allow to drink allow so you're not getting drink.")
    elif(age>=21) and (money<2):
        return print("Comeback with more money.")
    elif(age<21) and (money<2):
        return print("You are to young to drink alcohol and you don't have sufficient amount of money to buy an alcohol.")
    #OR
    else:
        return print("You are to young to drink alcohol and you don't have sufficient money to buy an alcohol.")