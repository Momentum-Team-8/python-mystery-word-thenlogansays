import random

file = open('words.txt', 'r')

list = file.read().lower().split()
#print(list)

selected_word = random.choice(list)
print(selected_word)