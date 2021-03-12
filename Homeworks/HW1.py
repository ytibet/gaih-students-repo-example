# Yusuf Tibet'e ait ilk gün ödevidir.
# Soru: sayıları tek ve çift olarak ayıran ve bulundukları listenin türünü veren bir program yazınız?
import random
rnd=list(range(100))
sayilar=random.sample(rnd,20)
sayilar.sort()
print ("Sayılarımız :", sayilar)
cift=[i for i in sayilar if i %2 ==0]
tek=[i for i in sayilar if i %2 ==1]
birlesme=[]
birlesme.extend(cift)
birlesme.extend(tek)
birlesme.sort()
carpim=[i*2 for i in birlesme]
print("Tek Sayılar :", tek)
print("Çift Sayılar: ", cift)
print("Birleşik Liste :", carpim)
print("Sayılar veri türünüz :", type(carpim))
