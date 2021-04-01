#region ornek_1
"""
n1, n2 = int(input("lütfen 1. sınav notunu giriniz: ")), int(input("lütfen 2. sınav notunu giriniz: "))
ort = (n1+n2)/2
if ort>=85:
    print(f"yıl sonu notunuz {ort} tur. Üstün başarı sağladınız. Tebrikler!")
elif ort>=75:
    print(f"yıl sonu notunuz {ort} tur. Başarılısınız:)")
elif ort>=55:
    print(f"yıl sonu notunuz {ort} tur. Daha fazla çalışarak daha başarılı olabirirsiniz:)")
else:
    print(f"yıl sonu notunuz {ort} tur. Dersten kaldınız seneye daha fazla çalışın. Başarabilirsiniz:)")

"""
#endregion

#region ornek_2
"""
3 sayının sıralamasını yapma #doğru çalışmıyor bu kod
"""
"""
s1 = int(input("1. sayıyı giriniz : "))  #doğru çalışmadı bu kod!!!!!
s2 = int(input("2. sayıyı giriniz : "))
s3 = int(input("3. sayıyı giriniz : "))
if s1<s2:
    s1, s2 = s2, s3     #yer değişikliği yaptım
if s1<s3:
    s1, s3 = s3, s1
if s2<s3:
    s2, s3 = s3, s2
print(f"{s1}>{s2}>{s3}")
"""
#endregion

#region ornek_3
"""
a = int(input("a kenarını girin : "))
b = int(input("b kenarını girin : "))
if a==b:
    print(f"karenin alanı {a*b} dir.")
else:
    print(f"dikdörtgenin alanı {a*b} dir.")
"""
#endregion

#region ornek_4
"""
kısaKenar = int(input("lütfen kısa kenarı girin : "))
uzunKenar = int(input("lütfen uzun kenarı girin : "))
if kısaKenar>uzunKenar:
    print("kısa kenar uzun girilemez")   #uyarı yaptık
else:
    print(f"dörtgenin çevresi {2*(kısaKenar+uzunKenar)}")
"""
#endregion




