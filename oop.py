class Weapon:
    def __init__(self, name, price) -> None:
        self._name = name
        self._price = price


class Person:
    def __init__(self, name, age, balance) -> None:
        self._name = name
        self._age = age
        self._balance = balance
        self._health = 100
        self._weapons = []

    def buy_weapon(self, weapon):
        if self._balance >= weapon._price:
            self._balance -= weapon._price
            self._weapons.append(weapon)
            print(f'Congrats, you bought a new {weapon._name}')
            print(f'Your balance: {self._balance}')
        else:
            print(f'You dont have enough money to buy {weapon._name}')

    def my_weapons(self):
        for w in self._weapons:
            print(f'I have {w._name}')


weapons_list = (
    ('AK-47', 3000),
    ('MK', 3500),
    ('Sniper', 5000),
    ('Deagle', 1700)
)


weapons = []
for w in weapons_list:
    weapons.append(Weapon(name=w[0], price=w[1]))


p = Person(name='Feruz', age=20, balance=15000)


p.buy_weapon(weapons[0])
p.buy_weapon(weapons[3])
p.my_weapons()