# EJEMPLOS DE CADENAS (STRINGS)
#1. Creación de cadenas

# Con comillas simples o dobles
nombre = 'Ana'
apellido = "Pérez"

# Cadenas multilínea
texto_largo = """Este es un texto
que ocupa múltiples
líneas en el código"""

print(nombre, apellido)
print(texto_largo)

#2. Concatenación

# Usando el operador +
nombre = "Carlos"
apellido = "González"
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Carlos González

# Con números (convertir a str)
edad = 25
mensaje = nombre + " tiene " + str(edad) + " años"
print(mensaje)  # Carlos tiene 25 años

#3. Repetición con *

# Repetir cadenas
guiones = "-" * 20
print(guiones)  # --------------------

risa = "ja" * 5
print(risa)  # jajajajaja

# Combinación
print("=" * 30)
print("BIENVENIDO".center(30))
print("=" * 30)

#4. Indexación y slicing (acceso por posición)

texto = "Python"
# Índices:  P y t h o n
#          0 1 2 3 4 5
#         -6-5-4-3-2-1

print(texto[0])      # P (primer carácter)
print(texto[2])      # t
print(texto[-1])     # n (último carácter)
print(texto[-3])     # h

# Slicing [inicio:fin]
print(texto[0:3])    # Pyt (desde índice 0 hasta 2)
print(texto[2:5])    # tho
print(texto[:4])     # Pyth (desde inicio hasta 3)
print(texto[2:])     # thon (desde índice 2 hasta el final)
print(texto[-4:-1])  # tho (desde -4 hasta -2)
print(texto[::-1])  # invertir la cadena

#5. Métodos útiles con cadenas

mensaje = "  hOlA MunDo  "

# Limpieza y formato
print(mensaje.strip())           # "hOlA MunDo" (quita espacios)
print(mensaje.upper())           # "  HOLA MUNDO  " (mayúsculas)
print(mensaje.lower())           # "  hola mundo  " (minúsculas)
print(mensaje.capitalize())      # "  Hola mundo  " (primera mayúscula)
print(mensaje.title())           # "  Hola Mundo  " (cada palabra mayúscula)

# Búsqueda
print(mensaje.strip().find("Mundo"))      # 5 (posición donde empieza)
print("Mundo" in mensaje)                  # True
print(mensaje.strip().startswith("hOlA"))  # True
print(mensaje.strip().endswith("do"))      # False (termina en "do"? No, termina en "do" con espacio)

# Reemplazo
print(mensaje.replace("Mundo", "Python"))  # "  hOlA Python  "

#6. Longitud de cadena

palabra = "Fundamentos"
print(len(palabra))              # 11 (cantidad de caracteres)

# Validación de longitud
clave = input("Ingrese contraseña: ")
if len(clave) >= 8:
    print("Contraseña válida")
else:
    print("Mínimo 8 caracteres")

#7. Separar y unir cadenas

# split() - separa en lista
fecha = "2024-03-15"
partes = fecha.split("-")
print(partes)                    # ['2024', '03', '15']
print(f"Día: {partes[2]}, Mes: {partes[1]}, Año: {partes[0]}")

# join() - une lista en cadena
palabras = ["Hola", "mundo", "Python"]
frase = " ".join(palabras)
print(frase)                     # "Hola mundo Python"

csv = ",".join(["Juan", "30", "Ingeniero"])
print(csv)                       # "Juan,30,Ingeniero"

#8. Verificación de contenido

texto = "Python 3.10"

print(texto.isalpha())    # False (tiene número y espacio)
print(texto.isdigit())    # False (tiene letras)
print(texto.isalnum())    # False (tiene espacio)

codigo = "ABC123"
print(codigo.isalnum())   # True (solo letras y números)

espacios = "   "
print(espacios.isspace()) # True (solo espacios)

#9. Formateo avanzado

nombre = "Lucía"
edad = 28
salario = 2500.50

# f-strings (recomendado)
print(f"Nombre: {nombre}, Edad: {edad}, Salario: ${salario:.2f}")

# .format()
print("Nombre: {}, Edad: {}, Salario: ${:.2f}".format(nombre, edad, salario))

# % formatting (estilo antiguo)
print("Nombre: %s, Edad: %d, Salario: $%.2f" % (nombre, edad, salario))

#10. Ejemplos con ejercicios típicos

# Ejercicio: Palíndromo
palabra = "neuquen"
es_palindromo = palabra == palabra[::-1]
print(f"¿'{palabra}' es palíndromo? {es_palindromo}")

# Ejercicio: Invertir nombre
nombre = "Python"
invertido = nombre[::-1]
print(f"'{nombre}' al revés es '{invertido}'")



# Las comparaciones son lexicográficas (orden alfabético/ASCII)
print("a" < "b")          # True
print("Python" > "Java")  # True (P > J en ASCII)
print("abc" == "ABC")     # False (distinta capitalización)
print("abc".lower() == "ABC".lower())  # True