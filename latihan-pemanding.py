nilai_ujian = float(input("masukkan nilai ujian:"))

if nilai_ujian >= 90:
    kategori = "A"

elif nilai_ujian >= 80:
    kategori = "B"

elif nilai_ujian >= 70:
    kategori = "C"

elif nilai_ujian >= 60:
    kategori = "D"

else:
    kategori = "E"

print(f"Nilai ujian Anda adalah {nilai_ujian}, sehingga masuk kategori: {kategori}")

