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
word1 = [15, 9, 15, 15]
word2 = [15, 9, 15, 14]
word3 = [9, 7, 14, 13, 14]
word4 = [13, 20, 9]

board = [word3] + [word2] + [word1] + [word4]

tplcode = code.items()

# changes the numbers of known words on the board into letters
#  most popular

counted = []
counting_list = []
# word we have not yet solved


# fill in the board with known letters
for i in range(len(board)):
    for j in range(len(board) - 1):
        if board[i][j]:
            a = code.get(board[i][j])
            if a != '':
                board[i][j] = a

current = 0
print(board)
# counts the occurrences of letters in the first word

for item in board[current]:
    a = code.get(item)
    if a != '':
        pass
    if a == '' and item not in counted:
        counts = board[current].count(item)
        counted.append(item)
        counting_list.append(counts)

print(counted)
print(counting_list)

order = list(zip(counting_list, counted))
print(order)


# need to replace every instance of the most common letter with another letter
# repeat until entire first word is full and a valid word
c = 0
cycle = 0
cycle2 = 0
check = ''
# 0 for the letter with the most counts
# 1 for the second occurance of the tuple, which will be the value tied to the count
i = 0

# copy so i can reference the real b0 as we destroy it

while True:
    print(iter)
    iter = board[0].copy()
    check = ''

    for i in range(len(board[0])):
        if type(board[0][i]) == int:
            iter[:] = [x if x != iter[i] else unused_letters[cycle] for x in iter]
            cycle = rd.randint(0, len(unused_letters)-1)

    # if board[0] has no numbers
    # check if its a word
        if all(isinstance(item, str) for item in iter):
            check = check.join(iter)
            if check in words:
                print(check + "  yay!")
                quit()




# probably best to start with the most common word in the list
def find_empty():
    empty_value = {i for i in code if code[i] == ''}
    empty_value = list(empty_value)
    if len(empty_value) == 0:
        return None
    else:
        return empty_value[0]


# function from the suduko to find if a certain position is valid
def valid(board, value, pos):
    pass


# need to find all options for one word
# then try this code for another word
# if both word try another
# untill all words are done

def solve():
    find = find_empty()
    if not find:
        return True
    else:
        # need to figure out a wah
        word = find

    # need to fill with random letter instead of random number
    # also need to add a clause that the dict is not already solved
    for i in range(1, 26):
        if valid(code, i, word):
            word[word][word] = i

        if solve(words):
            return True

        words[word] = 0

    return False



# length = int(input("How many letters do you know? "))


# print("Enter the number-letter pairs you know")
# for i in range(length):
# known_letter = input(f"Enter the {i+1} letter you know: ").lower()
# known_number = int(input(f"what number does  '{known_letter}' correspond to:  "))
# code[known_number] = known_letter

# print(code)


# user enters known number - letters
# then enters different combinations of numbers
# program keeps going until it has cracked the code
# use a dictionary
# can just print the dictionary when done

# tries every combination
# if it words appends it to possible words
# returns list of possible words

# need to figure out how i can run thru all 26 letters of the alphabet for each int in the list
