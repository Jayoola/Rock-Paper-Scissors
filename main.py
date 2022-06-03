import random
while True:

  possible_actions = ["R", "P", "S"]
  computer_action = random.choice(possible_actions)
  user_action = input("Enter a choice('R' for rock, 'P' for paper, 'S' for scissors): ")
  while user_action not in possible_actions:
      print("Please input a valid option")
      user_action = input("Enter a choice('R' for rock, 'P' for paper, 'S' for scissors): ")
  if user_action == computer_action:
      print("computer: ",computer_action)
      print("player: ",user_action)
      print("It's a tie!")
  elif user_action == "R":
      if computer_action == "P":
          print("computer: ",computer_action)
          print("player: ",user_action)
          print("You lose!")
      if computer_action == "S":
          print("computer: ",computer_action)
          print("player: ",user_action)
          print("You win!")
  elif user_action == "P":
      if computer_action == "R":
          print("computer: ",computer_action)
          print("player: ",user_action)
          print("You win!")
      if computer_action == "S":
          print("computer: ",computer_action)
          print("player: ",user_action)
          print("You lose!")
  elif user_action == "S":
      if computer_action == "P":
          print("computer: ",computer_action)
          print("player: ",user_action)
          print("You win!")
      if computer_action == "R":
          print("computer: ",computer_action)
          print("player: ",user_action)
          print("You lose!")
 
  play_again = input("Play again? (yes/no): ").lower()

  if play_again != "yes":
    break

print("Bye!")




    
    
        


    

