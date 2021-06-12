import random


file = open('words.txt', 'r')
list = file.read().lower().split()
#print(list)

guess_list = []

selected_word = random.choice(list)
#print('selected word is: ', selected_word)

def guess_input():
    guess = input("Choose a letter").lower()
    if len(guess) != 1:
        print("You may only guess 1 letter at a time")
    else:
        guess_list.apphend(guess)
    return guess_list

def display_word(selected_word, guess_list):
    return[letter if letter in guess_list else '_' for letter in selected_word]

