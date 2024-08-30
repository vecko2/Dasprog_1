#!!!! BUATLAH KONSEP UNTUK MENGUKUR KECEPATAN MEMOTONG RUMPUT !!!!

#step 1
panjang_lahan = int(input("berapa panjang lahan: "))
lebar_lahan = int(input("berapa lebar lahan: "))

#step 2
panjang_rumah = int(input("berapa panjang rumah: "))
lebar_rumah = int(input("berapa lebar rumah: "))

#step 3
luas_lahan = panjang_lahan * lebar_lahan
luas_rumah = panjang_rumah * lebar_rumah
luas_rumput = luas_lahan - luas_rumah

#step 4
waktu_memotong = luas_rumput / 2

#step 5
print(f"lama waktu untuk memotong rumput adalah {waktu_memotong} detik")