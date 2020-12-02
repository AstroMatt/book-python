def print_1(what):
    """
    >>> print_1('José')
    José
    José
    José
    José
    José
    """
    for i in range(0, 5):
        print(what)


def print_2(what):
    """
    >>> print_2('José')
    José
    José
    José
    José
    José
    """
    i = 0

    while i < 5:
        print(what)
        i += 1


def print_3(what):
    """
    >>> print_3('José')
    José
    José
    José
    José
    José
    <BLANKLINE>
    """
    print(f'{what}\n' * 5)


if __name__ == '__main__':
    user_string = input('Type: ')
    print_1(user_string)
    print_2(user_string)
    print_3(user_string)
