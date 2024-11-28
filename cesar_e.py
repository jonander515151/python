import random
import time
print('Ejercicio César')
#alfabeto
abc =     'abcdefghijklmnñopqrstuvwxyz .'
#usamos un alfabeto más largo para añadir el +3 de césar
abc_ext = 'abcdefghijklmnñopqrstuvwxyz .,;/'
abc_len = len(abc)
#texto en claro
n1 ='nada es especialmente dificil si lo divides en pequeños trabajos. henry ford'
n1_len = len(n1)
#preparamos listas vacias para escribir el orden
orden = 500*[0]
n1_cript = 500*[0]
orden_cript = 500*[None]
#criptograma
criptograma = ''

for x in range(0,n1_len):
    for y in range(0,abc_len):
        #anotamos el orden
        if n1[x] == abc[y]:
            orden[x] = y
 #sumamos 3 al orden
for x in range(0 , n1_len):
    orden_cript[x] = orden[x]+3

for x in range(n1_len):
     #pasamos de orden a letras
    n1_cript[x] = abc_ext[orden_cript[x]]
    #reconstruimos la frase letra a letra
    criptograma = criptograma+n1_cript[x]
    
#mostramos la frase
print('Frase incriptada:', criptograma)


