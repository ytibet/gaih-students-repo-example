# Yusuf Tibet'e ait ilk gün ödevidir.
# Soru: sayıları tek ve çift olarak ayıran ve bulundukları listenin türünü veren bir program yazınız?
sayilar=list(range(10))
print ("Sayılarımız :", sayilar)
cift=[i for i in sayilar if i %2 ==0]
tek=[i for i in sayilar if i %2 ==1]
print("Çift sayılar :", cift)
print("Tek sayılar :", tek)
print("Çift sayılar veri türünüz :", type(cift))
print("Tek sayılar veri türünüz :", type(tek))
