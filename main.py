print ("Hallo, welkom bij galgje")

name = input('Wat is je naam?\n')
print('Hoi, %s.' % name)
print("Het is de bedoeling dat je alle leters goed raad om een woord te vormen.")
print ("Je hebt maar een paar kansen om de letters te raden.")

import random 
words = ["mango", "vuurtoren", "muziek", "bosbes", "plaats", "telefoon", "statief"]
picked = random.choice(words)
galg = [
  "  ---------",
  "  |       |",
  "  |       O",
  "  |       |",
  "  |     --+--",
  "  |       |",
  "  |      / \\",
  "  |",
  "  |",
  "------"
]


guesses = ''

turns = 10

while turns > 0:         

    letters_not_guesed = 0             
    toonwoord=''

print ('Helaas, dat is niet goed')
 
        print (name, 'je hebt nog', + turns, 'kansen') 

        if turns == 0:           
    
            print ()
 
            print ('Helaas', name, 'je hebt verloren, het woord was:', woord)

