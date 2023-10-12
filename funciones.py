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

#Variables de entrada
print('Ingresa n : ',end='')
n=int(input())

print('Ingresa alfa : ',end='')
alfa=int(input())

print('Ingresa beta : ',end='')
beta=int(input())

mcd,x,y=aee(alfa,n)

print('\nFunción de cifrado\n'+str(mcd)+' = '+str(alfa)+' + '+str(beta)+' mod('+str(n)+')')

print('\nFunción de decifrado\n'+'p = alfainversa [ '+str(mcd)+' + '+str(n-beta)+' ] mod( '+str(n)+' ) ')


