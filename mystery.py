import random


file = open('words.txt', 'r')
list = file.read().lower().split()
#print(list)

#selected_word = random.choice(list)
#print('selected word is: ', selected_word)


easy_list = [ word for word in list if 4 <= len(word) <= 6 ]
normal_list = [ word for word in list if 6 <= len(word) <= 8]  
hard_list = [ word for word in list if 8 <= len(word)]

def get_level():
    level = input('Choose a level (easy, normal, hard):')
    if level == 'easy':
        word = random.choice(easy_list)
    elif level == 'normal':
        word = random.choice(normal_list)
    elif level == 'hard':
        word = random.choice(hard_list)
    else:
        return get_level()
    print(f'Your word is {len(word)} characters long.')
    return word

def display_word(word, guess_list):
        return [letter if letter in guess_list and word else '_' for letter in word]

def guess_input(guess_list):
    guess = input("Choose a letter").lower()
    if len(guess) != 1:
        print("You may only guess 1 letter at a time")
    else:
        guess_list.append(guess)
    return guess_list

def play(word):
    guesses = 0
    guess_list = []
    guess_input(guess_list)
    wrong_guesses(word, guess_list)
    while True:
        len(guess_list) < 8
        #print(f"Wrong Guesses: {' '.join(wrong_guesses(word, guess_list))}")
        print(f"Mystery Word: {' '.join(display_word(word, guess_list))}")
        print(f"You have {8- len(guess_list)} guesses left. Don't screw it up.")
        guesses += 1
        break
        if "_" not in display_word(word, guess_list):
            print(f"Yay! You guessed the Mystery Word: {word}")
            break
        if len(guess_list) >= 8:
            print(f"Oops, you're out of guesses.  The mystery word was {word}.")
            break

def wrong_guesses(word, guess_list):
    for letter in guess_list:
        if letter not in word:
            return sorted(set(letter))


word = (get_level())
play(word)