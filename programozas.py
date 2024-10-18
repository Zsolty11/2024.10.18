import math
'''
db = 0
while True:
    try:
        db = int(input("Hány állatot szeretnél hozzáadni?"))
    except ValueError:
        print("Érvénytelen formátum.")
    else:
        break
allatok = []
szam = 1
for allat in range(db):
    allat = input(f"Add meg az {szam} állat nevét: ")
    while True:
        try:
            pont = int(input(f"Add meg {allat} pontszámát: "))
            allatok.append((allat,pont))
            szam +=1
        except ValueError:
            print("Érvénytelen formátum.")
        else:
            break
valasztas = input("Szeretnéd látni az összes állatot? (igen/nem): ")
if valasztas == 'igen':
    print(allatok)
    
atlag = 0
for szam2 in allatok:
    atlag += szam2[1]

valasztas1 = input("Szeretnéd tudni az átlagos pontszámot? (igen/nem): ")
if valasztas1 == 'igen':
    print(f"Az átlagos pontszam: {atlag/len(allatok)}")
    
    

szam = int(input('Adj meg egy számot: '))
szam2 = int(input('Add meg a másik feladatot: '))

try:
    print(szam2 // szam)
except:
    print("Nullával nem lehet osztani")
    


szam3 = int(input('Adjon meg egy számot amelynek tudni szeretnéd a négyzetgyökét?'))
try:
    print(szam3**0.5)
except :
    print('Helytelen adattípus')
    


try:
    megnyit = open(alma.txt)
except:
    print("A fájl nem létezik.")
    


lista = [1,23,3,4,5,6,7,78,8]
inde = int(input('Adj megy egy indexet: '))
try:
    print(lista[inde])
except:
    print('Az index a listán kívül esik') '''
''' 1, feladat						'''
class Dog:
    def __init__(self,nev,kor):
        self.nev = nev
        self.kor = kor
    def display_info(self):
        print(self.nev)
        print(self.kor)
        
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

dog1.display_info()
dog2.display_info()


''' 2, feladat						'''

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,a):
        self.balance += a
    def withdraw(self,b):
        self.balance -= b
    def get_balance(self):
        print(self.name)
        print(self.balance)

nber = BankAccount('Péter',2000)
nber2 = BankAccount('Béla', 1000)

nber.deposit(1000)
nber2.withdraw(100)

nber.get_balance()
nber2.get_balance()

''' 3, feladat					'''

class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    def add_grade(self,jegy):
        self.grades.append(jegy)
        
    def get_average(self):
        a = sum(self.grades)
        b = len(self.grades)
        print(self.name , a/b)

bela = Student('Béla',[1,2,3,4])
peti = Student('Péter',[5,5,5,5])
anna = Student('Péter',[1,1,1,1,1,1])


bela.add_grade(3)
anna.add_grade(1)
peti.add_grade(4)

bela.get_average()
peti.get_average()
anna.get_average()        






