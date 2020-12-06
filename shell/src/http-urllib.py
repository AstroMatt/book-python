import os
import urllib.request
import zipfile

data_path = 'data'

os.makedirs(data_path, exist_ok=True)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'
file_name = url.split('/')[-1]
dest_file = os.path.join(data_path, file_name)

data_file = 'SMSSpamCollection'
data_full = os.path.join(data_path, data_file)

urllib.request.urlretrieve(url, dest_file)

with zipfile.ZipFile(dest_file) as zip_file:
    zip_file.extract(data_file, path=data_path)