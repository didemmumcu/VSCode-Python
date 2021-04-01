#region ilk_giris
#variable - değişkenler
"""
skor = 12
print(skor)

name = "mehmet"
print(name)
"""
#endregion

#region notation
"""
#camel casing
okulNumarasi = 571 #ilk karakter küçük ikinci karakter büyük harfle başlar 
ad = "didem"
soyad = "mumcu"
sinavNotu = 99
print(okulNumarasi, ad, soyad, sinavNotu)
"""
"""
#undercore casing 
okul_numarasi = 571 #alttire kullanılır
ad = "didem"
soyad = "mumcu"
sinav_notu = 100
print(okul_numarasi, ad, soyad, sinav_notu)
"""
#endregion

#region değisken-isimlendirme_kurallari
"""
Değişken isimlendirme Kuralları
1- harf veya alt çizgi ile başlanmalıdır.
2- rakamla başlanmaz
3- illk harf dışındakiler , harf, sayı, alt çizgi kullanılabilir
4- alt çizgi dışında alfa sayısal karakterlerimiz (%, #, $...) kullanılamaz
5- case sensitive
6- anahtar kelimeler if, pass, while, def bunlar kullanılamaz
7- türkçe karakter kullanmamaya özen gösterelim
"""


#1- harf veya alt çizgi ile başlanmalıdır
"""
okul = "gaziantep üni" #doğru
birinci = "adana" #doğru
_birinci = "adana" #doğru
1inci = "adana" #yanlış
"""


#2- rakamla başlanmaz
"""
_34istanbul = "en güzel şehir" #rakamla başlamamak için alttire kullanabilirsin
"""


#3- illk harf dışındakiler , harf, sayı, alt çizgi kullanılabilir
"""
plaka34 = "ist"
"""


#4- alt çizgi dışında alfa sayısal karakterlerimiz (%, #, $...) kullanılamaz
"""
plaka&34 = "ist" #yanlış
"""

#5- case sensitive
"""
ad = "ali"
print(Ali) #hata verir değişken tanımlanmamış diye
"""

#6- değişken adı yerine anahtar kelimeler if, pass, while, def, for bunlar kullanılamaz
"""
def = "definition" #yanlış
"""

#7- türkçe karakter kullanmamaya özen gösterelim
"""
öğrenci = "ali"
ogrenci = "ezgi"
print(ogrenci) öğrenci ogrenci
"""
#endregion

