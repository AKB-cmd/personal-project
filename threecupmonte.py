from random import shuffle

# Function to shuffle the list
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

# Function to get the player's guess
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a position: 0, 1, or 2: ')
    return int(guess)

# Function to check the player's guess
def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(my_list)

# INITIAL LIST
my_list = ['', 'O', '']

# SHUFFLE LIST
shuffled_list = shuffle_list(my_list)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(shuffled_list, guess)
