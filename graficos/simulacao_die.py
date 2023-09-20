from die import Die

die = Die()

random = []

for value in range(100):
    random.append(die.roll())


print(random)