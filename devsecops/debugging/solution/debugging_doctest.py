

class Astronaut:
    """
    New Astronaut
    """

    def __init__(self, name):
        self.name = name

    def say_hello(self, lang='en'):
        """
        prints greeting according to the language

        >>> Astronaut(name='José Jiménez').say_hello(lang='es')
        '¡hola José Jiménez!'

        >>> Astronaut(name='Иван Иванович').say_hello(lang='ru')
        'здраствуйте Иван Иванович!'
        """
        if lang == 'en':
            return f'hello {self.name}'
        elif lang == 'es':
            return f'¡hola {self.name}!'
        elif lang == 'ru':
            return f'здраствуйте {self.name}!'
        else:
            return f'witaj {self.name}!'


def doctest(docstring):
    if not docstring:
        return None

    docstring.replace('\\', '').split('\n')

    i = 0

    for line in docstring:
        line = line.strip()

        if line.startswith('>>> '):
            expected = docstring[i+1].strip()
            code = line.split('>>> ')[1]
            result = eval(code)

            if isinstance(result, str):
                result = f"'{result}'"

            if result == expected:
                print('ok')
            else:
                print(f'\nExpected: {expected}\nGot: {result}')

        i += 1



jose = Astronaut(name='José Jiménez')

for method in dir(jose):
    print(f'jose.{method}.__doc__')
    docstring = eval(f'jose.{method}.__doc__')
    doctest(docstring)



