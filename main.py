# Imports
import random
# Data

acceptable_input = ["1", "2", "3", "4", "r", "p", "s", "g",\
                     "rock", "paper", "scissors", "shotgun"]
names_objects = ["rock", "paper", "scissors", "shotgun"]

WELCOME_MESSAGE = "Rock\nPaper\nScissors\nSHOTGUN"
player_one_input = None
player_two_input = None
__p1_shells__ = 3
__p2_shells__ = 3
player_one_lives_counter = 0
player_two_lives_counter = 0
CPU_player_flag = 0

# Functions

def random_ouput():
    rand = random.randint(1,4)
    print(f"RESULT> {rand}")
    result = str(rand)
    return result

def set_players_live_counters(A, B):
    global player_one_lives_counter
    player_one_lives_counter = A
    global player_two_lives_counter
    player_two_lives_counter = B

def display_clash(A, B):
    p1_display = names_objects[A-1]
    p2_display = names_objects[B-1]
    print(f">>>{p1_display}<<< VS >>>{p2_display}<<<")

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
# > int result_1, result_2
def proccess_users_input(A, B):
    result_1 = None
    result_2 = None
    if A == "1" or A == "r" or A == "rock":
        result_1 = 1
    elif A == "2" or A == "p" or A == "paper":
        result_1 = 2
    elif A == "3" or A == "s" or A == "scissors":
        result_1 = 3
    elif A == "4" or A == "g" or A == "shotgun":
        result_1 = 4
    else:
        result_1 = 5

    if B == "1" or B == "r" or B == "rock":
        result_2 = 1
    elif B == "2" or B == "p" or B == "paper":
        result_2 = 2
    elif B == "3" or B == "s" or B == "scissors":
        result_2 = 3
    elif B == "4" or B == "g" or B == "shotgun":
        result_2 = 4
    else:
        result_2 = 5
    return result_1, result_2

def check_user_input(A):
    for x in acceptable_input:
        if A == x:
            return True
    return False

def game_player_vs_player():
    global player_one_lives_counter
    global player_two_lives_counter
    global CPU_player_flag
    # TODO: Add decsision setting live counters
    set_players_live_counters(3,3)
    rounds_counter = 1
    while player_one_lives_counter > 0 and player_two_lives_counter > 0:
        print(f"Round number: {rounds_counter}")
        print(f"PLAYER ONE: {player_one_lives_counter} HP")
        print(f"PLATER TWO: {player_two_lives_counter} HP")
        while True:
            print("Player one! Enter you choice!")
            player_one_input = input(">")
            if check_user_input(player_one_input) == True:
                break
            else:
                print("Incorrect input, valid options are:")
                print(acceptable_input)

        while True:
            if CPU_player_flag == 1:
                print("Computer input")
                player_two_input = random_ouput()
                break
            print("Player two! Enter you choice!")
            player_two_input = input(">")
            if check_user_input(player_two_input) == True:
                break
            else:
                print("Incorrect input, valid options are:")
                print(acceptable_input)

        player_one_choice, player_two_choice = proccess_users_input(player_one_input, player_two_input)
        display_clash(player_one_choice, player_two_choice)
        result_phase_1 = check_ammo(player_one_choice, player_two_choice)
        if result_phase_1 == 1:
            player_two_lives_counter -= 1
            print("ROUND ENDED\nWINNER: PLAYER ONE")
            rounds_counter += 1
            continue
        elif result_phase_1 == 2:
            player_one_lives_counter -= 1
            print("ROUND ENDED\nWINNER: PLAYER TWO")
            rounds_counter += 1
            continue
        elif result_phase_1 == 3:
            player_one_lives_counter -= 1
            player_two_lives_counter -= 1
            print("DRAW\nBOTH PLAYER LOSE 1 health point!")
            rounds_counter += 1
            continue
        elif result_phase_1 == 3:
            print("DRAW\n")
            rounds_counter += 1
            continue
        else:
            pass

        print("Phase 2 reached")
        result_phase_2 = evaluate_players_choices(player_one_choice, player_two_choice)
        print(f"Result_phase2: {result_phase_2}")
        if result_phase_2 == 1:
            player_two_lives_counter -= 1
            print("ROUND ENDED\nWINNER: PLAYER ONE")
            rounds_counter += 1
            continue
        elif result_phase_2 == 2:
            player_one_lives_counter -= 1
            print("ROUND ENDED\nWINNER: PLAYER TWO")
            rounds_counter += 1
            continue
        else:
            print("DRAW\n")
            rounds_counter += 1
            continue

    
    if player_one_lives_counter == 0 and player_two_lives_counter > 0:
        print("END OF THE GAME, THE WINNER IS:\nPLAYER TWO")
    elif player_two_lives_counter == 0 and player_one_lives_counter > 0:
        print("END OF THE GAME, THE WINNER IS:\nPLAYER ONE")
    elif player_one_lives_counter == 0 and player_two_lives_counter == 0:
        print("END OF THE GAME, DRAW")
    else:
        print("ERROR")



# @ int A, int B
# converts user input to integers associated with game objects
# > int result
# 0 = no ammo used, 1 = player one wins, 2 = player two wins
# 3 = both users shot (DRAW), 4 = users are ouf of ammo (DRAW)
def check_ammo(A, B):
    player_one_status = 0
    player_two_status = 0
    global __p1_shells__
    global __p2_shells__
    global player_one_lives_counter
    global player_two_lives_counter
    if A != 4 and B != 4:
        print("NO GUNS USED")
        return 0
    else:
        if A == 4:
            if __p1_shells__ > 0:
                __p1_shells__-= 1
                player_one_status = 1
            else:
                player_one_status = 0

        if B == 4:
            if __p2_shells__ > 0:
                __p2_shells__-= 1
                player_two_status = 1
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
    return 5 # Consider delete, not achivable now
        
# Main flow start
print("START")
print(WELCOME_MESSAGE)
CPU_player_flag = 1
game_player_vs_player()