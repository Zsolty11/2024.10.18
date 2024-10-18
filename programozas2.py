import random
kor = 0
class Warrior:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def Attack(self, other_warrior):
        self.health -= other_warrior.attack_power
    
    def is_alive(self):
        if self.health > 0 :
            return True
        else:
            return False
    def defending(self,other_warrior):
        a = random.choice([True,False])
        if a == True:
            other_warrior.attack_power / 2
    def spec_kepesseg(self,):
        a = random.choice([True,False])
        if a == True:
            self.attack_power * 2
    def tuzgolyo(self,other_warrior):
        a = random.choice([True,False])
        if a == True:
            print('Képesség elhasználva')
            other_warrior.health -= 20
            
    def villamcsapas2(self,other_warrior):
        a = random.choice([True,False])
        if a == True:
            print('Képesség elhasználva')
            other_warrior.health -= 30    
        
        
hos1 = Warrior("Warrior1",100, random.randint(1,50))
hos2 = Warrior("Warrior2",100, random.randint(1,50))

print(hos1.name,hos1.health,hos1.attack_power)
print(hos2.name,hos2.health,hos2.attack_power)

while hos1.is_alive() and hos2.is_alive():
    kor += 1
    hos2.defending(hos1)
    hos1.spec_kepesseg()
    hos1.tuzgolyo(hos2)
    hos1.Attack(hos2)
    print(f"{hos1.name} is attacking.")
    print(f'{hos2.name}has {hos2.health} hp')
    hos1.defending(hos2)
    hos2.spec_kepesseg()
    hos2.villamcsapas2(hos1)
    hos2.Attack(hos1)
    print(f"{hos2.name} is attacking.")
    print(f'{hos1.name} has {hos1.health} hp')
    kor += 1 
print(kor)    
        
    
    
