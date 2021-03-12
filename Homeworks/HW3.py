print("Öğrencilerinizin notlarını giriniz.")
sinif=[
    ["Ahmet","Ak",],["Burcu", "Beyaz"],["Cemil", "Ceylan"], ["Didem", "Dağ"], ["Emre", "Erik"]]
m= 0
ekli=[]
ogrenci=[]
while m  <=4:
    print(sinif[m] , "-----------", sep="\n")
    vize = int(input("Vize notu: "))
    final = int(input("Final notu: "))
    proje = int(input("Proje notu: "))
    notu = vize * 0.30 + final * 0.40 + proje * 0.30
    ogrenci = {"Adı":sinif[m], "Vize notu": vize, "Final notu" : final,"Proje notu": proje, "geçme notu" : notu }
    print (ogrenci)
    ekli.append(ogrenci)
    m +=1
print(ekli)
