#region-karsilastirma_operatorleri_giris
"""
karşılaştırma operatörleri
1→ == eşittir
2→ != eşit değildir
3→ <  küçüktür
4→ >  büyüktür
5→ <= küçük eşittir
6→ >= büyük eşittir
"""
#endregion


#region == 
"""
print(10==10)
print(-5==-5)
print(10==5)
"""
"""
print("istanbul" == "istanbul")  #stringlerde de true false yapılır
print("İstanul" == "istanbul")   #case sensitive önemli
print("meb" == "MEB")
"""
"""
print(" " == " ")  #boşluk ta bir karakter olduğundan true der
"""
"""
print(10 = 10)   #karşılaştırmada tek eşittir yanlıştır
"""


#region !=
"""
print(10 != 10)
print(10 != 5)
print("meb" != "MEB")
"""
#endregion


#region <
"""
print(10<20)
print(10 < 10)
print(20 < 10)
print(5<9)
"""
#endregion

#region >
"""
print(10>20)
print(10>10)
print(20>10)
"""
#endregion

#region <=
"""
print(10<=20)
print(10<=10)
print(20<=10)
"""
#endregion

#region >=
"""
print(10>=20)
print(10>=10)
print(20>=10)
"""
#endregion


#region ornek_1
"""
ogrenciYas = int(input("lütfen ogrencinin yaşını giriniz: "))
print(ogrenciYas >= 18)
"""

#endregion 

#region ornek_2
"""
kullanıcı adını giriniz : admin     →true
kullanıcı adını giriniz : user      →false
"""
"""
uName = input("lütfen kullanıcı adını giriniz : ")
print(uName=="admin")
"""
#endregion