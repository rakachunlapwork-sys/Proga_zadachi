import random
import time

class Person:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack_power = attack
        self.health = health

class Dragon(Person):
    def __init__(self, name, attack, health, choice):
        super().__init__(name, attack, health)
        self.choice = choice

class Knight(Person):
    def __init__(self, name, attack, health, choice):
        super().__init__(name, attack, health)
        self.choice = choice

class Gollem(Person):
    def __init__(self, name, attack, health, choice):
        super().__init__(name, attack, health)
        self.choice = choice
    
class Woolf(Person):
    def __init__(self, name, attack, health, choice):
        super().__init__(name, attack, health)
        self.choice = choice

