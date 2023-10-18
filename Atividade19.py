n1 = float(input("primeira nota:"))
n2 = float(input("segunda nota:"))
media = (n1 + n2) / 2
print ("media:", media)

if media<7.0:
    print("reprovado, boa sorte na proxima")
elif media<10:
    print ("aprovado")
else:
    print ("aprovado")

