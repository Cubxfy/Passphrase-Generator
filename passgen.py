import random

list_ = open("words_alpha.txt").read().split()

print(f"{random.choice(list_)}-{random.choice(list_)}-{random.choice(list_)}")
