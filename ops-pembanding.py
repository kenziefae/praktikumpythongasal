bil1= float(input("masukkan bilangan pertama : "))
bil2= float(input("masukkan bilangan kedua : "))
if bil1 > bil2:
    print(f"{bil1} lebih besar {bil2}")
elif bil1 < bil2:
    print(f"{bil1} lebih kecil {bil2}")
else:
    print(f"{bil1} sama dengan {bil2}")