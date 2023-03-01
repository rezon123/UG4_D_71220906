def kata_terpanjang(kl): #kl artinya kalimat
    perkata = kl.split()
    palingpanjang= max(len(i) for i in perkata)
    kataterpanjang = [i for i in perkata if len(i) == palingpanjang]
    return kataterpanjang[0]
kl = input("Masukkan sebuah kalimat: ")
tp = kata_terpanjang(kl) #tp artinya terpanjang
print("Kata terpanjang dalam kalimat tersebut adalah:", tp)