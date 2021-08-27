def main():
    # escribe tu código abajo de esta línea
    nuevos= int(input('Dame la cantidad de juegos nuevos: '))
    usados= int(input('Dame la cantidad de juegos usados: '))

    total= (1000*nuevos)+(350*usados)
    print('El total de la compra es:',total)


if __name__ == '__main__':
    main()
