from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#for index, data in enumerate(header_row):
#    print(f'{index}-{data}')

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    temp = int(row[4])
    highs.append(temp)
    dates.append(current_date)
    low = int(row[5])
    lows.append(low)

plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily high temperatures, july 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()
ax.set_ylabel("Temperature (f)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()