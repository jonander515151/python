import random
import time
print('Ejercicio César')
#alfabeto
abc =     'abcdefghijklmnñopqrstuvwxyz .'
#usamos un alfabeto más largo para añadir el +3 de césar
abc_ext = 'abcdefghijklmnñopqrstuvwxyz .,;/'
#longitudes de los alfabetos para los bucles
abc_len = len(abc)
abc_len2 = len(abc_ext)
#criptograma
n1 = 'pdgd;hv;hvshfldñohpwh;glilflñ;vl;ñr;glylghv;hp;shtxhqrv;wudedmrv/;khpu.;irug'
n1_len = len(n1)
#preparamos listas vacias para escribir el orden
orden = 500*[0]
orden_decript = 500*[0]
n1_sin_cript = 500*[0]
texto_claro = ''
for x in range(0,n1_len):
    for y in range(0,abc_len2):
        #anotamos el orden
        if n1[x] == abc_ext[y]:
            orden[x] = y
            #restamos 3 al orden
            orden_decript[x] = y-3


for x in range(n1_len):
    #pasamos de orden a letras
    n1_sin_cript[x] = abc[orden_decript[x]]
    #reconstruimos la frase letra a letra
    texto_claro = texto_claro + n1_sin_cript[x]

#mostramos la frase
print('Tu frase:' , texto_claro)





