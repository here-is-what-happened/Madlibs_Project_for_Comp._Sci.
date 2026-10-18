import random
# This project is a madlibs project

name = input("Enter a name or type random for a random name -- > ").capitalize()
verb = input("Enter a verb or type random for a random verb -- > ").lower()
place = input("Enter a place or type random for a random place -- > ").capitalize()
ing_verb = input("Enter a ing_noun or type random for a random ing_noun -- > ").lower()
noun = input("Enter a noun or type random for a random noun -- > ").lower()
plant = input("Enter a plant or type random for a random plant -- > ").lower()
number = input("Enter a number or type random for a random number -- > ").lower()
game = input("Enter a game or type random for a random game -- > ").lower()
plural_noun = input("Enter a plural noun or type random for a random plural noun -- > ").lower()
senses = input("Enter a sense or type random for a random sense -- > ").lower()

name_list = ['', '', '', '', '']
verb_list = ['', '', '', '', '']
place_list = ['', '', '', '', '']
ing_verb_list = ['', '', '', '', '']
noun_list = ['', '', '', '', '']
plant_list = ['', '', '', '', '']
number_list = ['', '', '', '', '']
game_list = ['catan', 'monopoly', 'Zelda', 'chess', 'rock, paper, scissors']
plural_noun_list = ['cats', 'boxes', 'leaves', 'children', 'puppies']
senses_list = ['eyesight', 'hearing', 'proprioception', 'taste', 'sense of heat']





if name == 'random':
    name = random.choice(name_list)
if verb == 'random':
    verb = random.choice(verb_list)
if place == 'random':
    place = random.choice(place_list)
if ing_verb == 'random':
    ing_verb = random.choice(ing_verb_list)
if noun == 'random':
    noun = random.choice(noun_list)
if plant == 'random':
    plant = random.choice(plant_list)
if number == 'random':
    number = random.choice(number_list)
if game == 'random':
    game = random.choice(game_list)
if plural_noun == 'random':
    plural_noun = random.choice(plural_noun_list)
if senses == 'random':
    senses = random.choice(senses_list)


print(f"""\nOne day {name} was {verb} to their {place} while {ing_verb}. 
Out of nowhere, a {noun} with a {plant} told him to go {number} degrees in the other direction
Before he could go, {plural_noun} challenged him to {game}.
The twist was that he lost his {senses}. He ended up winning!""")