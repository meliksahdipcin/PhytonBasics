"""
Merhaba
Dünya!
"""

#Yorum satırı

"""
tamSayi = 1 #int
virgulluSayi = 1.5 #float
karakterDizisi = "1" #string
dogruYanlis = True #boolean

sayi1, sayi2, sayi3, sayi4 = (1, 2, 3, 4)

print(int(karakterDizisi) + tamSayi)

print(sayi1, sayi2, type(sayi1))

cikarma = tamSayi - virgulluSayi
carpim = tamSayi - virgulluSayi
print(type(carpim))
"""

"""
isim = "Ali"
yas = 30
cumle = "{a} {b} yaşındadır.".format(a = isim, b = yas)
print(cumle)
"""

"""
isim = "selman kahya"
print(isim.upper())
print(isim.capitalize())
"""

"""
sayilar = [1, 2, 3, 4, 5, 6]
meyveler = ["elma", "armut"]
print(sayilar[0])
print(meyveler[1])
# lenght = uzunluk -> len
print(len(sayilar))
sayilar.append(7)
print(sayilar)

meyveler.insert(0, "karpuz")
meyveler.remove("armut")
print(meyveler)
meyveler.sort()
print(meyveler)
meyveler.sort(reverse = True)
print(meyveler)
"""

"""
insan ={
    "ilkIsim" : "Selman"
    "soyIsım" : "Kahya"
    "yas" : 30
        }

print(insan["ilkIsim"])
print(insan.get("ilkIsim"))
delete(insan["yas"])
print(insan)
"""

"""
def toplam(sayi1, sayi2):
    return sayi1 + sayi2

sonuc = toplam(1, 3)
print(sonuc)
"""

"""
x  = 10

if x > 20:
    print("x 20'den büyüktür.")

elif x == 20:
    print("x 20'ye eşittir.")

else:
    print("x 20'den küçüktür.")
"""

"""
x = 20

if x == 20 or x < 20:
    print("x 20'ye küçük eşittir.")
"""

"""
sayilar = [1, 2, 3]
aradigimSayi = 4
print(aradigimSayi in sayilar)
if aradigimSayi in sayilar:
    print("Aradığım sayı, sayı dizisinin içindedir.")
"""

"""
baslangic = 3
while baslangic != 0:
    baslangic = baslangic - 1
    print(baslangic)
"""

"""
class Kullanici:
    
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        
    def selamla(self):
        print("Ooo hoşgeldin! Benim adım {isim}".format(isim = self.isim))
        
kullanici1 = Kullanici("Selman", 30)
kullanici1.selamla()
#print(kullanici1.isim)

class Musteri(Kullanici):
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        self.bakiye = 0
        
    def bakiyemiSorgula(self):
        return self.bakiye
    
    def bakiyemiArttır(self):
        self.bakiye += 10
        
musteri1 = Musteri("Selman", 30)
print(musteri1.bakiyemiSorgula())
"""