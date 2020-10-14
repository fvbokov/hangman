from random import randint
from os.path import join, dirname

#functions---
def find_pos(letter, word): # get positions of letters in word
	last_pos = 0
	positions = []
	last_pos = word.find(letter)
	while(last_pos != -1): ### word.find() returns -1 if there is no such symbol
		positions.append(last_pos)
		last_pos = word.find(letter, last_pos + 1)
	return positions	

def print_progress(word, positions): # function prints gaps filled with right letters that have been already guessed
	for i, letter in zip(range(len(word)), word):
		if i in positions:
			print(letter, end=" ")
		else:
			print("_", end=" ")	
#------------

#word list---
words = [    
	"alone",
	"control",
	"population",
	"impression",
	"diamond",
	"permission"
]
#------------

#variables---
assets = join(dirname(__file__), "assets") ### get those files with hangman progress
word = words[randint(0, len(words) - 1)] ### hidden word
letters_count = 0 ### how many words in hidden word
positions = [] ### indexes of guessed words
mistakes_count = 1 ### how many mistakes player made
gallows = None ### the gallows texture
#------------

#phrases---
phrases = {
	"letters" : "Letters in word:",
	"guess" : "Guess the letter:",
	"input_error" : "You entered too many symbols. Try again",
	"correct" : "Correct! The letter position is",
	"incorrect" : "Incorrect!",
	"loss" : "I'm trying to be gracious, I'm SOOOO sorry, you're dead. Bye",
	"win" : "Congratulations on your victory. The hidden word was:"
}
#----------

#the game progress---
with open(join(assets, "0.txt")) as f: ### print gallows w/o body
	gallows = f.read()
print(gallows)

for i in word: ### count the letters in hidden word
	letters_count += 1
print(phrases["letters"], letters_count)

while(mistakes_count < 6): ### main game cycle
	print(phrases["guess"])
	letter = input()
	if len(letter) != 1: ### check if only one symbol inputed
		print(phrases["input_error"])
		letter = ""
		
	if letter in word:
		positions.extend(find_pos(letter, word))
		print(phrases["correct"], find_pos(letter, word))
	else:
		print(phrases["incorrect"])
		with open(join(assets, "{}.txt").format(mistakes_count)) as f2:
			gallows = f2.read()
		print(gallows)
		mistakes_count += 1

	if len(positions) == len(word): ### check if the word is fully guessed
		break

	print("")
	print_progress(word, positions)
print("")	
if mistakes_count == 6:
	print(print["loss"])
	with open(join(assets, "6.txt")) as f3:
		gallows = f3.read()
	print(gallows)
else:
	print(phrases["win"], word)		
#---------------