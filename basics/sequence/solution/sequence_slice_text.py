a = 'lt. Mark Watney'
b = 'lt. col. Jan Twardowski\t'
c = 'dr hab. inż. Jan Twardowski, prof. LAW'
d = 'gen. pil. Jan Twardowski'
e = 'Mark Watney, PhD'
f = 'lt. col. ret. Melissa Lewis'
g = 'dr n. med. Ryan Stone'
h = 'Ryan Stone, MD-PhD'

print(a[4:])
print(b[8:-1])
print(c[13:-11])
print(d[10:])
print(e[:-5])
print(f[5:-4])
print(g[:-7])
print(h[4:-8])

## Alternative Version
length = len('Jana III Sobieskiego')
print(a[4:length + 4])
print(b[6:length + 6])

## Alternative Version
text = 'Jana III Sobieskiego'
length = len(text)

b = b[b.find(text):length + b.find(text)]
c = c[c.find(text):length + c.find(text)]
d = d[d.find(text):length + d.find(text)]
e = e[e.find(text):length + e.find(text)]
f = f[f.find(text):length + f.find(text)]
g = g[g.find(text):length + g.find(text)]
h = h[h.find(text):length + h.find(text)]

print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')
print(f'd: {d}')
print(f'e: {e}')
print(f'f: {f}')
print(f'g: {g}')
print(f'h: {h}')


## Alternative Version
def get_slice(text):
    length = len(text)
    start = text.find(text)
    stop = start + length
    return slice(start, stop)


text = 'Jana III Sobieskiego'
b = b[get_slice(text)]
c = c[get_slice(text)]
d = d[get_slice(text)]
e = e[get_slice(text)]
f = f[get_slice(text)]
g = g[get_slice(text)]
h = h[get_slice(text)]
