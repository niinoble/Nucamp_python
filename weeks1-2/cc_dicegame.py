import random

high_score = 0

current_score=0

def dice_game():
    dice_1=random.randint(1,6)
    dice_2=random.randint(1,6)
    print("You rolled a ...",dice_1)
    print("You rolled a ...",dice_2 ,"\n")
    global current_score
    current_score = dice_1 + dice_2
    return current_score
    
def check_score(score):
    global high_score
    if score > high_score:
          high_score = score
          print("New high score! \n")
          return high_score
    else:
        return high_score



print('Current High Score:',high_score)
while True:
    print("1) Roll Dice")
    print("2) Leave Game")
    choice = input('Enter your choice:')
    print("\n")
    if choice== "1":
        print("You have rolled a total  of:",dice_game(), "\n")
        print("Current High Score" ,check_score(current_score))
       
    else:
        print("Goodbye!")
        break