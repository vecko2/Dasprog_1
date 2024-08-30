#!!!! BUKTIKAN JUMLAH BTU PANAS YANG DISALURKAN KE RUMAH !!!!
#galon = 100

#Diketahui:
energi_barel = 5800000
galon_perbarel = 42 
efisiensi = 0.65

#step 1
galon = int(input("berapa jumlah galon "))
jumlah_barel = galon / galon_perbarel

#syep 2
energi = jumlah_barel * energi_barel
energi_akhir = energi * efisiensi

#step 3
print(f"besar efisiensi: {efisiensi} = 65%")
print(f"jumlah BTU panas yang disalurkan ke rumah: {energi_akhir:.2f} BTU")