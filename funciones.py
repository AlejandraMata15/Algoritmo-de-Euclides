import os
os.system('clear')

def aee(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, x1, y1) = aee(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (d, x, y)

def inicio(n,alfa,beta):
	mcd,x,y=aee(alfa,n)
	cifrado_label.config(text="\nFunción de cifrado'\nc=" + str(alfa)+'p + '+str(beta)+' mod('+str(n)+)
	descifrado_label.config(text="\nFunción de descifrado'\nc=" + str(alfa)+'p + '+str(beta)+' mod('+str(n)+)
	print('\nFunción de cifrado\nc='+str(alfa)+'p + '+str(beta)+' mod('+str(n)+')')
	print('\nFunción de decifrado\np='+str(x)+' [c+'+str(n-beta)+'] mod('+str(n)+')')
