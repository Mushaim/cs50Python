from project import combat,explore,healing_fountain
from player import Player
from enemy import Enemy
from unittest.mock import patch


def test_combat_win():
    player = Player("MK")
    enemy = Enemy("Goblin",10,3,10,10,loot = "shield")
    with patch("builtins.input", return_value = "a"):
        result = combat(player,enemy)
    assert result is True
    assert player.is_alive()

def test_combat_run():
    player = Player("MK")
    enemy = Enemy("Goblin",10,3,10,10,loot = "shield")
    with patch("builtins.input", return_value = "r"):
        result = combat(player,enemy)
    assert result is True
    assert player.is_alive()

def test_combat_death():
    player = Player("MK")
    player.health = 3
    enemy = Enemy("Dragon",25,6,30,30,loot = "Ring Of Vitality")
    with patch("builtins.input", return_value = "a"):
        result = combat(player,enemy)
    assert result is False
    assert player.is_alive() == False

def test_explore_exit():
    player = Player("MK")
    steps = 4
    end_at = 5
    with patch("builtins.input", return_value = "r"):
        steps,won,alive = explore(player,steps,end_at)
    assert won is True
    assert alive is True

def test_explore_enemy():
    player = Player("MK")
    steps = 0
    end_at = 5
    inputs = iter(["l","a"])
    with patch("builtins.input", lambda _:next(inputs)):
        with patch("random.choices", lambda *args, **kwargs: ["enemy"]):
            with patch("project.combat", lambda p, e: True):
                steps,won,alive = explore(player,steps,end_at)
    assert steps == 1
    assert alive in [True,False]

def test_healing_fountain():
    player = Player("MK")
    player.health = 5
    healing_fountain(player)
    assert player.health == player.max_health
