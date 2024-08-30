#!!!! BUKTIKAN KECEPATAN INFUSNYA 300 ML/HR !!!!
#VTBI = 100 ml
#menit infus = 20

#step 1
VTBI = int(input("volume penginfusan (VTBI): "))
lama_infus = int(input("menit penginfusan: "))

#step 2
kecepatan_infus = (VTBI / lama_infus) * 60

#step 3
print (f"kecepatan penginfusannya adalah {kecepatan_infus} ml/hr. \nDan VTBInya adalah {VTBI} ml.")
