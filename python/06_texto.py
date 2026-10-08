# string cadenas de caracteres 
jedi = "qui-gon jinn"
aprendiz = "Obi-Wan Kenobi"
droide = "R2-D2"
planeta = "Naboo"
codigo = "327"

print("El Jedi es: " + jedi)
print("El jedi", type(jedi))
print("El aprendiz es: " + aprendiz)
print("El aprendiz", type(aprendiz))
print("El droide es: " + droide)
print("El droide", type(droide))
print("El planeta es: " + planeta)
print("El planeta", type(planeta))
print("El código es: " + codigo)
print("El código", type(codigo))

longitud_jedi = len(jedi)
print("La longitud del nombre Jedi es: " + str(longitud_jedi))
longitud_aprendiz = len(aprendiz)
print("La longitud del nombre Jedi es: " + str(longitud_aprendiz))

# MAYUSCULA Y MINUSCULA CON STRING
mensaje = "La Federacion  de comercio ha establecido un bloqueo en Naboo"
print("El mensaje es: " + mensaje)
mensaje_mayusculas = mensaje.upper()
print("El mensaje en mayuscula es: " + mensaje_mayusculas)
mensaje_minuscula = mensaje.lower()
print("El mensaje en minuscula es: " + mensaje_minuscula)

comunicado = "Los Jedi son enviados de Naboo"
print("EL comunicado es: " + comunicado)
nuevo_comunicado = comunicado.replace("Naboo", "Tatooine")
print("El nuevo comunicado es: " + nuevo_comunicado)

# HACER UNA LSITA .SPLIT
planetas = "Naboo, Tatooine, Coruscant, Alderaan"
planetas_lista = planetas.split(", ")
print(planetas_lista)
print("La lista de planetas es: " + str(planetas_lista))
print("El primer planeta es: " + planetas_lista[0])

