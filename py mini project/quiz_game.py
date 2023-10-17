playing = input("Do u want to play? ")
if playing != "yes": 
    quit()

print("okay Lets play :) ")
marks = 0
answer = (input("What does sql stands for? ")).lower()
if answer == "structured query language": 
    marks += 1
    print("Correct! ")
else:
    print("Incorect! ")
    
answer2 = (input("What does PHP stands for? ")).lower()
if answer2 == "hypertext preprocessor": 
    marks += 1
    print("Correct! ")
else:
    print("Incorect! ")
    
answer3 = (input("What does JS stands for? ")).lower()
if answer3 == "javascript": 
    marks += 1
    print("Correct! ")
else:
    print("Incorect! ")
    
answer4 = (input("What does DBA stands for? ")).lower()
if answer4 == "database administrator": 
    marks += 1
    print("Correct! ")
else:
    print("Incorect! ")
    
answer5 = (input("What does OS stands for? ")).lower()
if answer5 == "operating system":
    marks += 1 
    print("Correct! ")
else:
    print("Incorect! ")
marks  = int(marks)
print("You got " + str(marks) + " of 5 correct question!")
print("Your marks was " + str((marks * 100)/5) + "%")
print(" 🙏🙏 thanks for your participation!!")