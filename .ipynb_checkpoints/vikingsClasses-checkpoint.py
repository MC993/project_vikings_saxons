import random

# Soldier Class
class Soldier:
    def __init__(self, health, strength):
        self.health = health #attribute health
        self.strength = strength #attribute strength
    
    def attack(self):
        return self.strength #function to attack

    def receiveDamage(self, damage): #function to receive damage
        self.health -= damage
        if self.health <= 0:
            return None
        return None

# Viking Class
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def battleCry(self):
        return "Odin Owns You All!" #function to call the battle cry
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        return f"{self.name} has received {damage} points of damage"

# Saxon Class
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has died in combat"
        return f"A Saxon has received {damage} points of damage"

# War Class
class War:
    def __init__(self):
        self.vikingArmy = [] #list to contain the viking army
        self.saxonArmy = [] #list to contain the saxons army

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if len(self.saxonArmy) == 0:
            return "No Saxons left to attack."
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = viking.attack()
        result = saxon.receiveDamage(damage)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result

    def saxonAttack(self):
        if len(self.vikingArmy) == 0:
            return "No Vikings left to attack."
        if len(self.saxonArmy) == 0:
            return "No Saxons left to attack."
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = saxon.attack()
        result = viking.receiveDamage(damage)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."
