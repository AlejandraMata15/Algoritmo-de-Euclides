import os
os.system('clear')

def euclides_extendido(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, x1, y1) = euclides_extendido(b, a % b)
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

mcd,x,y=euclides_extendido(alfa,n)

print('\nFunción de cifrado\n'+str(mcd)+' = '+str(alfa)+' + '+str(beta)+' mod('+str(n)+')')

print('\nFunción de decifrado\n'+'p = alfainversa [ '+str(mcd)+' + '+str(n-beta)+' ] mod( '+str(n)+' ) ')


