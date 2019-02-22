class Player:
    def __init__(self, gold_coins, health, lives):
        self.gold_coins = gold_coins
        self.health = health
        self.lives = lives

    def __str__(self):
        return "{} has {} health points and {} gold coins".format(self.gold_coins, self.health, self.lives)

    def level_up(self):
        self.lives += 1

    def collect_treasure(self, gold_coins, level_up):
        if gold_coins % 10 == 0:
            level_up()
        else:
            self.gold_coins += 1

    def do_battle(self, damage, restart):
        self.health -= damage
        if self.lives == 0:
            restart()
        elif self.health < 0:
            self.lives -= 1
            self.health = 10

    def restart(self):
        self.coins = 0
        self.health = 10
        self.lives = 5
