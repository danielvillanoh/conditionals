# author: Daniel Villano-Herrera
# date: 7/23/2021

# --------------- # Section 2 # --------------- #
# ---------- # Part 1 # ---------- #

print('----- Section 2 -----'.center(25))
print('--- Part 1 ---'.center(25))

# 2 - Palindrome
print('\n' + 'Task 1' + '\n')
#
# Background: A palindrome is a word that is the same if read forwards and backwards. Examples of palindromes include:
#   - mom
#   - dad
#   - radar
#   - deified
#
# Instructions
#   a. Prompt input from the user in the form of a word.
#   b. Determine if the word is a palindrome.
#       a. If so, print that the word is a palindrome.
#       b. Otherwise, print that the word is not a palindrome.

word = input('Please enter a word: ')


# Creating a function called palindrome with words as parameter.

def palindrome(words):
    # Creating a variable called reserve which will take the parameter and reserve it.
    reverse = words[::-1]

    # If the parameter and reserve are the same, then we print out that they are the same, not if otherwise.
    if words == reverse:
        print('The word is a palindrome.')
    else:
        print('The word is not a palindrome')


palindrome(word)
# 2 - for Loop Patterns
print('\n' + 'Task 2' + '\n')
#
#
# Instructions
#   a. Create at least two of the following patterns using for loops and conditionals. One has been done for you as an
#       example. You still have to do two more. You are free to choose which ones you do.
#   b. Use the symbol specified by the user.

# $$$$$ | i = 0
# $     | i = 1
# $     | i = 2
# $$$$$ | i = 3
# $     | i = 4
# $     | i = 5
# $$$$$ | i = 6

# When i is evenly divisible by 3 --> 5 symbols. Otherwise, 1 symbol.

s = input('>> symbol | ')

for i in range(7):
    if i % 3 == 0:
        print(s * 5)
    else:
        print(s)

print()

# ****  | i = 0
# *   * | i = 1
# *   * | i = 2
# *   * | i = 3
# *   * | i = 4
# *   * | i = 5
# ****  | i = 6
d = input('Enter a symbol: ')

for i in range(7):
    if i % 6 == 0:
        print(d * 4)
    else:
        print(d + ' ' * 3 + d)
print()
# &     | i = 0
# &     | i = 1
# &     | i = 2
# &     | i = 3
# &     | i = 4
# &&&&& | i = 5
el = input('Enter a symbol: ')

for i in range(6):
    if i == 5:
        print(el * 5)
    else:
        print(el)
print()
# @   @ | i = 0
# @   @ | i = 1
#  @ @  | i = 2
#   @   | i = 3
#  @ @  | i = 4
# @   @ | i = 5
# @   @ | i = 6


# -------
#      -
#     -
#    -
#   -
#  -
# -------
