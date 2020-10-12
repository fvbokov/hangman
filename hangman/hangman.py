from random import randint
from os.path import join, dirname

def find_pos(letter, word):
	last_pos = 0
	positions = []
	last_pos = word.find(letter)
	while(last_pos != -1):
		positions.append(last_pos)
		last_pos = word.find(letter, last_pos + 1)
	return positions	

def print_progress(word, positions):
	for i, letter in zip(range(len(word)), word):
		if i in positions:
			print(letter, end=" ")
		else:
			print("_", end=" ")	

words = [
	"morriage",
	"control",
	"population",
	"impression",
	"diamond",
	"permission"
]

assets = join(dirname(__file__), "assets")

with open(join(assets, "0.txt")) as f:
	gallows = f.read()
print(gallows)

letters_count = 0
word = words[randint(0, len(words) - 1)]

for i in word:
	letters_count += 1
print("Letters in word:", letters_count)
positions = []
mistakes_count = 1

while(mistakes_count < 6):
	print("Guess the letter:")
	letter = input()
	if len(letter) != 1:
		print("You entered too many symbols. You lose")
		with open(join(assets, "6.txt")) as f2:
			gallows = f2.read()
		print(gallows)
		
	if letter in word:
		positions.extend(find_pos(letter, word))
		print("Correct! The letter position is", find_pos(letter, word))
	else:
		print("Incorrect!")
		with open(join(assets, "{}.txt").format(mistakes_count)) as f2:
			gallows = f2.read()
		print(gallows)
		mistakes_count += 1

	print_progress(word, positions)
print("")	
print("I'm trying to be gracious, I'm SOOOO sorry, you're dead. Bye")
with open(join(assets, "6.txt")) as f3:
	gallows = f3.read()
print(gallows)	