#!!!! BUKTIKAN KAMU MENEMPUH 20.2 MILES DAN MEMBAYAR $30.30 !!!!
#biaya per miles = $1.50
#odometer awal = 78602.5
#odometer akhir = 78622.7

#step 1
odometer_awal = float(input("odometer awal: "))
odometer_akhir = float(input("odometer akhir: "))

#step 2
jarak = odometer_akhir - odometer_awal
biaya = float(jarak * 1.50)

#step 3
print(f"kamu menempuh jarak {jarak:.1f} miles. \ndan kamu perlu membayar ${biaya:.2f}.") 