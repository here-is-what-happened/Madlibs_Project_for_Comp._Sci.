name = input("Enter a name -- > ").capitalize()
verb = input("Enter a verb -- > ").lower()
place = input("Enter a place -- > ").capitalize()
ing_verb = input("Enter a ing_noun -- > ").lower()
noun = input("Enter a noun -- > ").lower()
plant = input("Enter a plant -- > ").lower()
number = input("Enter a number -- > ").lower()
game = input("Enter a game -- > ").lower()
plural_noun = input("Enter a plural noun -- > ").lower()
senses = input("Enter a sense -- > ").lower()

print(f"""\nOne day {name} was {verb} to their {place} while {ing_verb}. 
Out of nowhere, a {noun} with a {plant} told him to go {number} degrees in the other direction
Before he could go, {plural_noun} challenged him to {game}.
The twist was that he lost his {senses}. He ended up winning!""")