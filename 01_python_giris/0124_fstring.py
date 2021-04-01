#output anında csting - dönüşüm ile ilgili efor harcamamak için format yöntemleri kullanırız

#region format
#ekrana output formatlarken ilk yöntem → format
"""

rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print("girgiğiniz rakamın bir fazlası {}".format(rakam + 1))
print("girdiğiniz {} rakamının bir fazlası {} dir".format(rakam, (rakam + 1)))
"""
"""
a= int(input("1. a değerini giriniz: "))
b= int(input("1. b değerini giriniz: "))
print("{} değeri ile, {} değerinin toplamı {} dur.".format(a, b, (a+b)))
"""
#endregion

#region fstring
#ekrana output formatlarken ilk yöntem → fstring
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print(f"girdiginiz {rakam} rakamının bir fazlası {rakam+1}")
"""
"""
a= int(input("1. a değerini giriniz: "))
b= int(input("1. b değerini giriniz: "))
print(f"{a} değeri ile, {b} değerinin toplamı {a+b}")
"""
"""
s1=int(input("1. s. g. : "))
s2=int(input("1. s. g. : "))
print(f"girdiginiz sayıların toplamı {s1+s2}")
"""
#endregion

#region ornek_1
"""
a = int(input("1. kenarı giriniz : "))
b = int(input("2. kenarı giriniz : "))
alan = a*b
print(f"karenin alanı {alan} metrekaredir. ")
"""
#endregion

#region ornek_2
"""
bir üçgenin iki iç açısı verilsin 3. iç açı bulunsun
"""
"""
a = int(input("1. açıyı yazın : "))
b = int(input("2. açıyı yazın : "))
formul = 180-(a+b)
print(f"3. açımız {formul} dur")
"""
#endregion

#region ornek_3 aklını karıştırma
"""
kürenin hacmini hesaplama
"""
"""
import math #matematiksel veriler(pi sayısı gibi), yazılırken önemseme amaçlı
radius=int(input("Please enter the radius of the sphere : "))
volume=(4/3)*math.pi*math.pow(radius,3) 
print(f"Volume of a sphere with radius:{volume}")
"""
#endregion 

#region ornek_3
"""
yetişkin bileti 8 tl , öğrenci bileti 5 tl , yaşlı bileeti 6tl
fiyatlara göre toplam bilet fiyatını hesapla
"""
"""
yetiskin = int(input("lütfen yetişkin sayısını gir: "))
ogrenci = int(input("lütfen öğrenci sayısını girin: "))
yaslı = int(input("lütfen yaşlıyı girin : "))
ucret = (8*yetiskin)+(5*ogrenci)+(6*yaslı)
print(f"toplam ücret {ucret} tir")
"""
#endregion
