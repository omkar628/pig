import random

def roll():
    min_value=1
    max_value=6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    player =input("Enter the number of player you wanted to play (2-6)")
    print(f"The number of players playing game are {player}")
    if player.isdigit():
        player=int(player)
        if 2<= player <=6:
            print("you are good to go  ")
            print("Lets start the game")
            break
        else:
            print("enter between 2 to 6")
    else:
        print("envalid try again")
print(player)

max_score=50
player_score= [0 for _ in range(player)]


while max(player_score)<max_score:
    for player_idx in range(player):
        print("\nPlayer number",player_idx+1, "has started\n")
        current_score=0


        while True:
            should_roll=input("Wouuld you  like to roll(y)")
            if should_roll!="y":
                break

            value=roll()
            if value==1:
                print("you have rolled one")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a :",value)

            print("your score is ",current_score)
        player_score[player_idx]+=current_score
        print("Your total score is:",player_score[player_idx])
        
highest_score=max(player_score)
winning_idx=player_score.index(highest_score)
print("player score:",highest_score,"winning player is :",winning_idx+1)



