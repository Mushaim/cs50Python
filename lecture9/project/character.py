import random

class Character:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.max_health = health

    def is_alive(self):
        return self.health > 0

    def take_damage(self,damage):
        self.health -= damage

    def attack_target(self,target):
        damage = random.randint(1,self.attack)
        target.take_damage(damage)
        return damage


