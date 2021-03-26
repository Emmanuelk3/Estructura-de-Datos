registro = []
venta = []
articulo = {}
num_venta = 1
total = 0

try:
    with open('BD.txt','r') as file:
        control = 0
        control2 = 0
        for line in file:
            puntos = line.find(':')
            if puntos != -1:
                x = line[:puntos]
                y = line[puntos+1:-1]
                articulo[x] = y
                control2 += 1
                if control2 == 3:
                    venta.append(articulo)
                    articulo = {}
                    control2 = 0
            else:
                if line == '':
                    continue
                if control < 2:
                    venta.append(int(line[:-1]))
                    control += 1
                else:
                    registro.append(venta)
                    num_venta = venta[-2] + 1
                    venta = []
                    control = 0
except:
    w = 1

opcion = input("[1] Registrar una venta \t[2] Consultar una venta \t[3] Salir: ")
while opcion != "3":
    if opcion == "1":
        print(f'Venta {num_venta}')
        opc2 = True
        while opc2 == True:
            while True:
                des = input("Descripcion del articulo:")
                if des == '':
                    print('La descripcion no puede estar vacia')
                    continue
                break
            while True:
                try:
                    piezas = int(input("Cantidad de piezas vendidas:"))
                    if piezas < 1:
                        print('Las piezas tiene que ser mayor a 0')
                        continue
                    break
                except:
                    print('El valor ingresado no es un int')
                    continue
            while True:
                try:
                    precio = int(input("Precio de venta:"))
                    if precio < 1:
                        print('El precio tiene que ser mayor a 0')
                        continue
                    break
                except:
                    print('El valor ingresado no es un int')
                    continue


            articulo['Descripcion'] = des
            articulo['Piezas'] = piezas
            articulo['Precio'] = precio

            venta.append(articulo)
            articulo = {}
            while True:
                opc3 = input("Hay mas articulos? si/no:")
                if opc3 == "no":
                    opc2 = False
                    break
                elif opc3 == "si":
                    break
                else:
                    print("Esa no es una opcion valida")
                    continue

        for arti in venta:
            sub_total = arti['Precio'] * arti['Piezas']
            total += sub_total

        print(f'Total de la venta es ${total}')
        venta.append(num_venta)
        venta.append(total)
        registro.append(venta)
        venta = []
        num_venta += 1
        total = 0
    elif opcion == "2":
        consulta = int(input('Numero de venta: '))
        w = 1
        j = 1
        try:
            for arti in registro[consulta-1]:
                if type(arti) != int:
                    print(f'Articulo {w}')
                    w += 1
                    for key in arti:
                        print(f'{key:12}: {arti[key]}')
                else:
                    if j == 1:
                        nom = 'Venta'
                        print(f'{nom:12}: {arti}')
                        j += 1
                    else:
                        nom = 'Total'
                        print(f'{nom:12}: {arti}')
            w = 1
            j = 1
        except:
            print("No existe ese numero de venta")
    opcion = input("[1] Registrar una venta \t[2] Consultar una venta \t[3] Salir: ")

with open('BD.txt','w') as file:
    if registro != []:
        for vent in registro:
            for arti in vent:
                if type(arti) != int:
                    for key in arti:
                        file.write(f'{key}:{arti[key]}\n')
                else:
                    file.write(str(arti)+'\n')
            file.write('\n')