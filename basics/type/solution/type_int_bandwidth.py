b = 1
kb = 1024 * b
Mb = 1024 * kb

B = 8 * b
kB = 1024 * B
MB = 1024 * kB

file_size = 100 * MB
speed = 100 * Mb
time = file_size // speed

print(f'File size: {file_size // MB} MB')
print(f'Download speed: {speed // MB} sec')
print(f'Download time: {time} sec')
