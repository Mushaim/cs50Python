from player import Player
from enemy import Enemy
from random import random,choice,randint,choices
from scores import Scores
from colorama import Fore, init
init(autoreset=True)


def main():
    print("🏰 WELCOME TO THE DUNGEON ESCAPE!")
    name = input("Enter your hero's name: ")
    player = Player(name)
    steps = 0
    exit_at = randint(20,40)
    won = False
    alive = True
    record = Scores(player)
    while alive and not won:
        steps,won,alive = explore(player,steps,exit_at)
    if not player.is_alive or not alive:
        record.save_record("Lose")
        print("#"*40 + "\n")
        print(f"{Fore.RED}💀 Game Over! You fell in the dungeon!")
        print(f"{Fore.RED}Final score {player.score}")
        print("#"*40 + "\n")
        record.display_records()
    elif won:
        record.save_record("Win")
        print("#"*40 + "\n")
        print(f"{Fore.GREEN}🎉 Congratulations! {player.name} escaped with score {player.score}")
        print("\n" + "#"*40 + "\n")
        record.display_records()

def show_hud(player):
    print("\n" + "="*40)
    print(f"{Fore.CYAN} 🏹 {player.name} | HP: {player.health}/{player.max_health} | XP: {player.xp} | Score: {player.score}")
    inv = [f"{k} x{v}" for k, v in player.inventory.items() if v > 0]
    if inv:
        print(f"{Fore.YELLOW} 🎒 Inventory: " + " ,".join(inv))
    else:
        print(f"{Fore.YELLOW} 🎒 Inventory: Empty")
    print("="*40 + "\n")

def combat(player,enemy):
    print(f"{Fore.RED}⚔️  {enemy.name} appears! HP: {enemy.health}, Attack: {enemy.attack}")
    while player.is_alive() and enemy.is_alive():
        action = input(f"{Fore.YELLOW}Do you want to [a]ttack, open [i]nventory or [r]un?").lower()

        if action == "a":
            dmg = player.attack_target(enemy)
            e_health = max(0,enemy.health)
            print(f"{Fore.GREEN}🗡️  You strike {enemy.name} for {dmg} damage! (Enemy HP is {e_health})")
            if enemy.is_alive():
                edmg = enemy.attack_target(player)
                p_health = max(0,player.health)
                print(f"{Fore.RED}💥 Enemy hit you by {edmg}! (Your HP is {p_health})")

        elif action == "i":
            print(f"{Fore.CYAN}📦 Inventory: ",{k:v for k,v in player.inventory.items() if v > 0})
            choice = input("Use what? Want to go [b]ack: ").title()
            if choice.lower() == "b":
                continue
            player.use_item(choice)

        elif action == "r":
            if random() > 0.5:
                print(f"{Fore.LIGHTBLACK_EX}🏃You ran out successfully")
                return True
            else:
                print(f"{Fore.RED}🏃Enemy did not let you run!")
                if enemy.is_alive():
                    edmg = enemy.attack_target(player)
                    p_health = max(0,player.health)
                    print(f"{Fore.RED}💥 Enemy hit you by {edmg}! (Your HP is {p_health})")
        else:
            print("❌ Invalid action")

    if player.is_alive():
        print(f"{Fore.GREEN}🎉 You have defeated the {enemy.name}")
        player.win += 1
        player.xp += enemy.xp_reward
        player.score += enemy.score_reward
        if enemy.loot and random() > 0.5:
            if enemy.loot == "Shield" and not player.shield_active:
                player.inventory[enemy.loot] = 1
                print(f"{Fore.CYAN}🛡️ You found {enemy.loot}!")
            elif enemy.loot == "Magic Sword" and not player.sword_active:
                player.inventory[enemy.loot] = 1
                print(f"{Fore.CYAN}🗡️ You found {enemy.loot}!")
            elif enemy.loot == "Ring Of Vitality" and not player.ring_active:
                player.inventory[enemy.loot] = 1
                print(f"{Fore.CYAN}💍 You found {enemy.loot}!")

        if player.xp >= player.level * 20 + 5:
            player.level_up()
            print(f"{Fore.GREEN}⬆️  You have leveled up! Now level {player.level}")
        return True
    else:
        print(f"{Fore.RED}💀You have been slayed by {enemy.name}\n")
        return False

def healing_fountain(player):
    if player.health < player.max_health:
        healed = player.heal()
        print(f"Fountain has healed {healed} HP : {player.health}")
    else:
        player.inventory["Potion"] += 1
        print(f"Health is already full healing fountain added a potion in inventory Potion: {player.inventory["Potion"]}")

def explore(player,steps,exit_at):
    show_hud(player)
    while True:
        print(f"{Fore.MAGENTA}Which way will you go?")
        print(f"{Fore.GREEN}[L]eft   {Fore.GREEN}[R]ight    {Fore.GREEN}[F]orward")
        dir = input(">")
        if dir.lower() in ["l","r","f"]:
            break
        else:
            print("Invalid command")
    steps +=1
    if steps == exit_at:
        print(f"{Fore.GREEN}🌟 You have successfully found the way out of dungeon! YOU WIN!")
        return steps,True,True

    event = choices(["enemy","healing_fountain","empty"],weights = [0.6,0.3,0.1],k=1)[0]
    if event == "enemy":
        print(f"{Fore.RED}👹 An enemy approaches...")
        if player.win == 0:
            enemy = Enemy("Goblin",10,3,10,10,loot = "Shield")
        elif player.win == 1:
            enemy = choice([Enemy("Goblin",10,3,10,10,loot = "Shield"),
                           Enemy("Skeleton",15,4,15,15,loot = "Magic Sword")])
        else:
            enemy = choice([Enemy("Goblin",10,3,10,10,loot = "Shield"),
                           Enemy("Skeleton",15,4,15,15,loot = "Magic Sword"),
                           Enemy("Dragon",25,6,30,30,loot = "Ring Of Vitality")])
        alive = combat(player,enemy)
        return steps,False,alive
    elif event == "healing_fountain":
        print(f"{Fore.BLUE} 💧You found an healing fountain")
        healing_fountain(player)
    else:
        print(f"{Fore.WHITE} ...The room is empty.Nothing happens.")

    return steps,False, True


if __name__ == "__main__":
    main()




