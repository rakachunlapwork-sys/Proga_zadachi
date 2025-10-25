import random
print()
class Person:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack_power = attack
        self.health = health

class Dragon(Person):
    def __init__(self, name, attack, health):
        super().__init__(name, attack, health)
    
    def kick(self, kick_power):
        self.kick_power = kick_power

class Knight(Person):
    def __init__(self, name, attack, health):
        super().__init__(name, attack, health)