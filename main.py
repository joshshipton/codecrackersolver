import sys
import random as rd

sys.path.append(r'c:\users\shipt\appdata\roaming\python\python38\site-packages')
from english_words import english_words_lower_alpha_set as words

code = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: 'l', 8: '', 9: 'p', 10: '', 11: '', 12: '', 13: '', 14: '', 15: '',
        16: '', 17: '', 18: '', 19: '', 20: '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: ''}

used_letters = ['l', 'p']
unused_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z']

# i have two words now need to see possible solutions for both words
word1 = [1, 10, 8, 16, 4]
word2 = [1, 2, 2]
word3 = [2, 7, 13, 17, 2, 1, 3, 16]
word4 = [8, 14, 13, 12]
word5 = [3, 4, 5]
word6 = [18, 1, 4, 16]

# if i add word5 and word6 the whole thing breaks but no fucking clue why
board = [word1] + [word2] + [word3] + [word4]

print(board)

# changes the numbers of known words on the board into letters
#  most popular

# words that have already been tried
tried = []

counted = []
counting_list = []
# word we have not yet solved


# fill in the board with known letters
# how the fuck did i fuck this up so fucking badly just by adding two words to the board?!?!?

# board is not filling correctly wil have to correct this
# letters that are filled need to be removed from unused letters
# need a way to put that back into unsed letters if they are not used

def fillboard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            # if string in board pass
            if type(board[i][j]) == str:
                    pass
            else:
            # get the value of the key and update the board
                item = code.get(board[i][j])
                if item != '':
                    board[i][j] = item
    print(board)
    return board

fillboard(board)
current = 0
print(board)




# need to replace every instance of the most common letter with another letter
# repeat until entire first word is full and a valid word
c = 0
cycle = 0
cycle2 = 0
check = ''
# 0 for the letter with the most counts
# 1 for the second occurance of the tuple, which will be the value tied to the count
i = 0
run = True
# copy so i can reference the real b0 as we destroy it

while run:
    board_copy = board[0].copy()
    check = ''

    for i in range(len(board[0])):
        if type(board[0][i]) == int:
            board_copy[:] = [x if x != board_copy[i] else unused_letters[cycle] for x in board_copy]
            # rand int is not gonna work long term.... but its a solution for now
            cycle = rd.randint(0, len(unused_letters)-1)

    # if board[0] has no numbers
    # check if its a word
        if all(isinstance(item, str) for item in board_copy):
            check = check.join(board_copy)
            print('h')
            print(board_copy)
            if check in words and check not in tried:
                tried.append(check)
                print(check + "  yay!")
                run = False
                break


# update the code-dict

    # get the index of the board[0] numbers and the value of the numbers
    # the value of the numbers is the key the letter they are now is the value
# updates the dict with known values



for item in board[0]:
    if type(item) == int:
        find = board[0].index(item)
        code[item] = board_copy[find]

print(code)
fillboard(board)
print(board)

# fill all known words with known knowledge
    # if any of them are complete check if they are words
    # if they arent
    # fill in the next one with a valid word and then check again







# get word with the least amount of intergers and try that word

