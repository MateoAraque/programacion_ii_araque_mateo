
peso = float(input("Ingrese el peso del paquete en kilogramos: "))
zona = int(input("Ingrese la zona de destino (1: America, 2: Europa, 3: Resto del Mundo )"))

if zona == 1:
    precio_kilo = 5.0
elif zona == 2:
    precio_kilo = 7.5
elif zona == 3:
    precio_kilo = 10.0
else:
    precio_kilo = None


if precio_kilo is not None:
    costo_final = peso * precio_kilo
    print("El costo final del envio es:", costo_final)
else:
    print("Error: LA zona ingresada no es valida")
     