from player import Player
from enemy import Enemy
from random import random,choice,randint


def main():
    print("🏰 WELCOME TO THE DUNGEON ESCAPE!")
    name = input("Enter your hero's name: ")
    player = Player(name)
    steps = 0
    exit_at = randint(8,12)
    won = False
    alive = True
    while alive and not won:
        steps,won,alive = explore(player,steps,exit_at)
    if not player.is_alive or not alive:
        print(f"💀Game Over! Final score {player.score}")
    elif won:
        print(f"🎉 Congratulations! You escaped with score {player.score}")


def combat(player,enemy):
    print(f"{enemy.name} appears! HP: {enemy.health}, Attack: {enemy.attack}")
    while player.is_alive() and enemy.is_alive():
        action = input("Do you want to [a]ttack, open [i]nventory or [r]un?").lower()

        if action == "a":
            dmg = player.attack_target(enemy)
            e_health = max(0,enemy.health)
            print(f"You hit the enemy by {dmg} (Enemy HP is {e_health})")
            if enemy.is_alive():
                edmg = enemy.attack_target(player)
                p_health = max(0,player.health)
                print(f"Enemy hit you by {dmg} (Your HP is {p_health})")

        elif action == "i":
            print("📦 Inventory: ",{k:v for k,v in player.inventory.items() if v > 0})
            choice = input("Use what? Want to go [b]ack: ")
            if choice.lower() == "b":
                continue
            player.use_item(choice)

        elif action == "r":
            print("You ran out successfully")
            return
        else:
            print("Invalid action")

    if player.is_alive():
        print(f"You have defeated the {enemy.name}")
        player.win += 1
        player.xp += enemy.xp_reward
        player.score += enemy.score_reward
        if enemy.loot and random() < 10:
            if enemy.loot == "Shield" and not player.shield_active:
                player.inventory[enemy.loot] = 1
                print(f"✨ You found {enemy.loot}!")
            elif enemy.loot == "Magic Sword" and not player.sword_active:
                player.inventory[enemy.loot] = 1
                print(f"✨ You found {enemy.loot}!")
            elif enemy.loot == "Ring of Vitality" and not player.ring_active:
                player.inventory[enemy.loot] = 1
                print(f"✨ You found {enemy.loot}!")

        if player.xp >= player.level * 20:
            player.level_up()
            print(f"You have leveled up! Now level {player.level}")
        return True
    else:
        print(f"Player {player.name} has been defeated by {enemy.name}")
        return False

def healing_fountain(player):
    if player.health < player.max_health:
        healed = player.heal()
        print(f"Fountain has healed {healed} HP : {player.health}")
    else:
        player.inventory["Potion"] += 1
        print(f"Health is already full healing fountain added a potion in inventory Potion: {player.inventory["Potion"]}")

def explore(player,steps,exit_at):
    while True:
        dir = input("\nChoose a direction: [l]eft, [r]ight or [f]orward?")
        if dir.lower() in ["l","r","f"]:
            break
        else:
            print("Invalid command")
    steps +=1
    if steps == exit_at:
        print("You have successfully found the way out of dungeon! YOU WIN!")
        return steps,True,True

    event = choice(["enemy","healing_fountain","empty"])
    if event == "enemy":
        if player.win == 0:
            enemy = Enemy("Goblin",10,3,10,10,loot = "shield")
        elif player.win == 1:
            enemy = choice([Enemy("Goblin",10,3,10,10,loot = "shield"),
                           Enemy("Skeleton",15,4,15,15,loot = "Magic sword")])
        else:
            enemy = choice([Enemy("Goblin",10,3,10,10,loot = "shield"),
                           Enemy("Skeleton",15,4,15,15,loot = "Magic sword"),
                           Enemy("Dragon",25,6,30,30,loot = "Ring of Vitality")])
        alive = combat(player,enemy)
        return steps,False,alive
    elif event == "healing_fountain":
        print("You have found an healing fountain")
        healing_fountain(player)
    else:
        print("You entered an empty corridor")

    return steps,False, True




if __name__ == "__main__":
    main()




