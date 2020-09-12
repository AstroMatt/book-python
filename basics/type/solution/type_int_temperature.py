C = -273
K = +273

moon_day = 453 + K
moon_night = 93 + K
mars_max = 20 + C
mars_min = -120 + C
mars_avg = -63 + C

print(f'Moon day: 453K, {moon_day}°C')
print(f'Moon night: 93K, {moon_night + C}°C')
print(f'Mars high: {mars_max}K, 20°C')
print(f'Mars low: {mars_min}K, -153°C')
print(f'Mars avg: {mars_avg}K, -63°C')

# Moon day: 453K, 726°C
# Moon night: 93K, 93°C
# Mars high: -253K, 20°C
# Mars low: -393K, -153°C
# Mars avg: -336K, -63°C
