print("================= BARIS ARITMATIKA ==================")
def aritmatika(awal, bilangan, suku):
    bedaselisih = bilangan - awal
    banyaksuku = awal + (suku - 1)* bilangan
    tl = (suku / 2 ) * (awal + banyaksuku)
    return tl
awal = int(input("Masukkan bilangan awal : "))
bilangan = int(input("Masukkan selisih bilangan : "))
suku = int(input("Masukkan banyakny suku : "))
tl = aritmatika(awal, bilangan, suku)
print("Total dari deret aritmatika tersebut adalah:", tl)