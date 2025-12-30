while True :
    games = ["Soccer", "Tic Tac Toe", "Snake", "Puzzle", "Rally"]
    choice = int(input("Choose a game (0-4) or (-1) to quit :"))
    if choice == -1 :
      print("Game ended")
      break
    elif choice < 0 or choice > 4 :
       print("Invalid number")
    else :
       print(games[choice])