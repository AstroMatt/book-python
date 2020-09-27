import pandas as pd
import requests


DATA = 'https://python.astrotech.io/_static/openapi.json'

resp = requests.get(DATA)
data = resp.json()

api = pd.DataFrame(data['paths']).transpose()
api.applymap(lambda x: x['summary'] if type(x) == dict else pd.NA)

api
