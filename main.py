print ("Hallo, welkom bij galgje")

name = input('Wat is je naam?\n')
print('Hoi, %s.' % name)
print("Het is de bedoeling dat je alle leters goed raad om een woord te vormen.")
print ("Je hebt maar een paar kansen om de letters te raden.")

import random 
words = ["mango", "vuurtoren", "muziek", "bosbes", "plaats", "telefoon", "statief"]
picked = random.choice(words)
print (picked)

guesses = ''

turns = 10



