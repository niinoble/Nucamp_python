import random

diamonds = ["AD","2D","3D","4D","5D", "6D",
            "7D", "8D", "9D","10D", "JD","QD", "KD"]
hands = []

while diamonds:

    hand = input("Enter to pick a card or Press Q and Enter to quit: ")
    if hand.lower() == "q":
      break
    elif hand == "":
        hand = random.choice(diamonds)
        diamonds.remove(hand)
        hands.append(hand)
       
        print("Your hand:",hands)
        print("Remaining cards:", diamonds)
    else: 
        print("Please press Q and Enter to quit or Just Enter to pick card")

    if not diamonds:
        print("There are no more cards to pick")