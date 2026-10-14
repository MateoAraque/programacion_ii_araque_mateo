print("==== CONTROL DE ENERGIA ====")
energia_texto = "ochenta"

try:
    energia = int(energia_texto)
    print(energia)
except ValueError:
    print(" Error : debe ser numerico")


print("Fin del sistema")

"""
ValueError
TypeError
KeyError
IndexError
ZeroDivisionError
"""


def calcular_energia(total, cantidad):
    try:
        resultado = total / cantidad
        return resultado
    except ZeroDivisionError as Error:
        print("ERROR : division entre cero", Error)
        return None
    except TypeError:
        print("ERROR : valores deben ser numericos")
        return None

print("Caso 1:", calcular_energia(100,4))
print("Caso 2:", calcular_energia(100,0))
print("Caso 3:", calcular_energia(100,"cuatro"))

print("========= DIAGNOSTICO R2-D2 ==========")
try:
    energia = int("cuatro")
    print("energia", energia)
except ValueError:
    print("Error de lectura")
else:
    print("diagnóstico completo")
finally:
    print("Cerrando diagnostico")

def validar_energia(energia):
    if type(energia) is not int:
        raise TypeError("La energia debe ser un numero entero")
    if energia < 0 or energia > 100:
        raise ValueError("La energia debe ser entre 0 y 100")
        return energia


try:
    resultado = validar_energia(60)
    print("Energia", resultado)
except (TypeError, ValueError) as Error:
    print("Error: ", Error)
