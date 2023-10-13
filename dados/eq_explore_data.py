from pathlib import Path
import json
import plotly.express as px


path = Path('eq_data/eq_1_day_m1.geojson')
contents = path.read_text()

all_eq_data = json.loads(contents)
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats, titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    titles.append(title)

print(mags)
print(lons)
print(lats)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=titles,)
fig.show()

#path = Path('eq_data/readable_eq_data.geojson')

#readable_contentds = json.dumps(all_eq_data, indent=4)
#path.write_text(readable_contentds)
