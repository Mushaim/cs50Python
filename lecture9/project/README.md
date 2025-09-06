# Dungeon Escape
#### Video Demo: https://youtu.be/559n04aLP6E
#### Description:
Dungeon Escape is a text-based role-playing adventure game written in Python. The player takes on the role of a hero trapped inside a dungeon and must explore different rooms in search of the exit. At every step, the player chooses a direction to move — left, right, or forward — and the game randomly generates an event. These events may include facing an enemy, discovering a healing fountain, or entering an empty room. The balance of chance makes each run unique and unpredictable.

When encountering enemies, the game switches into a combat system. Combat is turn-based: the player can choose to attack, access the inventory to use items, or attempt to flee. Enemies fight back, reducing the hero’s health, so strategy and resource management are essential. Defeating enemies rewards the player with score points, experience, and loot. Loot items such as shields, magic swords, rings of vitality, and potions enhance the player’s abilities and can be stored in the inventory for later use. Collecting these items not only makes survival easier but also adds progression and variety to the gameplay.

As the hero gains experience from combat, they level up, increasing maximum health and attack power. Healing fountains provide opportunities to restore health or earn potions if already at full strength. The dungeon exit is hidden after a random number of steps, ensuring that players cannot predict the game’s length, further enhancing replayability.

The game ends in two possible ways: if the hero discovers the dungeon’s exit, they win and escape with their final score; if their health reaches zero, they lose and the game ends with a "Game Over" screen. The interface makes use of Python’s `colorama` library along with emojis to add color and atmosphere, making the text-based experience feel more engaging and immersive.
