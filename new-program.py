nilai_ujian =str(input("masukkan nilai ujian:"))

if nilai_ujian =="A":
    kategori = "Luar Biasa"

elif nilai_ujian =="B":
    kategori = "Baik"

elif nilai_ujian =="C":
    kategori = "Cukup"

elif nilai_ujian =="D":
    kategori = "kurang"

else:
    kategori = "mengulang"
    
print(f"Nilai ujian Anda adalah {nilai_ujian}, sehingga masuk kategori: {kategori}")

