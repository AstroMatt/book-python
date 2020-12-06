import pandas as pd


## Solution 1
pd.DataFrame({
    'Crew': ['Prime', 'Prime', 'Prime', 'Backup', 'Backup', 'Backup'],
    'Role': ['CDR', 'LMP', 'CMP', 'CDR', 'LMP', 'CMP'],
    'Astronaut': ['Neil Armstrong', 'Buzz Aldrin', 'Michael Collins', 'James Lovell', 'William Anders', 'Fred Haise'],
})


## Solution 2
pd.DataFrame([
    {'Crew': 'Prime', 'Role': 'CDR', 'Astronaut': 'Neil Armstrong'},
    {'Crew': 'Prime', 'Role': 'LMP', 'Astronaut': 'Buzz Aldrin'},
    {'Crew': 'Prime', 'Role': 'CMP', 'Astronaut': 'Michael Collins'},
    {'Crew': 'Backup', 'Role': 'CDR', 'Astronaut': 'James Lovell'},
    {'Crew': 'Backup', 'Role': 'LMP', 'Astronaut': 'William Anders'},
    {'Crew': 'Backup', 'Role': 'CMP', 'Astronaut': 'Fred Haise'},
])
