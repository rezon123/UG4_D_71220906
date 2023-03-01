bg = input("Masukkan sekumpulan bilangan (pisahkan dengan koma): ") #bg artinya bilangan
bg = list(map(int, bg.split(','))) 
palingbesar = max(bg, key=lambda x: x)
palingkecil = min(bg, key=lambda x: x)
print("Bilangan terbesar dari kumpulan bilangan yang di input adalah :", palingbesar)
print("Bilangan terkecil dari kumpulan bilangan yang di input adalah :", palingkecil)