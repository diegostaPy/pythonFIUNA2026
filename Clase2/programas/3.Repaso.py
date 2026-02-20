# ==================================================
# SCRIPT DE REPASO: Fundamentos de Programación

# ==================================================

# --- 1. COMENTARIOS ---
# Los comentarios son ignorados por Python, pero son vitales para los programadores.
# Se usan para explicar el código.
print("--- 1. Comentarios ---")
print("Los comentarios (como este) son ignorados por el intérprete.\n")

# --- 2. VARIABLES Y TIPOS DE DATOS BÁSICOS ---
# En Python, las variables se crean en el momento de la asignación.
# No es necesario declarar su tipo.
print("--- 2. Variables y Tipos de Datos Básicos ---")
nombre = "Ana"          # Tipo str (cadena)
edad = 25               # Tipo int (entero)
altura = 1.67           # Tipo float (decimal)
es_estudiante = True    # Tipo bool (booleano)
sin_valor = None        # Tipo NoneType (ausencia de valor)

print(f"Variable 'nombre' = '{nombre}' es de tipo: {type(nombre)}")
print(f"Variable 'edad' = {edad} es de tipo: {type(edad)}")
print(f"Variable 'altura' = {altura} es de tipo: {type(altura)}")
print(f"Variable 'es_estudiante' = {es_estudiante} es de tipo: {type(es_estudiante)}")
print(f"Variable 'sin_valor' = {sin_valor} es de tipo: {type(sin_valor)}")

# Las variables pueden cambiar de tipo (aunque no es una buena práctica abusar de esto).
x = 10
print(f"\nVariable x inicialmente es {x} ({type(x)})")
x = "Ahora soy un texto"
print(f"Variable x ahora es '{x}' ({type(x)})")
print("-" * 50)

# --- 3. REGLAS DE IDENTIFICADORES ---
# Los nombres de las variables deben seguir reglas específicas.
print("\n--- 3. Reglas de Identificadores ---")
mi_variable = "válida"  # Correcto: usa guión bajo
_variable2 = 100        # Correcto: puede empezar con guión bajo
variableLarga3 = 3.14   # Correcto: sensible a mayúsculas/minúsculas
print("Ejemplos válidos: mi_variable, _variable2, variableLarga3")
print("Ejemplos inválidos: 1valor, mi-variable, $precio (contienen caracteres no permitidos)")
print("-" * 50)

# --- 4. OPERADORES Y EXPRESIONES ---
# Python tiene varios tipos de operadores: aritméticos, de asignación, relacionales y lógicos.
print("\n--- 4. Operadores y Expresiones ---")

# Aritméticos
a, b = 15, 4
print(f"a = {a}, b = {b}")
print(f"Suma (+) = {a + b}")
print(f"Resta (-) = {a - b}")
print(f"Multiplicación (*) = {a * b}")
print(f"División (/) = {a / b}")          # Siempre devuelve un float
print(f"División Entera (//) = {a // b}")  # Descarta el resto
print(f"Módulo/Resto (%) = {a % b}")        # Resto de la división
print(f"Potencia (**) = {a ** b}")

# Asignación aumentada
c = 5
print(f"\nValor inicial de c: {c}")
c += 3  # Equivalente a c = c + 3
print(f"c += 3 -> c = {c}")

# Relacionales (siempre devuelven True o False)
print(f"\n{a} > {b}: {a > b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

# Lógicos
print(f"\n({a} > 10) and ({b} < 10): {(a > 10) and (b < 10)}")
print(f"({a} > 20) or ({b} < 10): {(a > 20) or (b < 10)}")
print(f"not ({a} == 15): {not (a == 15)}")
print("-" * 50)

# --- 5. ENTRADA Y SALIDA DE DATOS (INPUT/PRINT) ---
print("\n--- 5. Entrada y Salida de Datos ---")
# La función input() SIEMPRE devuelve un string. Hay que convertirlo si necesitamos otro tipo.
# nombre_usuario = input("¿Cómo te llamas? ")  # Descomenta para probar
# Para este script de demostración, asignamos un valor fijo.
nombre_usuario = "Carlos"
print(f"\nHola, {nombre_usuario}! (saludo con print estándar)")

# Formateo de salida con f-strings (recomendado)
edad_usuario = 30
print(f"{nombre_usuario} tiene {edad_usuario} años.")
print(f"El año que viene tendrá {edad_usuario + 1}.")

# Formateo de salida con el método format y el operador %
pi = 3.14159265359
print(f"\nEl valor de pi con 3 decimales es: {pi:.3f} (f-string)")
print("El valor de pi con 3 decimales es: %.3f" % pi) # Usando % (estilo antiguo)
print("-" * 50)

# --- 6. ESTRUCTURAS DE SELECCIÓN (IF / ELIF / ELSE) ---
# Permiten que el programa tome decisiones basadas en condiciones booleanas.
print("\n--- 6. Estructuras de Selección ---")

# Ejemplo 1: If simple
print("\n---> Ejemplo If Simple <---")
numero = -5
print(f"Número evaluado: {numero}")
if numero < 0:
    print("El número es negativo.")

# Ejemplo 2: If-else
print("\n---> Ejemplo If-Else <---")
numero = 10
print(f"Número evaluado: {numero}")
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")

# Ejemplo 3: If-elif-else (Múltiples caminos)
# Problema de la calificación del alumno (Página 73 del PDF)
print("\n---> Ejemplo If-Elif-Else <---")
puntaje = 85
print(f"Puntaje del alumno: {puntaje}")
if puntaje >= 90:
    calificacion = 5
elif puntaje >= 80:
    calificacion = 4
elif puntaje >= 70:
    calificacion = 3
elif puntaje >= 60:
    calificacion = 2
else:
    calificacion = 1
print(f"La calificación correspondiente es: {calificacion}")

# Ejemplo 4: Anidamiento y lógica compleja
print("\n---> Ejemplo de Lógica Compleja (Año Bisiesto) <---")
anho = 2024
print(f"Año evaluado: {anho}")
# Un año es bisiesto si es múltiplo de 4 pero no de 100, a no ser que lo sea también de 400.
if (anho % 4 == 0 and anho % 100 != 0) or (anho % 400 == 0):
    print(f"El año {anho} es bisiesto.")
else:
    print(f"El año {anho} no es bisiesto.")

# Ejemplo 5: Operador Ternario (forma concisa de if-else)
print("\n---> Ejemplo Operador Ternario <---")
edad_votar = 17
mensaje = "Puede votar" if edad_votar >= 18 else "No puede votar"
print(f"Edad: {edad_votar} -> {mensaje}")
print("-" * 50)

# --- 7. MÓDULOS Y FUNCIONES INCORPORADAS ---
# Podemos importar módulos para tener más funcionalidades.
print("\n--- 7. Uso de Módulos (math) ---")
import math

radio = 5
circunferencia = 2 * math.pi * radio
area = math.pi * (radio ** 2)
print(f"Para un círculo de radio {radio}:")
print(f"  - Circunferencia = {circunferencia:.2f}")
print(f"  - Área = {area:.2f}")
print(f"  - Raíz cuadrada de 25 es: {math.sqrt(25)}")
