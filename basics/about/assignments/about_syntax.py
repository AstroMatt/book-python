"""
* Assignment: About Syntax
* Filename: about_syntax.py
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Write comments:
        a. This is my first Python script
        b. If not counting the previous Hello World
    2. Define variable `name` and set its value to `Mark Watney`
    3. Add inline comment to variable declaration with text: `Space Pirate`
    4. Define `result` with text "Hello World {name}", where "Mark Watney" is the value of `name` variable
    5. Use f-string

Polish:
    1. Napisz komentarz:
        a. This is my first Python script
        b. If not counting the previous Hello World
    2. Zdefiniiuj zmienną `name` i ustaw jej wartość na `Mark Watney`
    3. Dodaj komentarz "inline" do zmiennej o treści: `Space Pirate`
    4. Zdefiniiuj `result` z tekstem "Hello World {name}", gdzie "Mark Watney" jest wartością zmiennej `name`
    5. Zastosuj f-string

Tests:
    >>> result
    'Hello World Mark Watney'
"""

# Solution

# This is my first Python script
# If not counting the previous Hello World
name = 'Mark Watney'  # Space Pirate
result = f'Hello World {name}'
