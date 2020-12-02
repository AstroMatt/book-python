import os
import subprocess
import logging

PATH = os.path.join('Users', 'matt', 'Desktop')
readme_found = False

for root, dirs, files in os.walk(PATH):
    for name in files:
        if 'README' in name:
            absolute_path = os.path.join(root, name)
            cmd = ['type', absolute_path]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
            print(result.stdout)
            readme_found = True

if not readme_found:
    logging.critical('Readme not found')
