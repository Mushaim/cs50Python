from character import Character

class Enemy(Character):
    def __init__(self,name , health, attack, xp_reward, score_reward, loot=None):
        super().__init__(name, health,attack)
        self.xp_reward = xp_reward
        self.score_reward = score_reward
        self.loot = loot

