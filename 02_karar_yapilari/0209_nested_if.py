#nested if - iç içe if demektir

#region   ornek_1
"""
havaYagıslıMı = True
havaSogukMu = True
#print("x")   →    hoca buraya print atadı
if havaYagıslıMı == True:
    if havaSogukMu == True:
        print("kazak giy şemsiye al")
    else:
        print("tişört giy şapka al")
else:
    print("şapka al kazak giy")
#print("y")   →    hoca buraya print atadı
"""
#endregion

#region  ornek_2
"""
+  kullanıcı değer girecek
+  int dönüşümü yapılacak
+  kullanıcı 0 ya da negatif değer girmemeli
+  0-100 arası ya da 100+ olup olmadığını bulan program
+  ekrana kullanıcı dostu çıktı verecek
"""
"""
a = int(input("lütfen sayı giriniz : "))
if a>0:
    if a>100:
        print(f"{a} değeri 100 üstüdür.")
    if a<100:
        print(f"{a} değeri 100 den küçüktür.")
    if a==100:
        print("Girilen değer 100 e eşittir.")
else:
    print("lütfen 0 ya da negatif değer girmeyin!")
"""
#endregion

