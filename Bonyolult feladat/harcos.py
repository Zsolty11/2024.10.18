class Harcos:
    def __init__(self, nev, hp, inventory=None):
        self.nev = nev
        self.hp = hp
        self.inventory = inventory
        
    def __str__(self):
        return self.nev
        
    def __add__(self, masik):
        return self.hp + masik




class Ellenseg:
    def __init__(self, nev, hp, loot=None):
        self.nev = nev
        self.hp = hp
        self.loot = loot
        
        
    def __str__(self):
        return self.nev

                
