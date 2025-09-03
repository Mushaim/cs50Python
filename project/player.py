from character import Character
import random

class Player(Character):
    def __init__(self,name):
        super().__init__(name,health = 15,attack = 5)
        self.level = 1
        self.xp = 0
        self.win = 0
        self.score = 0
        self.inventory = {"Potion" : 0}
        self.shield_active = False
        self.sword_active = False
        self.ring_active = False

    def take_damage(self,damage):
        if self.shield_active:
            damage = max(0,dmg-1)
        self.health -= damage

    def heal(self):
        healed = random.randint(3,10)
        self.health = min(self.max_health,self.health + healed)
        return healed

    def use_item(self,item):
        if item == "Potion":
            if self.inventory["Potion"] > 0:
                self.health = self.max_health
                print("🧪 You used the portion and restore to full health")
                self.inventory[item] -= 1
            else:
                print("❌ Potion is not in inventory")
        elif item == "Shield":
            if not self.shield_active and self.inventory.get(item,0) > 0:
                print("🛡️ Shield Activated. Incoming damage reduced by 1 permanently")
                self.shield_active = True
                self.inventory[item] -= 1
            elif self.shield_active:
                print("Shield is already activated")
            else:
                print("❌ Shield is not in inventory")
        elif item == "Magic sword":
            if not self.sword_active and self.inventory.get(item,0) > 0:
                print(f"🗡️ Magic sword equipped! Attack +3")
                self.attack += 3
                self.sword_activate = True
                self.inventory[item] -= 1
            elif self.sword_active:
                print("Magic sword is already activated")
            else:
                print("❌ Magic sword is not in inventory")
        elif item == "Ring of Vitality":
            if not self.ring_active and self.inventory.get(item,0) > 0:
                print("💍Ring Glows! Max HP +5")
                player.max_health += 5
                player.health += 5
                self.inventory[item] -= 1
                self.ring_active = True
            elif self.ring_active:
                print("Ring of Vitality is already activated")
            else:
                print("❌ Ring of Vatility is not in inventory")
        else:
            print("Invalid Item")

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.max_health += 5
        self.attack += 2
        self.health = self.max_health



