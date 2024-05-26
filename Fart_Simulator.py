#---------------------------------------------------------------------------------------
# PACKAGES

import os
import random
import pygame
import pickle
from time import sleep

#---------------------------------------------------------------------------------------
# CLASSES

class Format:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    YELLOW = '\033[33m'

format = Format()

#---------------------------------------------------------------------------------------
# DICTIONARIES

# Score and stats for the current player. Only players who leave the table will be
# eligible for entry to the High Score table AND the Current Session scoreboard
dict_current_player = {
    'Name': '',                 # Current players name
    'Score': 0,                 # Calculated by total seconds of all farts length
    'Farts': 0,                 # Total number of safe farts
    'Avg Fart Length': 0,       # Farts / Score(total time of all farts length)
    'name_len': 0               # Total characters in players name
}

# Highest score for a player who has successfuly farted AND left the table during
# the current played session of the game
dict_session_player = {
    'Name': '-',                # Current playing session players name
    'Score': 0,                 # Calculated by total seconds of all farts length
    'Farts': 0,                 # Total number of safe farts
}

dict_high_scores = {
    'HS_Rank': list(range(1,11)),
    'HS_Name': ['Jack', 'Mack', 'Zack', 'Max', 'Jax', 'Lex', 'Alex', 'Marlene', 'Charlene', 'Darlene'],
    'HS_Score': [50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
    'HS_Farts': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    'HS_Avg Fart Length': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
}

#---------------------------------------------------------------------------------------
# BOWEL FUNCTIONS

cwd = os.getcwd()

fart_dir = cwd + r'/GameFiles/Fart Sounds/'
poop_dir = cwd + r'/GameFiles/Pooped Pants/'

#---------------------------------------------------------------------------------------
# CLEAR SCREEN FUNCTION

def cls():
    os.system("cls" if os.name == "nt" else "clear")

#---------------------------------------------------------------------------------------
# POO CHANCE RANDOM NUMBER FUNCTION

def rand_num():
    global fart_length
    global poo_chance
    fart_length = random.randint(1, 10)
    poo_chance = random.randint(1, 10)

#---------------------------------------------------------------------------------------
# GAME BEGIN

def main():
    game_intro()
    main_menu()

def game_intro():
    cls()
    print(format.OKGREEN + '\n' * 3,'        StinkyBumBum Productions Present' + format.ENDC)
    sleep(2)
    cls()
    sleep(1)
    print(format.OKGREEN + '\n' * 3,'          A game by Matt Green' + format.ENDC)
    sleep(2)
    cls()
    sleep(1)
    print(format.OKBLUE + '\n' * 3,'             PULL MY FINGER' + format.ENDC)
    sleep(2)
    print(format.OKBLUE + '\n       THE ULTIMATE FART EXPERIENCE' + format.ENDC)
    sleep(2)
    print(format.OKGREEN + '\n' * 3,'       for Oliver, Liam & Emelia' + format.ENDC)
    sleep(3)
    cls()
    sleep(2)
    print(format.YELLOW + 'So, here\'s the story....\n' * 1 + format.ENDC)
    sleep(2)
    print('\nYou are at your family dinner and you')
    print('have just had a succulent Chinese meal.\n' * 1)
    sleep(3)
    print('Your stomach starts to rumble and you')
    print('let out a ripper of a fart.\n' * 1)
    sleep(3)
    print('One of your young family members laughs')
    print('hysterically and begs you to do another.\n' * 1)
    sleep(3)
    print('You agree....\n' * 1)
    sleep(3)
    print('             ....on one condition\n\n' * 1)
    sleep(3)
    input(format.YELLOW + '     Hit ENTER to begin\n' * 1 + format.ENDC)
    pre_load()

#---------------------------------------------------------------------------------------
# SET UP INITIAL HIGH SCORE TABLE

def pre_load():
    # Define the filename for the save game file
    fart_sim_savefile = 'fart_sim_save.pickle'
    
    # Check if the save game file exists
    def pre_load_hs_table():
        pre_loaded_data = None  # Initialize pre_loaded_data

        if os.path.exists(fart_sim_savefile):
            # If the file exists, load the data from it
            with open(fart_sim_savefile, 'rb') as file:
                pre_loaded_data = pickle.load(file)
        else:
            # If the file doesn't exist, create and save it
            with open(fart_sim_savefile, 'wb') as file:
                pickle.dump(dict_high_scores, file)
                pre_loaded_data = dict_high_scores

        return pre_loaded_data  # Return the loaded or created data

    # Get the pre-loaded data from the function
    pre_loaded_data = pre_load_hs_table()

    # Update dict_high_scores with the loaded or created data
    dict_high_scores.update(pre_loaded_data)

    main_menu()

#---------------------------------------------------------------------------------------
# MAIN MENU

def main_menu():
    cls()
    print(format.BOLD + format.OKBLUE + '\t       PULL MY FINGER\n' + format.ENDC)
    print(format.BOLD + format.OKBLUE + '\tThe Ultimate Fart Experience\n' + format.ENDC) 
    print(format.OKGREEN + '     A game where if you poo, you lose\n\n'+ format.ENDC)
    print(format.YELLOW + ' Please select from the following options;\n'+ format.ENDC)
    print(format.YELLOW + ' [1] ' + format.ENDC + 'Start a New Game'+ format.ENDC)
    print(format.YELLOW + ' [2] ' + format.ENDC + 'How to Play'+ format.ENDC)
    print(format.YELLOW + ' [3] ' + format.ENDC + 'High Scores'+ format.ENDC)
    print(format.YELLOW + ' [4] ' + format.ENDC + 'Exit Game\n'+ format.ENDC)
    option = input(" Choose: ")
    if option == "1":
        start_game()
    elif option == "2":
        how_to_play()
    elif option == "3":
        high_scores()
    elif option == "4":
        game_exit()
    else:
        print('\n Invalid option, try again')
        sleep(1)
        main_menu()

#---------------------------------------------------------------------------------------
# SUB MAIN MENUS

def how_to_play():
    cls()
    print(format.RED + '             ***** HOW TO PLAY *****\n'+ format.ENDC)
    print(' 1 - Have your finger pulled to rip farts')
    print(' 2 - The longer the fart, the more points you earn')
    print(' 3 - The more points you earn, the higher your score\n')
    print(' Simple, right?\n')
    print(' Just make sure you know when to stop.\n')
    print(' Because if you fart too much, you might poop your pants.')
    print(' And if you poop your pants, it\'s game over and you will')
    print(' lose all of your points.\n\n')
    input(format.YELLOW + ' Hit ENTER to return to the Main Menu' + format.ENDC)
    main_menu()

def high_scores():
    cls()
    print(format.RED + '             ****** FARTING HEROES ******\n'+ format.ENDC)
    print(format.YELLOW + '             Top 10 All Time Best Farters\n' + format.ENDC)
    print(' Rank\t','Name           ','Score\t','Farts\t','Avg Fart Length\n')
    print('  1\t',dict_high_scores['HS_Name'][0],(' '*(15-len(dict_high_scores['HS_Name'][0]))),dict_high_scores['HS_Score'][0],'\t ',dict_high_scores['HS_Farts'][0],'\t ',dict_high_scores['HS_Avg Fart Length'][0])
    print('  2\t',dict_high_scores['HS_Name'][1],(' '*(15-len(dict_high_scores['HS_Name'][1]))),dict_high_scores['HS_Score'][1],'\t ',dict_high_scores['HS_Farts'][1],'\t ',dict_high_scores['HS_Avg Fart Length'][1])
    print('  3\t',dict_high_scores['HS_Name'][2],(' '*(15-len(dict_high_scores['HS_Name'][2]))),dict_high_scores['HS_Score'][2],'\t ',dict_high_scores['HS_Farts'][2],'\t ',dict_high_scores['HS_Avg Fart Length'][2])
    print('  4\t',dict_high_scores['HS_Name'][3],(' '*(15-len(dict_high_scores['HS_Name'][3]))),dict_high_scores['HS_Score'][3],'\t ',dict_high_scores['HS_Farts'][3],'\t ',dict_high_scores['HS_Avg Fart Length'][3])
    print('  5\t',dict_high_scores['HS_Name'][4],(' '*(15-len(dict_high_scores['HS_Name'][4]))),dict_high_scores['HS_Score'][4],'\t ',dict_high_scores['HS_Farts'][4],'\t ',dict_high_scores['HS_Avg Fart Length'][4])
    print('  6\t',dict_high_scores['HS_Name'][5],(' '*(15-len(dict_high_scores['HS_Name'][5]))),dict_high_scores['HS_Score'][5],'\t ',dict_high_scores['HS_Farts'][5],'\t ',dict_high_scores['HS_Avg Fart Length'][5])
    print('  7\t',dict_high_scores['HS_Name'][6],(' '*(15-len(dict_high_scores['HS_Name'][6]))),dict_high_scores['HS_Score'][6],'\t ',dict_high_scores['HS_Farts'][6],'\t ',dict_high_scores['HS_Avg Fart Length'][6])
    print('  8\t',dict_high_scores['HS_Name'][7],(' '*(15-len(dict_high_scores['HS_Name'][7]))),dict_high_scores['HS_Score'][7],'\t ',dict_high_scores['HS_Farts'][7],'\t ',dict_high_scores['HS_Avg Fart Length'][7])
    print('  9\t',dict_high_scores['HS_Name'][8],(' '*(15-len(dict_high_scores['HS_Name'][8]))),dict_high_scores['HS_Score'][8],'\t ',dict_high_scores['HS_Farts'][8],'\t ',dict_high_scores['HS_Avg Fart Length'][8])
    print(' 10\t',dict_high_scores['HS_Name'][9],(' '*(15-len(dict_high_scores['HS_Name'][9]))),dict_high_scores['HS_Score'][9],'\t ',dict_high_scores['HS_Farts'][9],'\t ',dict_high_scores['HS_Avg Fart Length'][9],'\n\n')
    input(format.YELLOW + ' Hit ENTER to return to the Main Menu' + format.ENDC)
    main_menu()

def game_exit():
    cls()
    save_game_data('fart_sim_save.pickle')
    print(format.YELLOW + 'As a farting gift, here is a short limerick\n\n\n' + format.ENDC)
    sleep(3)
    print(format.OKGREEN + 'I dare say I was rather flustered')
    sleep(2)
    print('After shamefully cutting the mustard')
    sleep(2)
    print('To the toilet I booked')
    sleep(2)
    print('And fearfully looked')
    sleep(2)
    print('To find shorts that were full of brown custard!\n\n\n' + format.ENDC)
    sleep(4)
    print(format.YELLOW + 'Have a nice day :)\n' + format.ENDC)
    sleep(1)
    print(format.YELLOW + 'Goodbye' + format.ENDC)
    sleep(2)
    exit()

#---------------------------------------------------------------------------------------
# PLAYER DETAILS

def get_valid_player_name():
    name = input(" Enter Your Name: ")
    name_len = len(name)

    if name_len == 0 or name.isspace():
        print('\n Please enter a valid name')
        return get_valid_player_name()
    elif name_len > 15:
        print('\n Name must be 15 characters or less, enter a new name')
        return get_valid_player_name()
    else:
        return name

def new_player():
    dict_current_player['Name'] = get_valid_player_name()
    dict_current_player['name_len'] = len(dict_current_player['Name'])
    cls()
    start_game()

#---------------------------------------------------------------------------------------
# GAME PLAY FUNCTIONS

def play_game_player_con():
    # When player continues after pooping, name is retained and scores reset
    dict_current_player['Score'] = 0
    dict_current_player['Farts'] = 0
    dict_current_player['AVG Fart Length'] = 0
    start_game()

def start_game():
    while dict_current_player['Name'] == '':
        new_player()
        dict_current_player['name_len'] = len(dict_current_player['Name'])

    while True:
        print(format.OKGREEN + 'ALL-TIME HIGH SCORE' + format.ENDC)
        print('Player Name:\t ', dict_high_scores['HS_Name'][0])
        print('Player Score:\t ', dict_high_scores['HS_Score'][0])
        print('Player Name:\t ', dict_high_scores['HS_Farts'][0],'\n')
        print(format.OKGREEN + 'CURRENT SESSION HIGH SCORE' + format.ENDC)
        print('Player Name:\t ', dict_session_player['Name'])
        print('Player Score:\t ', dict_session_player['Score'])
        print('Successful Farts:', dict_session_player['Farts'],'\n')
        print((format.OKGREEN + 'PLAYER NAME:\t ' + format.ENDC), dict_current_player['Name'])
        print('Current Score:\t ', dict_current_player['Score'])
        print('Successful Farts:', dict_current_player['Farts'],'\n\n')
        print(format.YELLOW + 'What will you do?\n'+ format.ENDC)
        print(format.YELLOW + '[1] ' + format.ENDC + 'Have your finger pulled?')
        print(format.YELLOW + '[2] ' + format.ENDC + 'Leave the table\n')
        choice1 = input('Enter your choice: ')
        cls()

        if choice1 == "1":
            print('\nYou have your finger pulled')
            sleep(1)
            rand_num()
            if poo_chance == fart_length:
                lose_poo()
            else:
                win_fart()
        elif choice1 == "2":
            leave_table()
        else:
            print('\nInvalid option, try again')
            sleep(1)
            cls()

def win_fart():
    # Only add winning values to current players dictionary
    dict_current_player['Score'] += fart_length
    dict_current_player['Farts'] += 1
    dict_current_player['AVG Fart Length'] = round(dict_current_player['Score']/dict_current_player['Farts'],2)

    # Rip fart
    print(format.OKBLUE + '\nYOU RIP A FART!\n' + format.ENDC)
    sound_fart()
    if fart_length == 1:
        print('The fart lasted', fart_length, 'second')
        print('You earned', fart_length, 'point')
    elif fart_length > 1:
        print('The fart went for', fart_length, 'seconds')
        print('You earned', fart_length, 'points')
    input(format.YELLOW + '\nHit ENTER to continue' + format.ENDC)
    cls()

def lose_poo():
    print(format.RED + '\nUH OH! YOU JUST POOPED YOUR PANTS!' + format.ENDC)
    sound_pooped()
    print('\nYou were able to squeeze out', dict_current_player['Farts'], 'farts before disater struck')
    print('You lose:', dict_current_player['Score'], 'points\n')
    print(format.YELLOW + 'What will you do?\n'+ format.ENDC)
    print(format.YELLOW + '[1]'+ format.ENDC + ' Play again as the current player')
    print(format.YELLOW + '[2]'+ format.ENDC + ' Back to Main Menu')
    print(format.YELLOW + '[3]'+ format.ENDC + ' Exit Game\n')
    choice2 = input('Enter your choice: ')
    cls()
    if choice2 == "1":
        # Reset current player scores and stats to zero
        dict_current_player['Score'] = 0
        dict_current_player['Farts'] = 0
        dict_current_player['AVG Fart Length'] = 0
        play_game_player_con
    elif choice2 == "2":
        # Reset current player scores and stats to zero
        dict_current_player['Name'] = ''
        dict_current_player['Score'] = 0
        dict_current_player['Farts'] = 0
        dict_current_player['AVG Fart Length'] = 0
        main_menu()
    elif choice2 == "3":
        game_exit()
    else:
        print('\nInvalid option, try again')
        sleep(1)
        cls()
        lose_poo()

#---------------------------------------------------------------------------------------
# FART SOUNDS

def sound_fart():
    # PATH FOR PLAYING IN IDE TERMINAL
    # fart_dir = r'D:\Documents\My Documents\Personal\Coding\Python\Projects\Fart Simulator\GameFiles\Fart Sounds\\'
    
    # PATH FOR CREATING .EXE FILE
    # USING VARIABLE DEFINED AT TOP OF SCRIPT
    
    pygame.mixer.init()

    # Get a list of all the MP3 files in the directory
    fart_files = [file for file in os.listdir(fart_dir) if file.lower().endswith('.mp3')]

    selected_mp3 = random.choice(fart_files)
    selected_mp3_path = fart_dir + selected_mp3

    # Load and play the selected MP3 file
    pygame.mixer.music.load(selected_mp3_path)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    pygame.time.delay(1000)  # Adjust the delay as needed

    # Stop the audio playback
    pygame.mixer.music.stop()

#---------------------------------------------------------------------------------------
# POOPED PANTS

def sound_pooped():
    # PATH FOR PLAYING IN IDE TERMINAL
    # poop_dir = r'D:\Documents\My Documents\Personal\Coding\Python\Projects\Fart Simulator\GameFiles\Pooped Pants\\'
    
    # PATH FOR CREATING .EXE FILE
    # USING VARIABLE DEFINED AT TOP OF SCRIPT   
    #  
    poop_file = 'Pooped_Pants.mp3'
    pygame.mixer.init()

    # Check if the specified file exists
    mp3_path = poop_dir + poop_file
    if not os.path.isfile(mp3_path):
        print(f"'{poop_file}' not found in the specified directory.")
    else:
        # Load and play the specified MP3 file
        pygame.mixer.music.load(mp3_path)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

#---------------------------------------------------------------------------------------
# SAVE GAME DATA

def save_game_data(filename):
    with open(filename, 'wb') as handle:
        pickle.dump(dict_high_scores, handle, protocol=pickle.HIGHEST_PROTOCOL)

#---------------------------------------------------------------------------------------
# LEAVE TABLE - SAVE SCORES (IF APPLICABLE)

def leave_table():
    # Update Session Player scores IF the current players score exceeds 
    # the current played session score
    if dict_current_player['Score'] > dict_session_player['Score']:
        dict_session_player['Name'] = dict_current_player['Name']
        dict_session_player['Score'] = dict_current_player['Score']
        dict_session_player['Farts'] = dict_current_player['Farts']
    
    # Update High Score table IF the current players scores exceeds the
    # lowest score (rank 10) currently in the high score table
    new_score = dict_current_player['Score']

    # Check if the list is empty before accessing the last element
    if not dict_high_scores['HS_Score'] or new_score > dict_high_scores['HS_Score'][-1]:
        dict_current_player['Avg Fart Length'] = round(dict_current_player['Score'] / dict_current_player['Farts'],2)
        dict_high_scores['HS_Rank'].append(None)  # Placeholder for new rank
        dict_high_scores['HS_Name'].append(dict_current_player['Name'])
        dict_high_scores['HS_Score'].append(new_score)
        dict_high_scores['HS_Farts'].append(dict_current_player['Farts'])
        dict_high_scores['HS_Avg Fart Length'].append(dict_current_player['Avg Fart Length'])

    # Sort the high scores based on highest scores first
        sorted_data = sorted(zip(
            dict_high_scores['HS_Rank'],
            dict_high_scores['HS_Name'],
            dict_high_scores['HS_Score'],
            dict_high_scores['HS_Farts'],
            dict_high_scores['HS_Avg Fart Length']
        ), key=lambda x: x[2], reverse=True)

    # Update the values in the dictionary, ensuring lists are of the same length
        dict_high_scores['HS_Rank'], dict_high_scores['HS_Name'], dict_high_scores['HS_Score'], dict_high_scores['HS_Farts'], dict_high_scores['HS_Avg Fart Length'] = map(list, zip(*sorted_data))

    # Pad lists to ensure they have the same length
        list_length = len(dict_high_scores['HS_Score'])
        for key in dict_high_scores:
            while len(dict_high_scores[key]) < list_length:
                dict_high_scores[key].append(0)

        dict_high_scores['HS_Rank'] = list(range(1, list_length + 1))

    # Save the current game data
    filename = 'fart_sim_save.pickle'
    save_game_data(filename)

    print(format.OKGREEN + 'You have left the table.\n' + format.ENDC)
    print('After', dict_current_player['Farts'], 'farts, you have scored a respectable', dict_current_player['Score'], 'points\n')
    print(format.YELLOW + 'What will you do now?\n' + format.ENDC)
    print(format.YELLOW + '[1] ' + format.ENDC + 'Play Again as current player')
    print(format.YELLOW + '[2] ' + format.ENDC + 'Back to Main Menu')
    print(format.YELLOW + '[3] ' + format.ENDC + 'Exit Game\n')
    choice2 = input("Enter your choice: ")
    cls()

    # Reset the current players scores and stats
    dict_current_player['Score'] = 0
    dict_current_player['Farts'] = 0
    dict_current_player['AVG Fart Length'] = 0

    if choice2 == "1":
        start_game()
    elif choice2 == "2":
        dict_current_player['Name'] = ''
        main_menu()
    elif choice2 == "3":
        game_exit()
    else:
        leave_table()

# ---------------------------------------------------------------------------------------------------------------
# GAME LOADER

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------------------------