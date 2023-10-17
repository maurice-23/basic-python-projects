import random
random_num = random.randint(0, 11)
trial = 0


while True:
    trial += 1
    user_number = input("Enter a number: ")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number <=0: 
            print("please enter a number larger than 0 next time")
            continue
    else:
        print("Please Enter a number")

    random_num = random.randint(0, user_number)
    if user_number == random_num:
        print("congz 🎉🎇🎉 You got it!")
        print("You have tried " + str(trial) + " times")
        break 
    else:
        if user_number > random_num:
            print("You were above the number")
        else:
            print("you were below")
        print("You grab the wrong number! 😥")
        continue
 