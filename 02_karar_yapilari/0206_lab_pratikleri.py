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
""""""
biletFiyatı = float(input('lütfen bilet fiyatını giriniz: '))
bavulAgirligi = float(input('lütfen bavul ağırlığını giriniz: '))
ekUcret = 0
if bavulAgirligi > 15 :
    ekUcret = (bavulAgirligi-15)*5
print(f'toplam ücret: {(biletFiyatı) + (biletFiyatı*1.8) + (ekUcret)}')
print(f'kdv ücreti: {biletFiyatı*1.8}')
print(f'ekstra bagaj ücreti: {ekUcret}')
