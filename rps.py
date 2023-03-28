# rock python scissors
# Two dictionaries used to store possible choices and game results
import random
import sys

states = {'r':'Rock', 'p':'Python', 's':'Scissors'}
results = {'User':0, 'AI':0, 'Draws':0}

def welcome():
  print("\nWelcome to ... \n\tROCK-PYTHON-SCISSORS\n")

def get_user_choice(states):
  selection = ""
  while selection not in states.keys():
    selection = input("Choose your move! (r, p, s): ")
  return selection

def get_computer_choice(states):
  return random.choice(list(states.keys()))

def get_winner(round, u, c, states, results):
  print(f"User: {states[u]} \t vs\t AI: {states[c]}")
  if u == c:
    results['Draws'] += 1 # same move
  elif u == 'r':
    if c == 'p':
      results['AI'] += 1 # rock loses to python
    else: # c must be s
      results['User'] += 1 # rock beats scissors
  elif u == 'p':
    if c == 'r':
      results['User'] += 1 # python beats rock
    else: # c must be s
      results['AI'] += 1  # python loses to scissors
  else: # u must be s
    if c == 'p':
      results['User'] += 1 # scissors beats python
    else:
      results['AI'] += 1 # scissors loses to rock

def check_wins(results):
  #print(results)
  for k, v in results.items():
    #print(f"Checking {k} {v}...")
    if v == 2:
      #print(f"{k}")
      return k
  return None

def display_winner(player, results):
  if player == 'Draws':
    print("It was a draw!")
  elif results['AI'] == 1 and results['User'] == 1 and results['Draws'] == 1: # all end on 1
    print("It was a draw")
  else:
    print(f"Well done {player} with {results[player]}/3 !!!")

def display_final_results(results):
  for k, v in results.items():
    print(f"{k}:\t\t{v}")

def goodbye():
  print("Thank you for playing ROCK-PYTHON-SCISSORS.\nGoodbye.")
  #exit()

def main():
  welcome()
  for i in range(1,4):
    print(results)
    print(f"Round {i}:")
    computer_choice = get_computer_choice(states)
    user_choice = get_user_choice(states)
    get_winner(i,user_choice, computer_choice, states, results)
    winner = check_wins(results)
    if winner:
      display_winner(winner, results)
      break
  display_final_results(results)
  goodbye()

main()