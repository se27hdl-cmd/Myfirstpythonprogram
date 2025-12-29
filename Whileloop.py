while True :
    number = int(input("Choose a number between 1 and 10"))
    if number == 0 :
      print("End of game")
      break
    elif number < 1 or number > 10 : 
       print("Out of range")
    elif number == 5 :
       print("You chose 5")
    else:
       print("Valid number")
