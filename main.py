import sys
import random as rd
from english_words import english_words_lower_alpha_set as words

code = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: 'l', 8: '', 9: 'p', 10: '', 11: '', 12: '', 13: '', 14: '', 15: '',
        16: '', 17: '', 18: '', 19: '', 20: '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: ''}

used_letters = ['l', 'p']
unused_letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z']

word1 = [9, 7, 14, 13, 14]
word2 = [1, 5, 15, 14, 7]
word3 = [13, 20, 9]
word4 = [9, 15, 15, 9]

board = [word1] + [word2] + [word3] + [word4]
board_versions = [board]

# words that have already been tried
tried = []
cycle = rd.randint(0, len(unused_letters) - 1)
running = True
version = 0
index = 0

# fill in the board with known letters

def fill_board():
    global board
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
    board_versions.append(board)
    return board

# right now the board is updating so there are no ints in the board, need to revert the changes
def crackcode():
    global cycle
    global running
    global version
    global index

    while running:
        board_copy = board_versions[version][index].copy()

        for i in range(len(board[index])):
            if type(board[index][i]) == int:
                board_copy[:] = [x if x != board_copy[i] else unused_letters[cycle] for x in board_copy]
                cycle = rd.randint(0, len(unused_letters)-1)


            if all(isinstance(item, str) for item in board_copy):
                check = ''
                check = check.join(board_copy)
                if check in words and check not in tried:
                    tried.append(check)
                    print(check + "  yay!")
                    # updates the code dictionary
                    for item in board[index]:
                        if type(item) == int:
                            find = board[index].index(item)
                            code[item] = board_copy[find]
                            # dont know if i need unused letters, would sure make it a lot faster tho...
                            # is there a different way to not have duplicates?
                            #try:
                                #unused_letters.remove(board_copy[find])
                            #except ValueError:
                                #pass
                            #used_letters.append(board_copy[find])
                    # updates the code dictionary
                    running = False
                    break
                else:
                    pass


# fill all known words with known knowledge
# if any of them are complete check if they are words


def check_backtrack():
    global version
    version += 1
    for word in board:
        if all(isinstance(char, str) for char in word):
            check = ''
            check = check.join(word)
            # getting stuck here
            print("stuck")
            #if check in words and check not in tried:
                # this could break
                # eg, word a is wrong but the cipher word a creates causes word b to be correct
                # peep - bread possiblity eg.

                #tried.append(check)
            if check not in words:
                return True
                # backtrack to begining?
                # would 100% work but probs not most efficent

def solve():
    global version
    global index

    while True:
        fill_board()
        crackcode()
        fill_board()
        check_backtrack()

        # if cipher doesnt work go back a verison, same version as before
        if check_backtrack():
            version -= 1
            crackcode()
        # if cipher does work go up an index
        if not check_backtrack():
            index += 1
            crackcode()



solve()

# problem now is that if the code fucks up it cant change back and try again,
# as the board isnt numbers anymore its letters

# what if i somehow save every version of the board?
# or at least the last3 versions?
#
