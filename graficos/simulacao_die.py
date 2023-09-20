from die import Die

die = Die()

random = []

for value in range(1000):
    random.append(die.roll())

frequence = {}
posicao = range(1, die.num_sides + 1)
for value in posicao:
    count = random.count(value)
    frequence[value] = count

print(frequence)
