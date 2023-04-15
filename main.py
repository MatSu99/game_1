
# Functions

#  @ int A, int B
# 1 = ROC, 2 = PAPER, 3 = SCISSORS, 4 = SHOTGUN
# Function evaluates which option wins
# > int
# 0 = DRAW, 1 = P1 wins, 2 = P2 WINS, 3 = ERROR
def evaluate_players_choices(A, B):

    if A == 1:
        if B == 1:
            return 0
        elif B == 2:
            return 2
        elif B == 3:
            return 1
        else:
            return 2
    elif A == 2:
        if B == 1:
            return 1
        elif B == 2:
            return 0
        elif B == 3:
            return 2
        else:
            return 2
    elif A == 3:
        if B == 1:
            return 2
        elif B == 2:
            return 1
        elif B == 3:
            return 0
        else:
            return 2
    else:
        if B == 4:
            return 0
        else:
            return 1

    return 3

# @ string A, string B
# converts user input to integers associated with game objects
# > No output
# ! Modifies entered variables STRING to INT
def proccess_users_input(A, B):
    if A == "1" or A == "r" or A == "rock":
        A = 1
    elif A == "2" or A == "p" or A == "paper":
        A = 2
    elif A == "3" or A == "s" or A == "scissors":
        A = 3
    elif A == "4" or A == "g" or A == "shotgun":
        A = 4
    else:
        A = 5

    if B == "1" or B == "r" or B == "rock":
        B = 1
    elif B == "2" or B == "p" or B == "paper":
        B = 2
    elif B == "3" or B == "s" or B == "scissors":
        B = 3
    elif B == "4" or B == "g" or B == "shotgun":
        B = 4
    else:
        B = 5

# @ int A, int B
# converts user input to integers associated with game objects
# > int result
# 0 = no ammo used, 1 = player one wins, 2 = player two wins
# 3 = both users shot (DRAW), 4 = users are ouf of ammo (DRAW)
def check_ammo(A, B):
    player_one_status = 1
    player_two_status = 1
    if A != 4 and B != 4:
        return 0
    else:
        if A == 4:
            if __p1_shells__ > 0:
                __p1_shells__-= 1
            else:
                player_one_status = 0

        if B == 4:
            if __p1_shells__ > 0:
                __p1_shells__-= 1
            else:
                player_two_status = 0

        if player_one_status == 1 and player_two_status == 1:
            return 3
        elif player_one_status == 0 and player_two_status == 0:
            return 4
        elif player_one_status > player_two_status:
            return 1
        else:
            return 2
    return 5
        


print("START")

# Input variables
WELCOME_MESSAGE = "Rock\nPaper\nScissors\nSHOTGUN"
player_one_input = None
player_two_input = None
__p1_shells__ = 3
__p2_shells__ = 3

print("Player one! Enter you choice!")
player_one_input = input(">")

print("Player two! Enter you choice!")
player_two_input = input(">")

proccess_users_input(player_one_input, player_two_input)
check_ammo(player_one_input, player_two_input)

print(f"{player_one_input} VS {player_two_input}")
