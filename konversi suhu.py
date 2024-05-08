print('##  Program Python Konversi Suhu  ##')
print('====================================')
print()

celc = float(input('Input suhu celcius: ')) 

fahr = (9/5 * celc) + 32
kelv = celc + 273.15
ream = celc * (4/5) 

print(celc,'derajat Celcius =',fahr,'derajat Fahrenheit')
print(celc,'derajat Celcius =',kelv,'derajat Kelvin')
print(celc,'derajat Celcius =',ream,'derajat Reamur')

