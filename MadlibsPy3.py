"""
This program prompts the user for input, then
substitutes that info into the blank spaces of a story
"""
print("\nWelcome to this Madlibs style story!")

name = input("\nCan you give me your name? It'll make the experience better: ")

print("""\nOkay, first I need three adjectives from you.
    An adjective is a word or phrase naming an attribute, added to or grammatically related to a noun to modify or describe it.
    Some examples are words like chewy, pretty, and smooth.""")

adjective1 = input("Adjective #1: ")
adjective2 = input("Adjective #2: ")
adjective3 = input("Adjective #3: ")

print("""\nNow I want three verbs in the present tense.
    Verbs are words used to describe an action, state, or an occurrence.
    Some examples are think, eat, sleep, and run.""")

verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
verb3 = input("Verb 3: ")

print("""\nAt this point, give me four nouns.
    A noun is a word (other than a pronoun) used to identify any of a class of people, places, or things common.
    Some examples are friend, chair, laser, and cream.""")

noun1 = input("Noun 1: ")
noun2 = input("Noun 2: ")
noun3 = input("Noun 3: ")
noun4 = input("Noun 4: ")

print("""\nNow I need a bunch of random stuff""")
animal = input("Name an animal: ")
food = input("A type of food: ")
fruit = input("A fruit: ")
number = input("A number: ")
hero = input("A superhero you love: ")
country = input("A country (doesn't have to be the one you live in): ")
dessert = input("A dessert: ")
year = input("A year: ")

# The template for the story

STORY = """This morning I woke up and felt %s because %s was going to finally %s over the big %s %s.
On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the
rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats.
Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a
puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."""

print(STORY % (adjective1, name, verb1, adjective2, noun1, noun2, animal, food, verb2, noun3, fruit,
  adjective3, name, verb3, number, name, hero, hero, name, country, name, dessert, name, year, noun4))