# region ornek_1
"""
delta örneği
"""
a = 1
b = 4
c = 2
delta = b**2 - 4*a*c
print("delta değeri", delta, "dir.")
# endregion

# region ornek_2
"""
ortalama
"""
a = 2
b = 4
ort = (a+b)/2
print("ortalama değeri", ort)
# endregion

# region ornek_3
"""
saat bilgisini saniyeye dönüştürsün
"""
"""
saat = 5
saniye = 3600
print("saat:", saat)
print("ekrandaki saatin saniye karşılığı", saat*saniye, "sn")
"""
# endregion

# region ipucu→ formatter shift + alt + f → bitişik yerleri ayırıyor daha okunabilir kodumuz oluyor

s = 10
x = 19
toplam = s+x
# endregion

# region ornek_4
""""""
sayi = 562
kalan = sayi % 10
birler = kalan // 1
print(birler)
kalan = sayi % 100
onlar = kalan // 10
print(onlar)
kalan = sayi % 1000
yüzler = kalan // 100
print(yüzler)
toplamDegeri = birler + onlar + yüzler
# print(yüzler, onlar, birler)
print(sayi, "sayısının basamakları toplamı:", toplamDegeri, "tür.")

# endregion
