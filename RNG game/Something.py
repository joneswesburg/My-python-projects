from functions import error
from functions import your_aura
from functions import print_auras


print_auras()
your_aura()


while True:
    x = input("Do you want to play again? ").lower()
    if x == "yes":
        your_aura()
    elif x == "no":
        print("Game Ended")
        break
    else:
        error()
