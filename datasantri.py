pesantren = {}

print("?nmenu:")
print("1. tambah data santri")
print("2. Lihat Data santri")
print("3. Keluar")

pilihan = input("PILIH menu (1/2/3): ")

if pilihan =='1' :
    nama= input("masukkan nama santri: ")
    usia= int(input("masukkan usia santri"))
    kelas= input("masukkan kelas santri: ")
    pesantren[nama]= {"usia":"usia","kelas":"kelas"}
    print(f"data santri {nama} telah ditambahkan.")

elif pilihan == '2':
    if len(pesantren) == 0:
            print("tidak ada data santri yang tersedia.")
    else:
        print("\nData Santri:")
    for nama, data in pesantren.items(): 
         print(f"nama:{nama}, Usia:{data['usia']}, kelas:{data['kelas']}")        
      
elif pilihan == '3':
    print("terima kasih, program selesai.")
    break

else:
    print("pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
