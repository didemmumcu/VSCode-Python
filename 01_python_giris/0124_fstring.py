#output anında csting - dönüşüm ile ilgili efor harcamamak için format yöntemleri kullanırız

#region format
#ekrana output formatlarken ilk yöntem → format
"""

rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print("girgiğiniz rakamın bir fazlası {}".format(rakam + 1))
print("girdiğiniz {} rakamının bir fazlası {}".format(rakam, (rakam + 1)))
"""
"""
a= int(input("1. a değerini giriniz: "))
b= int(input("1. b değerini giriniz: "))
print("{} değeri ile, {} değerinin toplamı {}".format(a, b, (a+b)))
#endregion
"""
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