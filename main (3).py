# Define the Player class# define the player class
class player:
    def play(self):
        print("the player is playing cricket")

# define the batsman class that inherits from player
class batsman(player):
    def play(self):
        print("the batsman is batting")

# define the bowler class that inherits from player
class bowler(player):
    def play(self):
        print("the bowler is bowling")

# create objects of the batsman and bowler classes
batsman = batsman()
bowler = bowler()

# call the play() method for each object
batsman.play()
bowler.play()