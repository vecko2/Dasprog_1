#!!!! BUKTIKAN JUMLAH TOTAL SISWA, JUMLAH KELOMPOK YANG TERBENTUK, & SISA SISWA YANG TIDAK MENDAPAT KELOMPOK !!!!

#step 1
total_siswa = int(input("berapa jumlah total siswa: "))
kuota_kelompok = 30

#step 2
siswa_berkelompok = total_siswa // kuota_kelompok
sisa = total_siswa % kuota_kelompok

#step 3
print(f"Total Jumlah Siswa: {total_siswa}. \nJumlah Kelompok Yang Terbentuk: {siswa_berkelompok}. \nSisa Siswa Yang Tidak Mendapat Kelompok: {sisa}")