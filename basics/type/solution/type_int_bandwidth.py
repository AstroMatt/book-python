"""
>>> int(duration // SECOND)
8
"""

SECOND = 1

b = 1
kb = 1024 * b
Mb = 1024 * kb

B = 8 * b
kB = 1024 * B
MB = 1024 * kB

speed = 100 * Mb / SECOND
size = 100 * MB
duration = size // speed
