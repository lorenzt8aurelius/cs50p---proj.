def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if difficulty == "Casual":
             recommend("Poker")
        else:
            recommend("Klondite")
    else:
        if players == "Multiplayer":
        if players == "Single-player":
    

def recommend(game):
    print("You might like", game)