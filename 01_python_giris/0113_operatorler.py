#region aritmetik
#aritmetik operatörler
"""
1→ +   toplama
2→ -   çıkarma
3→ *   çarpma
4→ /   bölme
5→ // tam bölme
6→ ** üst alma
7→ % mod alma
"""
#endregion

#region +/-  → unary-işaretler  (binary toplama çıkarmadır)
"""
print(3+3)
print(6-3)
print(3-6)
print(0.15-15)
print(.15-15)
"""
#endregion

#region */
"""
print(4*4)
print(.4*4)
print(type(.4*4))
print(9/3)
print(9/2)
print(type(9/3)) #bölmeleri float olarak çıktı yapar
print(10/0)  #0a bölmek mümkün değil
"""

#endregion

#region **
"""
print(4**4)
print(2**4)
print(16**0.5)
print(16**(1/2))
"""
#endregion

#region // → tam bölme
"""
print(12/7)
print(12//7)
print(12//7.)
print(-13//5) #tam bölme bir küçüğğüne yuvarlar*****
"""

#endregion

#region % → mod alma - kalanı bulma
"""
print(10%4)
print(3%2)
print(7%4)
"""
#endregion

#region operator_oncelikleri
"""
1  +,-  unary
2  **   üst alma
3  *, /, %  çarpma bölme mod alma
4  +, -      toplama çıkarma
"""
print(3+4*5)
print(15%4*2)
print(15%4%2)
print(2**2**3)
#endregion
