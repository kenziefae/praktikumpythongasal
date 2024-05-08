# 1.INI ADALAH KOMENTAR
# contoh : #(pagar)

# 2.INI ADALAH SINTAKSIS PYTHON
# sintaksis adalah baris kode dalam python
#  contoh
# print("hello, world")
# print("kenzie")

#3.RUN PROGRAM PYTHON
 # A. variabel adalah sebuah nama atau karakter yang didefinisikan untuk menampung data dapat diubah 
 #                    mencakup lebih dari 1

# Konstanta sama dengan variabel namun sifatnya konstan tak dapat diubah 
 
  
 
 
# contoh:
# x = 5
# y = "NoM"
# print(x,y)
# print(x)
# print(y)

# TUGAS+CONTOH

# x = "Belajar pemrograman Algoritma Python"
# y = "kelas 1 intensiv"
# a = "Pesantren Teknologi Majapahit"
# b = "Kenzie FT"
# c = "BaBel"
# d =7

# print(x)
# print(y)

# print(a)
# print(b)

# print(c)
# print(d)

# B. Konstanta :sama seperti variabel tapi dia bersifat konstan(tetap), hanya mencakup 1



# TIPE DATA

# 1.Integer(INT) adalah tipe data untuk angka bulat baik itu positif maupun negatiF
# a = 50
# b = 100
# c = -500
# print(a)
# print(b)
# print(c)

#2.Float 
# float adalah tipe data untuk angka desimal baik itu positif atau negatif
# d = 0.5
# e = 500.5
# f = 3.53647
# print(d)
# print(e)
# print(f)

#3.STRING
# string adalah tipe data untuk teks atau karakter yang di definisikan menggunakan tanda petik("")/('')/("''")
# g = "55"
# h = "79"
# i = "77"

#4.Bolean :Tipe data percabangan true dan false

# contoh:
# while(true)


#Operasi pada python

#operator : simbol yang digunakan untuk melakukan operasi tertentu

# 1.operasi aritmatika
# + : penjumlahan
# - : pengurangan
# * : perkalian
# / : pembagian
# % : hasil bagi(modulus)
# **:perpangkatan


# 2.operasi logika 
# menilai kondisi benar atau salah
# logika AND(and)
# logika OR(or)
# logika Negasi(Not)kebalikan


# 3.pembanding 
# membandingkan suatu nilai pada tiap operan 
# == :sama dengan
# != :tidak sama dengan
# >  :lebih besar dari
# <  :lebih kecil dari
# >= :lebih besar sama dengan
# <= :lebih kecil sama dengan

#  Operator Augmented Assigment/ penugasan


# contoh Ops aritmatika(1)
# a =int(input("masukkan nilai a ="))
# b =int(input("masukkan nilai a ="))
# print("a+b =  ",a+b)
# print("a-b =  ",a-b)
# print("a*b =  ",a*b)
# print("a/b =  ",a/b)
# print("a%b =  ",a%b)
# print("a**b =  ",a**b)

#ops pembanding
# == != > < >= <=
# contoh ops pembanding 
# bil1 = float(input("masukkan bilangan pertama : "))
# bil2 = float(input("masukkan bilangan kedua : "))
# if bil1>bil2:
# print(f"{bil1} lebih besar {bil2}")
# elif bil1<bil2:
# print(f"{bil1} lebih kecil {bil2}")
# else:else if
# print(f"{bil1} sama dengan {bil2}")

# contoh prmbanding:

#ilai_ujian = float(input("masukkan nilai ujian:"))

# if nilai_ujian >= 90:
 #   kategori = "A"

# elif nilai_ujian >= 80:
 #   kategori = "B"

# elif nilai_ujian >= 70:
#    kategori = "C"

# elif nilai_ujian >= 60:
#    kategori = "D"

# else:
#    kategori = "E"

# print(f"Nilai ujian Anda adalah {nilai_ujian}, sehingga masuk kategori: {kategori}")


# contoh pembading(new)
#
# nilai_ujian =str(input("masukkan nilai ujian:"))

# if nilai_ujian =="A":
    # kategori = "Luar Biasa"

# elif nilai_ujian =="B":
    # kategori = "Baik"

# elif nilai_ujian =="C":
    # kategori = "Cukup"

# elif nilai_ujian =="D":
#    kategori = "kurang"

# else:
 #   kategori = "mengulang"
    
#print(f"Nilai ujian Anda adalah {nilai_ujian}, sehingga masuk kategori: {kategori}")


