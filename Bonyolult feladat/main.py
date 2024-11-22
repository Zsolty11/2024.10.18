from harcos import Harcos,Ellenseg
from bonyolult import beolvas

adat = beolvas("harcosok.json")
harcosok = []
for  harcos in adat["harcosok"]:
    harcosok.append(Harcos(harcos["nev"], harcos["hp"], harcos["inventory"]))

ellensegek = []
for  ellenseg in adat["ellensegek"]:
    ellensegek.append(Ellenseg(ellenseg["nev"], ellenseg["hp"], ellenseg["loot"]))


def harc(self,):
        pass
    

print(harcosok[0])
print(ellensegek[0])