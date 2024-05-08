ascii_code = int (input("masukkan kode ascii"))
if 0<= ascii_code <=255:
   character = chr(ascii-code)
   print(f"karakter yang sesuai dengan kode ascii {ascii_code} adalah {character}")
else:
    print(f"kode ASCII harus berada dalam rentang 0 sampai 255 ")