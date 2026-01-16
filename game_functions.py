

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    mid = len(poss_values)//2
    x = poss_values[mid]  
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if (current_val < next_val) and user_input == 'h':
        return True
    elif(current_val > next_val) and user_input =='l':
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    temp = []
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter
            temp.append(i)
    if len(temp) == 0:
        print(f"Sorry, {letter} is not in the word")
        return False
    if len(temp) > 0:
        print(f"Well done! {letter} is in the word")
        return True
       
