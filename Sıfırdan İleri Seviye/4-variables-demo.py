"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
    Müşteri Adı
    Müşteri Soyadı
    Müşteri Ad+Soyad
    Müşteri Cinsiyet
    Müşteri TC
    Müşteri Doğum Yılı
    Müşteri Adres
    Müşteri Yaş
"""
musteriAdi= 'Ali'
musteriSoyadi = 'Pak'
musteriAdSoyad = musteriAdi + ' ' +musteriSoyadi
musteriCinsiyet = True #Erkek
musteriTC = '12345678910'
musteriDogumYili = 1997
musteriAdresi = 'Bağcılar İstanbul'
musteriYasi = 2024 - musteriDogumYili

print("Müşteri Ad - Soyad:",musteriAdSoyad)
print("Müşteri Yaşı:",musteriYasi)
print("Müşteri Tc No:",musteriTC)
print("Müşteri Adresi:",musteriAdresi)

"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    Sipariş1 => 110
    Sipariş2 => 1110.5
    Sipariş3 => 356.95
"""
order1 = 110
order2 = 1110.5
order3 = 356.95
sum = order1+order2+order3
print("Sum:",sum)