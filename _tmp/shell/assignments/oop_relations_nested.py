"""
* Assignment: OOP Relations Nested
* Filename: oop_relations_nested.py
* Complexity: medium
* Lines of code: 30 lines
* Time: 21 min

English:
    1. Client can open a bank account
    2. Client can have many accounts
    3. Bank has many clients
    4. Each account has unique number generated when opening an account
    5. Client can ask about number of all of his accounts
    6. Client can add money to the account
    7. Client can withdraw money from the account
    8. Compare result with "Tests" section (see below)

Polish:
    1. Klient może otworzyć konto w banku
    2. Klient może mieć wiele kont
    3. Bank może mieć wielu klientów
    4. Każde konto ma unikalny numer, który jest generowany przy zakładaniu
    5. Klient może odpytać o numery wszystkich swoich kont
    6. Klient może wpłacić pieniądze na swoje konto
    7. Klient może wybrać pieniądze z bankomatu
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    TODO: Doctests
"""

# Solution
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Client:
    name: str
    pesel: int


@dataclass
class Account:
    number: int
    owner: Client
    amount: Decimal = 0.0


@dataclass
class Bank:
    accounts = []


@dataclass
class ATM:
    def input_card(self, card):
        pass

    def input_pin(self):
        pass

    def input_amount(self, amount):
        pass

    def give_money(self):
        pass

    def give_card(self):
        pass

    def _check_pin_number(self, pin):
        pass

    def _check_if_withdraw_possible(self):
        pass
