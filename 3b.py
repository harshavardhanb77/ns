import random
deck=["diamond","spade","Club","Heart"]
print("Before shuffling card",deck)
random.shuffle(deck)
print(deck)
print("Randomly choosing a suit",random.choice(deck))
new_deck=random.sample(deck,2)
print(new_deck)