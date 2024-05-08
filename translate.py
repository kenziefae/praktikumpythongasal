from googletrans import Translator
tl = Translator() 
text = input("masukkan text : ")

result = tl.translate(text, dest='en')

print(result.text)