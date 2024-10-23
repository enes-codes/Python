"""
    * Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r: 3.14)
"""
pi = 3.14
r = float(input("Yarı Çapı Giriniz: "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

print("Alan: ", alan)
print("Çevre: ",cevre)