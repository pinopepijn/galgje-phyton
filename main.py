print("Hallo, welkom bij galgje")
print ()
name = input('Wat is je naam?\n')
print()
print('Hoi, %s.' % name)
print()
print( "Het is de bedoeling dat je alle leters goed raad om een woord te vormen.")
print("Je hebt maar een paar kansen om de letters te raden.")
print()

import random
words = [
    "mango", "vuurtoren", "muziek", "bosbes", "plaats", "telefoon", "statief"
]
picked = random.choice(words)
words = (picked)
galg = [
    "  ---------", "  |       |", "  |       O", "  |       |",
    "  |     --+--", "  |       |", "  |      / \\", "  |", "  |", "------"
]

guesses = ''

turns = 10

while turns > 0:

    letters_not_guesed = 0
    toonwoord = ''

    for char in words:

        if char in guesses:

            toonwoord = toonwoord + (char)

        else:

            toonwoord = toonwoord + ('_')

            letters_not_guesed += 1

    print('Woord:', toonwoord, '. Al gegokte letters:', guesses)
    print()
    print()

    if letters_not_guesed == 0:
        print()

        print('Hoera,', name, ',je hebt gewonnen')

        break

    print

    guess = input('Raad een letter: ')

    guesses += guess

    if guess not in words:

        turns -= 1

        galgregel = turns
        nr_of_to_print_lines = (10 - turns)
        while nr_of_to_print_lines > 0:
            print(galg[galgregel])
            galgregel += 1
            nr_of_to_print_lines -= 1
        print("")

        print('Helaas, dat is niet goed')

        print(name, 'je hebt nog', +turns, 'kansen')

        if turns == 0:

            print()

            print('Helaas', name, 'je hebt verloren, het woord was:', words)

