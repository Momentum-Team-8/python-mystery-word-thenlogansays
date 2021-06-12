import random


file = open('words.txt', 'r')
list = file.read().lower().split()
#print(list)

selected_word = random.choice(list)
selected_word_list = selected_word.split()
#print('selected word is: ', selected_word)

def play(selected_word):
    incorrect_guesses = []
    guess_input()
    display_word(selected_word_list, guess_list)
    if guesses == 8:
        print(f"Game Over. The mystery word was {selected_word}")
    elif guesses < 0 and "_" in selected_word_list:
        print(f"Mystery Word: {' '.join(display_word(selected_word_list, guess_list))}")
        print(f"You've already guessed: {' '.join(incorrect_guesses)}")
        print(f"You have {guesses_available} guesses left")
    elif guesses < 8 and "_" not in selected_word_list:
        print(f"Yay! you guessed the Mystery Word {selected_word}")

def guess_input():
    guess_list = []
    guesses = 0
    guess = input("Choose a letter").lower()
    if len(guess) != 1:
        print("You may only guess 1 letter at a time")
    else:
        guesses += 1
        guess_list.append(guess)
    

def display_word(selected_word_list, guess_list):
    print([letter if letter in guess_list else '_' for letter in selected_word_list])




play(selected_word)