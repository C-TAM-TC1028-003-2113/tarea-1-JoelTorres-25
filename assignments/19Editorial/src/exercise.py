import math
def main():
    # escribe tu código abajo de esta línea
    palabras=int(input('Dame el número de palabras: '))
    paginas= math.ceil(palabras/475)
    costo= (paginas*60)-(paginas*60*.10) 
    print('El costo de la publicación es:',costo)
    
if __name__ == '__main__':
    main()