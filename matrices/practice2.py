
PAISES = 14 
DATOS = 6 
paises = [ "Costa Rica", "Argentina", "Panamá", "Chile",
         "Uruguay", "Paraguay", "Colombia", "Perú", "Ecuador",
         "Bolivia","Brasil", "México","Nicaragua","Venezuela"]
print(f"Estos son los paises ya puestos\n\n{paises}")
n = input("\n\tIngresa nuevo pais --> ")
paises.append(n)
datos = [ 
        [2290, 569, 4 , 300255, 527.7, 131],
        [75, 22.8, 3.3, 9500, 416.7, 127],
        [5.9, 1, 5.9, 744, 744, 126], 
        [2600, 634, 4.1, 276000, 435.3, 106], 
        [140, 30.8, 4.5, 13430, 436, 96],
        [26542, 5601,4.7, 2200000, 392.8, 83], 
        [10900, 2964, 3.7, 869453, 293.3, 80], 
        [11.5, 3.3, 3.5, 850, 257.6, 74], 
        [5.5, 1, 5.5, 386, 386, 70], 
        [34, 7, 4.9, 2000, 287.4, 59], 
        [16.5, 3.6, 4.6, 965, 268.1, 58], 
        [48, 19.6, 2.5, 2687, 137.2, 56], 
        [168, 31.3, 5.4, 8445, 269.6, 50], 
        [168000, 690854, 0.2, 1308000, 1.9, 8]
        ] 
m = int(input("\n\tIngrese datos de tu  pais (separado por comas) --> \n"))
datos.append([m])


while True:
    l = int(input("""

                                                                                0 = Costa Rica
                                                                                1 = Argentina
                                                                                2 = Panama  
                                                                                3 = Chile
                                                                                4 = Uruguay 
                                                                                5 = Paraguay
                                                                                6 = Colombia
                                                                                7 = Perú 
                                                                                8 = Ecuador
                                                                                9 = Bolivia
                                                                                10 = Brasil
                                                                                11 = México
                                                                                12 = Nicaragua
                                                                                13 = Venezuela      
                                    
                                    Enter number : """))
    pais = paises[l]
    ñ = int(input("""
                  0 = precio local 
                  1 = tasa de cambio de dolar
                  2 = Precio BM dolares
                  3 = Salario minimo local
                  4 = salario minimo dolares
                  5 = numero de Big-Macs
    
            """))
    dato = datos[ñ]
    print(f"\n{pais} = {dato}")
    break

    
for i in range(PAISES):
    
    print("%10s"%paises[i], end=" ") 
    for j in range(DATOS):
        print("%12.2f" % (datos[i][j]), end= " ") 
    print()

    