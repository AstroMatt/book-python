from datetime import datetime, date, timezone
import json
from typing import Dict, List, Union

FILE: str = '/tmp/json-datetimes.json'
DATA: Dict[str, Union[Dict[str, Union[date, str]], List[Dict[str, Union[datetime, str]]]]] = {
    "astronaut": {
        "date": date(1961, 4, 12),
        "person": "mark.watney@nasa.gov"
    },
    "flight": [
        {"datetime": datetime(1969, 7, 21, 2, 56, 15), "action": "landing"}
    ]
}


class JSONDatetimeEncoder(json.JSONEncoder):
    def default(self, value):

        if isinstance(value, datetime):
            return value.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        elif isinstance(value, date):
            return value.strftime('%Y-%m-%d')


class JSONDatetimeDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.default)

    def default(self, obj):
        for key, value in obj.items():

            if key == 'datetime':
                dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
                obj['datetime'] = dt.replace(tzinfo=timezone.utc)

            elif key == 'date':
                dt = datetime.strptime(value, '%Y-%m-%d')
                obj['date'] = dt.replace(tzinfo=timezone.utc).date()

        return obj


with open(FILE, mode='w', encoding='utf-8') as file:
    json.dump(DATA, file, cls=JSONDatetimeEncoder)


with open(FILE, encoding='utf-8') as file:
    data = json.load(file, cls=JSONDatetimeDecoder)


print(data)
