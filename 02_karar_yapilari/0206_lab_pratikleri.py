#region ornek_1
"""
bavulAgirligi = 16
biletFiyat = float(input("lütfen bilet fiyatını giriniz: "))
if bavulAgirligi>15:
    fark = bavulAgirligi - 15
    biletFiyat += fark*5
print(f"güncel bilet fiyatı {round(biletFiyat*1.18, 2)} TL.")
"""

#endregion

#region ornek_2
"""
biletFiyatı = float(input('lütfen bilet fiyatını giriniz: '))
bavulAgirligi = float(input('lütfen bavul ağırlığını giriniz: '))
ekUcret = 0
if bavulAgirligi > 15 :
    ekUcret = (bavulAgirligi-15)*5
print(f'toplam ücret: {(biletFiyatı) + (biletFiyatı*1.8) + (ekUcret)}')
print(f'kdv ücreti: {biletFiyatı*1.8}')
print(f'ekstra bagaj ücreti: {ekUcret}')
"""
#endregion


#region ornek_3
"""
klavyeden sayı girilsin mutlak değeri alınsın
"""
"""
sayi = int(input("lütfen sayi giriniz:"))
if sayi<0:
    sayi *= -1
print(f"sayının mutlak değeri {sayi}")
"""
#endregion

#region ornek_4
"""
bakiye var eft yapmak istiyor ama aynı bankada farklı fiyat farklı bankada farklı fiyat
"""
"""
bakiye = 5000
bankaKodu = 101
eftBankaKodu = 102 #bankalar farklı 
kesinti = 0
transfer = float(input("lütfen eft tutarını giriniz: "))
if bankaKodu != eftBankaKodu:  #para gönderdiğimiz banka farklıysa
    kesinti = transfer*0.05
print(f"güncel bakiyeniz {bakiye - transfer - kesinti} TL.")
"""
#endregion

#region ornek_5
"""
klavyeden 3 sayı girildiğinde en büyük olanını çıkaracak
"""
"""
eb = 0
a = int(input("lütfen sayı giriniz: "))
if a>0:
    eb = a
b= int(input("lütfen sayı giriniz: "))
if b>0:
    eb = b
c= int(input("lütfen sayı giriniz: "))
if c>0:
    eb = c
print(f"girilen en büyük sayı {eb}")
"""
#endregion

#region ornek_6
"""
2 sayının büyük olanını bulma
"""
"""
s1 = int(input("lütfen 1. sayıyı giriniz : "))
s2 = int(input("lütfen 2. sayıyı giriniz : "))
if s1>s2:
    print(f"en büyük sayı {s1} dir.")
if s2>s1:
    print(f"en büyük sayı {s2} dir")
"""

#endregion

#region ornek_7
"""
ortalama hesaplama
"""
"""
s1 = int(input("lütfen 1. sayı giriniz : "))
s2 = int(input("lütfen 2. sayı giriniz : "))
s3 = int(input("lütfen 3. sayı giriniz : "))
ort = (s1+s2+s3) / 3
if ort>=50:
    print(f"geçtiniz, ortalamanız {ort}")
if ort<50:
    print("dersten kaldınız:(")
"""
#endregion


