# 1. Buatlah variabel dengan nama kata benda
# 2. Isikan data pada variabel tersebut sejumlah 17 data
kata_benda =["baju","celana","topi","kopiah","kacamata","tas","gesper","jam","laptop","pencil","pena","penggaris","spidol","lampu","jendela","kaca","kayu"]

print("semua kata_benda: ada{} buah".format(len(kata_benda)))

# 3. Tambahkan 1 data paling belakang pada variabel tersebut
kata_benda.append("atap")

# 4. Tambahkan 1 data pada indeks ke 3
kata_benda.insert(3,"batu")

# 5. Cetak variabel tersebut menggunakan fungsi for
for benda in kata_benda:
    print(benda)