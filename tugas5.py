usia = int(input("Masukan usia Anda: "))
if 0 <= usia <= 13:
    print("Kategori: Anak")
elif 14 <= usia <= 24:
    print("Kategori: Remaja")
elif 25 <= usia <= 49:
    print("Kategori: Dewasa")
elif usia >= 50:
    print("Kategori: Lansia") 
else:
    print("Usia tidak valid!")           