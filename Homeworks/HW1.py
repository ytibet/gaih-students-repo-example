# Yusuf Tibet'e ait ilk gün ödevidir.
# Soru: sayıları tek ve çift olarak ayıran ve bulundukları listenin türünü veren bir program yazınız?
sayilar=list(range(10))
print ("Sayılarımız :", sayilar)
cift=[i for i in sayilar if i %2 ==0]
tek=[i for i in sayilar if i %2 ==1]
birlesme=[]
birlesme.extend(cift)
birlesme.extend(tek)
carpim=[i*2 for i in birlesme]
print("Birleşik Liste :", carpim)
print("Sayılar veri türünüz :", type(carpim))
