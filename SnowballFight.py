
''' 
    Name: Snowball-Mania
    Author: Landon Strutz
    Date: 
    Class: AP Computer Science Principles
    Python: 
'''

  import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    print(Fore.GREEN + 'Welcome to Snowball Mania!')
    time.sleep(1)
    name = input(Fore.YELLOW + "What is your name? ")
    opponent = input(Fore.YELLOW + "Who do you want to fight? ")
    print(Fore.GREEN + name + " vs. " + opponent)
    time.sleep(1)

    players = []
    players.append(name)
    players.append(opponent)

    nextPlayer = ""
    while nextPlayer != "DONE":
        nextPlayer = input(Fore.YELLOW + "Are there any more opponents? If so, type them one at a time or type DONE: ")
        if nextPlayer != "DONE":
            players.append(nextPlayer)

    choice = input(Fore.YELLOW + "Do you want to choose who to throw the snowball at? (yes or no): ")
    gameplay(name, players, choice)

def gameplay(name, players, manual):
    while len(players) > 1:
        thrower = random.choice(players)
        
        if manual.lower() == "yes" and thrower == name:
            print(Fore.BLUE + f"It's your turn to throw the snowball!")
            target = input(Fore.YELLOW + f"Choose your target ({', '.join(p for p in players if p != name)}): ")
            if target in players and target != name:
                print(Fore.GREEN + f"{name} hits {target} with a snowball!")
                players.remove(target)
            else:
                print(Fore.RED + "Invalid target! You missed your turn.")
        else:
            target = random.choice([p for p in players if p != thrower])
            print(Fore.CYAN + f"{thrower} throws a snowball at {target}!")
            players.remove(target)
        
        print(Fore.MAGENTA + f"Remaining players: {', '.join(players)}")
        time.sleep(1)
    
    print(Fore.GREEN + f"The winner is {players[0]}!")

if __name__ == "__main__":
    main()




