import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/astro-eva.csv'

astro_eva = pd.read_csv(DATA, delimiter=';')
astro_eva[['EV1', 'EV2', 'EV3']] = astro_eva['Participants'].str.split(', ', expand=True)
astro_eva['Duration'] = pd.to_timedelta(astro_eva['Duration'])

result = (pd.concat([
           astro_eva[['EV1','Duration']].rename(columns={'EV1':'Astronaut'}),
           astro_eva[['EV2','Duration']].rename(columns={'EV2':'Astronaut'}),
           astro_eva[['EV3','Duration']].rename(columns={'EV3':'Astronaut'})
       ], axis='rows')
       .groupby('Astronaut')
       .sum()
       .sort_values('Duration', ascending=False))

result
