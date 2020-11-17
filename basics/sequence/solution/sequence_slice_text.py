"""
>>> example
'Mark Watney'
>>> a
'Jan Twardowski'
>>> b
'Jan Twardowski'
>>> c
'Mark Watney'
>>> d
'Melissa Lewis'
>>> e
'Ryan Stone'
>>> f
'Ryan Stone'
>>> g
'Jan Twardowski'
"""

example = 'lt. Mark Watney, PhD'
a = 'dr hab. inż. Jan Twardowski, prof. AATC'
b = 'gen. pil. Jan Twardowski'
c = 'Mark Watney, PhD'
d = 'lt. col. ret. Melissa Lewis'
e = 'dr n. med. Ryan Stone'
f = 'Ryan Stone, MD-PhD'
g = 'lt. col. Jan Twardowski\t'

example = example[4:-5]
a = a[13:-12]
b = b[10:]
c = c[:-5]
d = d[14:]
e = e[11:]
f = f[:-8]
g = g[9:-1]

# print(f'>{g[9:-1]}<')
# >Jan Twardowski<
