# Operadores 
"""
Operadores aritméticos:
+  Suma
-  Resta
*  Multiplicación
/  División
%  Módulo
** Potencia 
"""
valor1 = 10 
valor2 = 3 
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

print("Tabla de multiplicar del 5:")
multiplicador = 5
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2)
print("5 x 3 =", 5 * 3)
print("5 x 4 =", 5 * 4)
print("5 x 5 =", 5 * 5)
print("5 x 6 =", 5 * 6)
print("5 x 7 =", 5 * 7)
print("5 x 8 =", 5 * 8)
print("5 x 9 =", 5 * 9)
print("5 x 10 =", 5 * 10)

print("Area de un triangulo con base 5 y altura 10:", (5 * 10) / 2)

# Operadores de comparación
"""
- == (igual)
- != (diferente)
- > (mayor que)
- < (menor que)
- >= (mayor o igual que)
- <= (menor o igual que)
"""

velocidad_anakin = 950
velocidad_sebula = 900

print("¿ Anakin es mas rapido que Sebula ?", velocidad_anakin > velocidad_sebula)
print("¿ Anakin es mas lento que Sebula ?", velocidad_anakin < velocidad_sebula)
print("¿ Anakin es igual de rapido que Sebula ?", velocidad_anakin == velocidad_sebula)
print("¿ Anakin es distinto de  Sebula ?", velocidad_anakin != velocidad_sebula)
print("¿ Anakin es mas rapido o igual que Sebula ?", velocidad_anakin >= velocidad_sebula)
print("¿ Anakin es mas lento o igual que Sebula ?", velocidad_anakin <= velocidad_sebula)

resultado = velocidad_anakin > velocidad_sebula
print("Resultado de la comparación:", resultado)
print("Tipo de resultado:", type(resultado))

# Operadores Logicos
"""
- and (y)
- or (o)
- not (no)
"""
motores_funcionando = True
escudos_funcionando = False
combustible = 80 

print("¿ Todos los sistemas están funcionando ?", motores_funcionando and escudos_funcionando)
print("¿ Alguno de los sistemas esta fallando ?", not motores_funcionando or escudos_funcionando)
print("¿ Los motores no están funcionando ?", not motores_funcionando )
 
cantidad_motores = 2
cantidad_alas = 4
combustible = 80

print("¿La nave tiene al menos 2 motores y 4 alas?")
print(cantidad_motores >= 2 and cantidad_alas >= 4 and combustible >= 50)
print("¿La nave tiene al menos 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas >= 4 or combustible >= 50)
print("¿La nave no tiene al menos 2 motores?")
print(not cantidad_motores >= 2 and combustible >= 50 and cantidad_alas >= 4)

#Operadores de asignacion
"""
- = (asignación)
- += (suma y asignación)
- -= (resta y asignación)
- *= (multiplicación y asignación)
- /= (división y asignación)
- %= (módulo y asignación)
- **= (potencia y asignación)
"""
velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad después de acelerar:", velocidad)
velocidad -= 30
print("Velocidad después de frenar:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad después de multiplicar:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de dividir:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de aplicar módulo:", velocidad)
velocidad **= 2
print("Velocidad después de aplicar potencia:", velocidad)

# PRECEDENCIA DE OPERADORES 
"""
1. ()
2. ** (potencia)
3. * / % (multiplicación, división, módulo)
4. + - (suma, resta)
"""
resultado_1 = 10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2 = (10+5)*2
print("Resultado 2:", resultado_2)
resultado_3 = 10 + 5 * 2 ** 2
# PRECEDENCIA DE OPERADORES 
"""
1. ()
2. ** (potencia)
3. * / % (multiplicación, división, módulo)
4. + - (suma, resta)
"""
resultado_1 = 10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2 = (10+5)*2
print("Resultado 3:", resultado_3)