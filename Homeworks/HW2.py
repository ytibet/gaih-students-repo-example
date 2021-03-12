# Yusuf Tibet'e ait ikinci gün ödevidir.
# Soru: CV uygulaması yapınız.
Ahmet= {"Adı":"Ahmet","Soyadı":"Ak", "Doğum Yeri": "Adana", "Meslek" : "Anestezi Uzmanı"}
Burcu= {"Adı":"Burcu", "Soyadı":"Beyaz", "Doğum Yeri": "Bursa", "Meslek" : "Bilgisayar Mühendisi"}
Cemil= {"Adı":"Cemil", "Soyadı":"Ceylan", "Doğum Yeri": "Çorum", "Meslek" : "İşletme Mezunu"}
Didem={"Adı":"Didem", "Soyadı":"Dağ", "Doğum Yeri": "Denizli", "Meslek" : "Doktor"}
Emre= {"Adı":"Emre", "Soyadı":"Erik", "Doğum Yeri": "Edirne", "Meslek" : "Endüstri Mühendisi"}
print ("Mevcut CV'ler :","------------", sep="\n")
for i in Ahmet:
    no=Ahmet[i]
    print(i+":"+" " +no)
print("---------------")
for i in Burcu:
    no=Burcu[i]
    print(i+":"+" " +no)
print("---------------")
for i in Cemil:
    no=Cemil[i]
    print(i+":"+" " +no)
print("---------------")
for i in Didem:
    no=Didem[i]
    print(i+":"+" " +no)
print("---------------")
for i in Emre:
    no=Emre[i]
    print(i+":"+" " +no)
print("---------------")
