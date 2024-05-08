import pyshorteners

link_asli = input("masukkan link:   ")
shortener = pyshorteners.Shortener()
result = shortener.tinyurl.short(link_asli)
print(result)