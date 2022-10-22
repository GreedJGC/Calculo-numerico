#!/usr/bin/env python3


def Error_absoluto(a,b): #Permite realizar el margen de error absoluto
	if a>b:Error_absoluto=a-b 
	pass
	return Error_absoluto

def Error_relativo(a,b): #Permite realizar el margen de error relativo
	if a>b:Error_relativo=(a-b)/a 
	pass
	return Error_relativo

if __name__ == '__main__':
	#Prueba 1
	x=5
	y=4
	print(Error_absoluto(x,y))
	print(Error_relativo(x,y))
	
	#Prueba 2
	x=20000
	y=19999
	print(Error_absoluto(x,y))
	print(Error_relativo(x,y))