#  contoh lain(new)                                                          
#
#nilai_ujian =str(input("masukkan nilai ujian:"))
# if nilai_ujian =="A":
#   print("Luar Biasa")
# elif nilai_ujian =="B":
    # print("Baik")
# elif nilai_ujian =="C":
    # print ("Cukup")
# elif nilai_ujian =="D":
    # print ("kurang")
# else:

    # print("mengulang")








# looping:memberikan dan meminta perintah pada komputer untuk melakukan sesuatu secara berulang ulang
# dibagi menjadi 2, for dan while
 
# for   : perulangan terhitung (counted loap)
# while : perulangan tidak terhitung (uncounted loap)


# FOR -> WITHOUT VAR             : Tanpa variabel
#     -> WITH VAR                : dengan variabel
#     -> LIST(senarai)           : dengan list, dia harus membuat daftar dulu
#     -> NESTED                  : Loop bersarang
#     -> WITH STATEMENT          : Loop dengan statement break(berhenti)
#     -> WITH STATEMENT CONTINUE : Loop dengan statement contonue(lanjut)


# ulang:10(data) > int
# for i in range(ulang):     
#     print(f"perulangan ke-{i}")
# 
# 
#  
#  Contoh for tanpa variabel:
#
# for index in "banana":
#     print(index)

# 
#  Contoh For dengan Variabel:
#  ontoh Program :
#  ulang = 25
#  for i in range(ulang):
#      print(f"Perulangan ke-{i}
# 

#  Contoh Program Looping Menggunakan Senarai (LIST) 
#   
#  jeniskopi = ["arabika", "robusta", "tubruk", "espreso", "vietnam drip"]
#  for x in jeniskopi:
#      print(x)
# 
#  Contoh NESTED LOOP:
# 
#   
# santri= ["abad", "kenzie", "zaydan"]
# kegiatan= ["pramuka", "jujitsu", "futsal"]
# for x in santri
#         for y in kegiatan:
#           print(x, y)
# 
# 
# 
#  Looping while:artinya syntax yang digunakan berfungsi untuk eksekusi perulangan selama ekspresi benar.
# 
# contoh looping while1:
#  # jawab = 'ya'
# hitung = 0

# while(True):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
#     if jawab == 'tidak':
#         break

# print(f"Total keseluruhan perulangan: {hitung}")

# contoh looping while2 :
# i = 1
# while i < 9 :
#     print(i)
#     i+=1
# 
# Contoh looping while with statement break :

# i = 1
# while i < 6:
#     print(i)
#     if i==3:
#        break 
#     i=+   1

# Contoh looping while with statement continue :

# i=0
# while i<6:
#     if i==3:
#        continue
#     print(i)

# 
#  LIST:struktur data yang mamapu menyimpan lebih dari satu data
# 
#  rumus-> var = [...]
# 
# 
# contoh:
#  -List satu
#  mapel = ["mtk"]
# print(mapel)
# 

# -list lebih dari satu
# kokulikuler =["jujitsu","sapta pesona","muhadoroh"]
# print(kokulikuler)
# 
# 
#  -list dengan tpe data campuran
# kenzie = ["BaBel",15,170.5,True]
# print(kenzie)
# 
# 
# -mengubah data list
# sayur = ["tomat","wortel","bayam","kol","kangkung"]
# sayur[2]= "brokoli"
# print(sayur)

# 
# 
#  -List menampung nama-nama
# satu_intensif =["indra","galih","kenzie","abad","dzakwan","habib","afham"]
# print("Daftar satu_intensif indeks ke-3 adalah:{}". format(satu_intensif[3]) )
# print("semua teman: ada{} orang".format(len(satu_intensif)))
# for santri in satu_intensif:
#     print(santri)
# 
# -module
# 
# pip install....
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# KISI-KISI PYTHON!!!!!!!,PENTING!!!!!
# 
# 1. tipe data(penegertian,penulisan, perbedaan)
# 2. struktur python variabel, input, output, tipe data
# 3. operator
# 4. perulangan(pengertian, jenis, perbedaan)
# 5. flowchart
# 6. module
# 
# 
# KISI KISI KOMSIS!!!! PENTING!!!!          

# 1. sistem bilangan(pengertian, jenis-jenis)
# 2. basis sistem bilangan
# 3. ASCII
# 4. gerbang logika(pengertian jenis jenis,simbol& maknanya)
# 5. penjumlahan sistem bilangan
# 6. makna dari bagian ic (integrated circuit)
# 7. alat dan bahan praktikum gerbang logika 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
