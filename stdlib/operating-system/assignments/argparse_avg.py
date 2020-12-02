from argparse import ArgumentParser


def avg(*args):
    return sum(args) / len(args)


parser = ArgumentParser()
parser.add_argument('--numbers', nargs='+', type=float)
arguments = parser.parse_args()

result = avg(*arguments.numbers)
print(result)
