from timeit import timeit


setup = """
firstname = 'José'
lastname = 'Jiménez'
"""

TEST = dict()
TEST[0] = 'name = f"{firstname} {lastname}"'
TEST[1] = 'name = "{0} {1}".format(firstname, lastname)'
TEST[2] = 'name = firstname + " " + lastname'
TEST[3] = 'name = " ".join([firstname, lastname])'


for stmt in TEST.values():
    duration = timeit(stmt, setup, number=10000)
    print(f'{duration:.5}\t{stmt}')

# 0.00071559    name = f"{firstname} {lastname}"
# 0.0026514     name = "{0} {1}".format(firstname, lastname)
# 0.001015      name = firstname + " " + lastname
# 0.0013494     name = " ".join([firstname, lastname])
