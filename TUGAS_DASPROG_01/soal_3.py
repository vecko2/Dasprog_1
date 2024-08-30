#!!!! BUATLAH PROGRAM UNTUK MEMPERKIRAKAN SUHU DALAM FREEZER !!!!
#jam = 2 jam
#menit = 30

#step 1
jam = int(input("berapa jam: "))
menit = int(input("berapa menit: "))

#step 2
total = jam + (menit / 60)
suhu = (4 *(total ** 2) / (total + 2)) - 20

#step 3
print(f"perkiraan suhu dalam freezer: {suhu:.2f}C")