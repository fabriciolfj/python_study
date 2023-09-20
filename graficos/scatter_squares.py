import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8-dark-palette")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

ax.axis([0, 1100, 0, 1_100_100])
ax.ticklabel_format(style='plain')

#plt.show()
#salva o grafico no disco
plt.savefig('squares_plot.png', bbox_inches='tight')