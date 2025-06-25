def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if difficulty == "Multiplayer":
          recommend("Poker")
        elif difficulty == "Single-player":
            recommend("Klondite")
        else:
            print("Enter a valid number difficulty")
            
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Enter a valid player")
            
    

def recommend(game):
    print("You might like", game)