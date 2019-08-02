import time
import sys
import os
from random import randint

def extrapolador():
	time.sleep(1.6)
	ax = os.system
	ax('cls')
	ax('color 4')
	print('''\t
	    ___ _   _  _ _      __   __  ___ _  __   
	   | __| \ / || | |   /' _/ /__\| __| |/  \ 
	   | _|`\ V /'| | |_  `._`.| \/ | _|| | /\ |
	   |___| \_/  |_|___| |___/ \__/|_| |_|_||_|
	   '''   )
	print("\t      ---Emmanuel Milos" + "|" + "Emilio Barroso---")
	print('''
  
    ''')
	nombre = str(input("  Introduce tu nombre de Binero: "))
	x = nombre.upper()
	print("")
	time.sleep(1)
	print("\tACCES GRANTED FOR USER {}!".format(x))
	print("")
	time.sleep(0.8)
	cc = int(input("  Introduce la primer cc completa de 16 digitos: "))
	print("")
	cc2 = int(input("  Introduce la segunda cc completa de 16 digitos: "))
	if not cc == cc2:
		print("")
	else:
		print("")
		print("  las tarjetas tienen que ser distintas :)")
		print("")
		cc2 = int(input("  Introduce la SEGUNDA cc completa de 16 digitos: "))
		print("")

	time.sleep(1)
	print("CC #1 {}".format(cc))
	print("      ^^^^^^^^")
	print("")
	print("  Ahora solo digita los primeros 8 digitos de la cc :D")
	time.sleep(0.3)
	print("")
	Bin = int(input("  Digite los primeros 8 digitos de la cc: "))
	print("")
	print("  La fecha de expiracion seran las correspondientes a la primer cc :D")
	print("")
	ExpM = int(input("  Introduce el mes de expiracion: "))
	if ExpM <= 12 and ExpM >= 0:
		print("")
	else:
		print("MES INCORRECTO :) ")
		print("")
		ExpM = int(input("  Introduce el mes de expiracion de nuevo: "))

	ExpA = int(input("  Introduce el año de expiracion: "))
	if ExpA >= 19 and ExpA <=30:
		print("")
	else:
		print("AÑO INCORRECTO")
		print("")
		ExpA = int(input("  Introduce el año de expiracion de nuevo: "))

	print("")
	ax('cls')

	print('''
	    ___ _   _  _ _      __   __  ___ _  __   
	   | __| \ / || | |   /' _/ /__\| __| |/  \ 
	   | _|`\ V /'| | |_  `._`.| \/ | _|| | /\ |
	   |___| \_/  |_|___| |___/ \__/|_| |_|_||_|
	   '''   )
	print("         Emmanuel Milos" + "|" + "Emilio Barroso")
	print("")
	print("")

	print("CC #1 {}".format(cc))
	print("                ^^")
	print("CC #2 {}".format(cc2))
	print("                ^^")

	bin11 = int(input("  Introduce el digito DIEZ de la primer cc: "))
	if bin11 >= 0 and bin11 <= 9:
		print("")
	else:
		print("  Introduce un numero correcto :)")
		bin11 = int(input("  Introduce de nuevo el digito DIEZ de la primer cc: "))

	bin12 = int(input("  Introduce el digito ONCE de la segunda cc: "))
	if bin12 >= 0 and bin12 <= 9:
		print("")
	else:
		print("  Introduce un numero correcto :)")
		bin12 = int(input("  Introduce de nuevo el digito ONCE de la primer cc: "))

	bin21 = int(input("  Introduce el digito DIEZ de la segunda cc: "))
	if bin21 >= 0 and bin21 <= 9:
		print("")
	else:
		print("  Introduce un numero correcto :)")
		bin21 = int(input("  Introduce de nuevo el digito DIEZ de la segunda cc: "))

	bin22 = int(input("  Introduce el digito ONCE de la segunda cc: "))
	if bin22 >= 0 and bin22 <= 9:
		print("")
	else:
		print("  Introduce un numero correcto :)")
		bin22 = int(input("  Introduce de nuevo el digito ONCE de la segunda cc: "))

	A = int(bin11 + bin21 / 2) * 5
	B = int(bin12 + bin22 / 2) * 5
	C = A + B
	equis = "xxxxxx"

	print("  Tu extrapolacion es: ")
	time.sleep(1)
	print("  {}{}{}".format(Bin, C, equis))
	print("  "+f"{ExpM}"+"|"+f"{ExpA}")
	time.sleep(2)

extrapolador()