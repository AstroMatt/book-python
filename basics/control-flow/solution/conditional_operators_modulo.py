number = input('What is your number?: ')
number = float(number)

print(number % 2 == 0)

# '50' % 1
# Traceback (most recent call last):
#     ...
# TypeError: not all arguments converted during string formatting

# '50 %s' % 1
# 50 1

# 50 % 1
# 0
