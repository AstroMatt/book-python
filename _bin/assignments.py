import csv
from pathlib import Path
import re


OUTPUT = r'/tmp/assignments.csv'
slug = re.compile(r'[a-zA-Z0-9 ]')
toctree = []
result = []


with open('../index.rst') as file:
    indexes = [filename
               for line in file
               if (filename := '..'+line.strip())
               and filename.startswith('../')
               and filename.endswith('.rst')
               and Path(filename).exists()]

for filename in indexes:
    toctree.append(str(filename))
    chapter = filename.split('/')[1]

    with open(filename) as file:
        if (files := [filename
                      for line in file
                      if (filename := f'../{chapter}/{line.strip()}')
                      and not filename.startswith('.. ')
                      and filename.endswith('.rst')
                      and Path(filename).exists()]):
            toctree.extend(files)


for path in toctree:
    with open(path) as file:
        content = file.readlines()

        for i, line in enumerate(content):
            if line.startswith(r'* Assignment name:'):
                assignment = content[i].split(':')[1].strip()
                updated = content[i+1].split(':')[1].strip()
                complexity = content[i+2].split(':')[1].strip()
                lines = int(content[i+3].split(':')[1].strip().split()[0])
                duration = int(content[i+4].split(':')[1].strip().split()[0])

                uri = str(path).replace('../', '').replace('.rst', '.html')
                id = ''.join(slug.findall(assignment)).lower().replace(' ', '-')
                url = f'https://python.astrotech.io/{uri}#{id}'

                result.append({
                    'assignment': assignment, 'updated': updated,
                    'complexity': complexity, 'lines': lines,
                    'duration': duration, 'url': url,
                })


with open(OUTPUT, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=result[0].keys(), quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(result)
