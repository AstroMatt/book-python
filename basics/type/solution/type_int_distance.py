m = 1
km = 1000

armstrong_line = 18000 * m
stratosphere = 20000 * m
usaf_space = 80000 * m

karman_line_earth = 100 * km
karman_line_mars = 80 * km
karman_line_venus = 250 * km

print(f'Armstrong Line: {armstrong_line // m} m')
print(f'Stratosphere: {stratosphere // m} m')
print(f'USAF Space: {usaf_space // m} m')
print(f'Kármán Line Earth: {karman_line_earth // km} km')
print(f'Kármán Line Mars: {karman_line_mars // km} km')
print(f'Kármán Line Venus: {karman_line_venus // km} km')

# Armstrong Line: 18000 m
# Stratosphere: 20000 m
# USAF Space: 80000 m
# Kármán Line Earth: 100 km
# Kármán Line Mars: 80 km
# Kármán Line Venus: 250 km
