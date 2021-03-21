#region tip_donusumu
"""
dTarihi = int(input("Doğum Tarihi Giriniz : "))  #ne yazarsak yazalım string çıkar ve sorun yaşarız
#dTarihi = int(dTarihi)     #stringi integer a dönüştürmek için int yazıyoruz
yas = 2021 - dTarihi
print(dTarihi, "doğum tarihli öğrencimizin yaşı", yas)
"""
#int(....), float(....) şeklinde dönüştürülür
#endregion

#region ornek
"""
a kenarı, b kenarı girilecek. dörtgen için alan hesaplanacak
int dönüşümü yapılacak
"""
"""
a = int(input("lütfen a kenarının uzunluğunu giriniz: "))
b = int(input("lütfen b kenarının uzunluğunu giriniz: "))
alan = a*b
print("dörtgenin alanı", alan, "metrekaredir.") 
"""
#print("dörtgenin alanı", a*b, "metrekare'dir") de diyebilirsin
#endregion

#region ornek_2
"""
yükseklik ve iki taban kenarı bilinen bir piramitin hacmi
"""
"""
h = int(input("yüksekliği giriniz: "))
a = int(input("a taban kenarını giriniz: "))
b = int(input("b taban kenarını giriniz: "))
hacim = 1/3*h*a*b
print("piramitin hacmi", hacim, "metre küptür.")
"""
#endregion