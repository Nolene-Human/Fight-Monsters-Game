
# Goal: Learn python by creating a simple text based game that is played in the terminal. The code needs to be clean and easy to read.
# LIST and RANDOM: Make the game more interesting by adding a list of monsters and randomly selecting one to be the monster in the game. Complexity in player choices and outcomes.
# FUNCTIONS: run_dice is called multiple time through out the game to simulate a dice roll. The function  will add 3 lines of code everytime it is needed.
# WHILE LOOP: The game will be played in a while loop that will continue until the player has defeated the monster based on points
# DICTIONARY: Added weapons to the monster using dicationary

import random

player={}
TotalScore = 0
FightScore = 0

monsters={
    "Dracula": "Wooden Stake",
    "Frankenstein's Monster": "Fire",
    "The Mummy": "Unraveling",
    "The Wolfman": "Silver Bullet",
    "The Invisible Man": "Paint",
    "The Creature from the Black Lagoon": "Harpoon",
    "The Phantom of the Opera": "Exposure",
    "The Headless Horseman":"Return its head",
    "Count Orlok (Nosferatu)": "Sunlight",
    "Jekyll and Hyde": "Antidote"
}

def start(name):
    player[name]=0
    print("Welcome ", name, "to your training, there are multiple vilians to fight. With every roll of the dice between 1 and 5 you will loose 2points. You need a total of 10 points to defeat the monster. Good luck! ")
    path="one"
    
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

   
def monster_fight():
    rooms = len(monsters)
    monster=random.choice(list(monsters.keys()))
    for w in monsters:
        if w == monster:
            fight=(monsters[w])
    print("Welcome there are ",rooms," to go through. You are trapped with monster ", monster ,". To win uou will need to ", fight, " to win") 
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
#for key in monsters:


monster_fight()



"""while len(monsters) > 0:
    monster_fight()
    print(monsters)
    

    print("There are ", len(monsters), "monsters left to fight")
    
    input("Press enter if you are ready to fight the next monster: ")

    if len(monsters) == 0:
        print("You have defeated all the monsters, you are the winner!")
        break"""
    
