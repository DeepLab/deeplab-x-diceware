import os, re
from random import randint, shuffle
from sys import exit

DICEWARE_LIST = {}
DICEWARE_LIST_PATH = "diceware.wordlist.asc.txt"
CUSTOM_LIST_PATH = "custom.wordlist.txt"

def setup():
	ROLLS = []
	WORDS = []

	with open(DICEWARE_LIST_PATH, 'rb') as D:
		for line in D.readlines():
			line = re.findall(r'(\d{5})\s*(.*)', line.strip())[0]
			
			ROLLS.append(str(line[0]))
			WORDS.append(line[1])

	shuffle(WORDS)

	if os.path.exists(CUSTOM_LIST_PATH):
		with open(CUSTOM_LIST_PATH, 'rb') as D:
			CUSTOM_WORDS = [c.strip() for c in D.readlines() if len(c.strip()) >= 2]

		WORDS = WORDS[:-(len(CUSTOM_WORDS))]
		WORDS.extend(CUSTOM_WORDS)

		shuffle(WORDS)

	for i, r in enumerate(ROLLS):
		DICEWARE_LIST[r] = WORDS[i]

def roll(num_dice, roll_range=[1,6]):
	return "".join([str(randint(*roll_range)) for r in xrange(num_dice)])

def generate_passphrase(num_words=8):
	return " ".join([DICEWARE_LIST[roll(5)] for r in xrange(num_words)])

if __name__ == "__main__":
	pad_len = 20

	os.system('clear')
	setup()

	print "Diceware!\n\n"

	while True:
		try:
			if raw_input("press enter to generate credentials") == '':
		
				print "\nOK, how about:\n"
				print "%s\n" % ("*" * pad_len)
				print generate_passphrase()
				print "\n%s" % ("*" * pad_len)
				print "\n"
		
		except KeyboardInterrupt as e:
			break

	exit(0)

