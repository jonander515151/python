import random
import time
import math
#nombre que vamos a buscar
nombre='nico'
print('Vamos a buscar a: ', nombre)
alfabeto='qwertyuiopasdfghjklñzxcvbnm'
alfabeto_len=len(alfabeto)
print('longitud del alfabeto: ',alfabeto_len)
for y in range(0,10):
    iteraciones_max=10000000
    inicio = time.time()
    for x in range(0,iteraciones_max):
        r1=random.randint(1, alfabeto_len)
        r2=random.randint(1, alfabeto_len)
        r3=random.randint(1, alfabeto_len)
        r4=random.randint(1, alfabeto_len)
        l1=alfabeto[r1-1]
        l2=alfabeto[r2-1]
        l3=alfabeto[r3-1]
        l4=alfabeto[r4-1]
        palabra_rand = l1 + l2 + l3 + l4
        if nombre == palabra_rand:
            print('hemos encontrado a : ', nombre)
            #break hace que acabe el for porque ya hemos resuelto
            break
        else:
            if x%100000==0 and x > 0:
                print('no hemos encontrado nada: ', palabra_rand)
                print('iteración número : ', x)

    texto_01 = 'tiempo total : '
    fin = time.time()
    tiempo_total = fin - inicio
    tiempo_total_str = str(tiempo_total)
    texto_02 = 'iteración número : '
    iteracion_str=str(x)
    coma=';'
    tiempo_1M=tiempo_total/x*1000000
    texto_03 = 'tiempo por millón de iteraciones: '
    tiempo_1M_str = str(tiempo_1M)
    texto_final = texto_01 + coma + tiempo_total_str + coma + texto_02 + coma + iteracion_str + coma + texto_03 + coma + tiempo_1M_str + coma
    print(texto_final)
    #código para escribir el txt
    busca_nombre_str="busca_nombre_"
    formato =".txt"
    nombre_archivo = busca_nombre_str + nombre + formato
    with open(nombre_archivo, "a") as archivo:
        archivo.write(texto_final)
        archivo.write("\n")
        # No olvides cerrar el archivo
        archivo.close()
    print('------------------------------------')






