
# Goal: Learn python by creating a simple text based game that is played in the terminal. The code needs to be clean and easy to read.
# LIST and RANDOM: Make the game more interesting by adding a list of monsters and randomly selecting one to be the monster in the game. Complexity in player choices and outcomes.
# FUNCTIONS: run_dice is called multiple time through out the game to simulate a dice roll. The function  will add 3 lines of code everytime it is needed.
# WHILE LOOP: The game will be played in a while loop that will continue until the player has defeated the monster based on points

import random

player=[]
TotalScore = 0
FightScore = 0

monsters=[
    "Dracula",
    "Frankenstein's Monster",
    "The Mummy",
    "The Wolfman",
    "The Invisible Man",
    "The Creature from the Black Lagoon",
    "The Phantom of the Opera",
    "The Headless Horseman",
    "Count Orlok (Nosferatu)",
    "Jekyll and Hyde"
]

weapons = [
    "Wooden Stake for Dracula",
    "Fire for Frankenstein's Monster",
    "Unraveling or Fire for The Mummy",
    "Silver Bullet for The Wolfman",
    "Paint or Dust for The Invisible Man",
    "Harpoon or Net for The Creature from the Black Lagoon",
    "Exposure or Confrontation for The Phantom of the Opera",
    "Decapitation for The Headless Horseman",
    "Sunlight or Wooden Stake for Count Orlok (Nosferatu)",
    "Antidote or Restraint for Jekyll and Hyde"
]



def run_dice():
    dice = random.randint(1, 6)
    input("Press enter to roll the dice: ")
    print("you rolled", dice)
    return dice

def score():
    score=0
    score += 1
    print(score)
    #return score

def hit():
    hit= score()
    hit -= 2
    print(hit)
    return hit

def start():
    start=input("Type in player name:  ")
    player.append(start)
    print("Welcome ", player[0], "to your training, there are multiple vilians to fight. With every roll of the dice between 1 and 5 you will loose 2points. You need a total of 10 points to defeat the monster. Good luck! ")
    path="one"


   
def monster_fight():
    rooms = len(monsters)
    print(monsters)
    monster = random.choice(monsters)
    print("Welcome there are ",rooms," to go through. You are trapped with monster ", monster ,"roll the dice to start.") 
    FightScore = 0
   
    while FightScore < 10:        
        dice=int(run_dice())
        if dice < 6:
            FightScore+=dice
            print("Your score is: ", FightScore)
        
        if dice == 6:
            FightScore-=3
            print("You were hit and lost 2 points!")
            print("Your score is: ", FightScore)

    if FightScore >= 10:
        rooms -= 1
        print("Congratulation you have killed ", monster)
        monsters.remove(monster)


    if FightScore <= 0:
        print("O that is bad luck, you have been killed by ", monster)
        print("R.I.P")
       

    return FightScore


"""while len(monsters) > 0:
    monster_fight()
    print(monsters)
    

    print("There are ", len(monsters), "monsters left to fight")
    
    input("Press enter if you are ready to fight the next monster: ")

    if len(monsters) == 0:
        print("You have defeated all the monsters, you are the winner!")
        break"""
    
