import os
os.system('clear')

def ae(n,alpha,beta):
	x=alpha
	y=n
	while(y>0):
		r=x%y
		x=y
		y=r
		if y!=0:
			print(str(x)+'=('+str(int(x/y))+')'+str(y)+'+'+str(x%y))
	print('\nEl MCD de ('+str(n)+','+str(alpha)+') es = '+str(x))
	return x

def aee(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, x1, y1) = aee(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (d, x, y)

def inicio(n,alpha,beta):
	#Valida que alpha si funcione de lo contrario pedir otro valor de alpha
	while True:
		if alpha<n:
			#Verificando beta
			if beta>0 and beta<=n:
				comproba=ae(n,alpha,beta)
				if comproba==1:
					mcd,x,y=aee(alpha,n)
					m='\nEl MCD de ('+str(n)+','+str(alpha)+') es = '+str(comproba)
					cifrado='\n\nFunción de cifrado\nc='+str(alpha)+'p + '+str(beta)+' mod('+str(n)+')\n'
					decifrado='\nFunción de decifrado\np='+str(x)+' [c+'+str(n-beta)+'] mod('+str(n)+')'
					#print(cifrado)
					#print(decifrado)
					return m+cifrado+decifrado
				else:
					return '\nEl MCD de ('+str(n)+','+str(alpha)+') es = '+str(comproba)
				break
			else:
				#print("\nIngrese nuevo valor de beta válido",end='')
				#beta=int(input())
				return "\n\nIngrese nuevo valor de beta válido"
				beta=int(input())
				#print('Beta no es un valor válido\n')
				#break
		else:
			return '\n\nEl valor de alpha ingresado esta mal, intente de nuevo'
			alpha=int(input())
		

