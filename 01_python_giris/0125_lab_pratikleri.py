print("""
    Leylek Uygulamasına Hoşgeldiniz:)
    Sürüş Ücreti → 0.59/dk)
""")
s = int(input("sürüş için geçen süre (saat)\t : "))
d = int(input("sürüş için geçen süre (dakika)\t : "))
toplamDakika = s*60
toplamDakika += d
toplamTutar = 0.59*toplamDakika
print(f"sürüş için geçen süre (saat)\t: {s}")
print(f"sürüş için geçen süre (dakika)\t: {d}")
print(f"sürüşün toplam süresi {s}:{d} - {toplamDakika} dakikada bitmiştir")
print(f"kartınızdan çekilen toplam tutar {round(toplamTutar,2)}")
