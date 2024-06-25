import random
user_action=input("enter a choice(rock,paper,scissors):")
possible_actions=['rock','paper','scissors']
if user_action not in possible_actions:
  print("please provide valid response from['rock','paper','scissors']")
else:
  computer_action=random.choice(possible_actions)
  print(f"\nyou choose{user_action},computer choose{computer_action}.\n")
  if user_action==computer_action:
    print(f"both players selected{user_action}.it is a tie")
  elif user_action=="rock":
    if computer_action=="scissors":
      print("rock smashes scissors! you win!")
    else:
      print("paper covers rock! you lose.")
  elif user_action=="paper":
    if computer_action=="rock":
      print("paper covers rock! you win!")
    else:
        print("scissors cut paper! you lose")
  elif user_action=="scissors":
    if computer_action=="paper":
        print("scissors cut paper! you win!")
    else:
        print("rock smashes scissors! tou lose!")
