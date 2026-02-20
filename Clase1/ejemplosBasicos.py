"""
===========================================
EJEMPLOS PYTHON  - CLASE 1
Fundamentos de Programación - FIUNA 2026
===========================================
"""

print("=" * 70)
print("PARTE 1: OPERADORES ARITMÉTICOS BÁSICOS")
print("=" * 70)

# Operadores básicos
print("1.1 OPERADORES SIMPLES:")
print("-" * 30)
print("Suma:       5 + 3 =", 5 + 3)
print("Resta:      10 - 4 =", 10 - 4)
print("Multiplicación: 7 * 2 =", 7 * 2)
print("División decimal: 15 / 4 =", 15 / 4)
print("División entera: 15 // 4 =", 15 // 4)
print("Módulo (resto): 15 % 4 =", 15 % 4)
print("Potencia:   2 ** 3 =", 2 ** 3)

print("\n" + "=" * 70)
print("PARTE 2: PRECEDENCIA DE OPERADORES - JERARQUÍA COMPLETA")
print("=" * 70)

print("\n2.1 JERARQUÍA DE PRECEDENCIA (de mayor a menor prioridad):")
print("-" * 50)
print("1. Paréntesis: ()")
print("2. Potencia: **")
print("3. Multiplicación, División, Módulo: * / // %")
print("4. Suma, Resta: + -")
print("5. Comparación: < > <= >= == !=")
print("6. Operadores lógicos: not, and, or")

print("\n2.2 EJEMPLOS PRÁCTICOS DE PRECEDENCIA:")
print("-" * 50)

# Ejemplo 1: Potencia antes que multiplicación
print("Ejemplo A: Potencia → Multiplicación")
print("3 * 2 ** 3 =", 3 * 2 ** 3)
print("  Explicación: Primero 2**3 = 8, luego 3*8 = 24")
print("(3 * 2) ** 3 =", (3 * 2) ** 3)
print("  Explicación: Primero 3*2 = 6, luego 6**3 = 216")

# Ejemplo 2: Multiplicación antes que suma
print("\nEjemplo B: Multiplicación → Suma")
print("5 + 3 * 2 =", 5 + 3 * 2)
print("  Explicación: Primero 3*2 = 6, luego 5+6 = 11")
print("(5 + 3) * 2 =", (5 + 3) * 2)
print("  Explicación: Primero 5+3 = 8, luego 8*2 = 16")

# Ejemplo 3: Expresión compleja
print("\nEjemplo C: Expresión completa")
expresion = 10 + 3 * 2 ** 2 / 4 - 1
print("10 + 3 * 2 ** 2 / 4 - 1 =", expresion)
print("  Paso a paso:")
print("  1. 2 ** 2 = 4  (potencia primero)")
print("  2. 3 * 4 = 12   (multiplicación)")
print("  3. 12 / 4 = 3   (división)")
print("  4. 10 + 3 = 13  (suma)")
print("  5. 13 - 1 = 12  (resta)")

# Ejemplo 4: Múltiples operaciones
print("\nEjemplo D: Varias operaciones juntas")
print("2 + 3 * 4 - 8 / 2 ** 2 =", 2 + 3 * 4 - 8 / 2 ** 2)
print("  Paso a paso:")
print("  1. 2 ** 2 = 4")
print("  2. 8 / 4 = 2")
print("  3. 3 * 4 = 12")
print("  4. 2 + 12 = 14")
print("  5. 14 - 2 = 12")

print("\n" + "=" * 70)
print("PARTE 3: TIPOS DE DATOS PRIMITIVOS")
print("=" * 70)

print("\n3.1 TIPOS BÁSICOS:")
print("-" * 30)

# Enteros (int)
entero_positivo = 25
entero_negativo = -10
print(f"Entero positivo: {entero_positivo} | Tipo: {type(entero_positivo)}")
print(f"Entero negativo: {entero_negativo} | Tipo: {type(entero_negativo)}")

# Decimales (float)
decimal_simple = 3.14
decimal_cientifico = 1.5e3  # 1.5 × 10³ = 1500.0
print(f"\nDecimal simple: {decimal_simple} | Tipo: {type(decimal_simple)}")
print(f"Decimal científico: {decimal_cientifico} | Tipo: {type(decimal_cientifico)}")

# Texto (str)
saludo = "Hola Python"
nombre_curso = 'Fundamentos de Programación'
print(f"\nTexto comillas dobles: {saludo} | Tipo: {type(saludo)}")
print(f"Texto comillas simples: {nombre_curso} | Tipo: {type(nombre_curso)}")

# Booleano (bool)
verdadero = True
falso = False
print(f"\nBooleano True: {verdadero} | Tipo: {type(verdadero)}")
print(f"Booleano False: {falso} | Tipo: {type(falso)}")

print("\n" + "=" * 70)
print("PARTE 4: REPRESENTACIONES NUMÉRICAS")
print("=" * 70)

print("\n4.1 DIFERENTES BASES NUMÉRICAS:")
print("-" * 30)

# Sistema decimal (base 10)
decimal = 100
print(f"Decimal: {decimal}")

# Sistema binario (base 2) - prefijo 0b
binario = 0b1100100  # 0b indica binario
print(f"Binario: 0b1100100 = {binario}")
print(f"  Verificación: 64 + 32 + 0 + 0 + 4 + 0 + 0 = 100")

# Sistema octal (base 8) - prefijo 0o
octal = 0o144  # 0o indica octal
print(f"\nOctal: 0o144 = {octal}")
print(f"  Verificación: 1×64 + 4×8 + 4×1 = 100")

# Sistema hexadecimal (base 16) - prefijo 0x
hexadecimal = 0x64  # 0x indica hexadecimal
print(f"\nHexadecimal: 0x64 = {hexadecimal}")
print(f"  Verificación: 6×16 + 4×1 = 100")

print("\n4.2 CONVERSIÓN ENTRE BASES:")
print("-" * 30)

numero = 255

# Conversión a diferentes bases
binario_decimal = bin(numero)     # A binario
hexadecimal_decimal = hex(numero) # A hexadecimal
octal_decimal = oct(numero)       # A octal

print(f"Decimal {numero} en diferentes bases:")
print(f"  Binario: {binario_decimal}")
print(f"  Hexadecimal: {hexadecimal_decimal}")
print(f"  Octal: {octal_decimal}")

# De binario a decimal
print(f"\nDe binario a decimal: int('11111111', 2) = {int('11111111', 2)}")
print(f"De hexadecimal a decimal: int('FF', 16) = {int('FF', 16)}")
print(f"De octal a decimal: int('377', 8) = {int('377', 8)}")

print("\n" + "=" * 70)
print("PARTE 5: OPERADORES DE COMPARACIÓN")
print("=" * 70)

print("\n5.1 COMPARACIONES NUMÉRICAS:")
print("-" * 30)

a, b = 10, 5
print(f"a = {a}, b = {b}")
print(f"{a} > {b}  : {a > b}")      # Mayor que
print(f"{a} < {b}  : {a < b}")      # Menor que
print(f"{a} == {b} : {a == b}")     # Igual a
print(f"{a} != {b} : {a != b}")     # Diferente de
print(f"{a} >= {b} : {a >= b}")     # Mayor o igual
print(f"{a} <= {b} : {a <= b}")     # Menor o igual

print("\n5.2 COMPARACIONES CON TEXTO:")
print("-" * 30)

texto1 = "Python"
texto2 = "python"
texto3 = "Java"

print(f"texto1 = '{texto1}', texto2 = '{texto2}', texto3 = '{texto3}'")
print(f"'{texto1}' == '{texto2}' : {texto1 == texto2}")  # Python es case-sensitive
print(f"'{texto1}' != '{texto3}' : {texto1 != texto3}")
print(f"'{texto1}' < '{texto3}'  : {texto1 < texto3}")   # Orden alfabético: 'P' < 'J'?

print("\n" + "=" * 70)
print("PARTE 6: OPERADORES LÓGICOS")
print("=" * 70)

print("\n6.1 TABLAS DE VERDAD BÁSICAS:")
print("-" * 30)

print("AND (y):")
print("  True AND True  :", True and True)
print("  True AND False :", True and False)
print("  False AND False:", False and False)

print("\nOR (o):")
print("  True OR True  :", True or True)
print("  True OR False :", True or False)
print("  False OR False:", False or False)

print("\nNOT (no):")
print("  NOT True  :", not True)
print("  NOT False :", not False)

print("\n6.2 EJEMPLOS PRÁCTICOS:")
print("-" * 30)

# Ejemplo 1: Validar edad para votar
edad = 20
tiene_cedula = True
puede_votar = (edad >= 18) and tiene_cedula

print(f"Edad: {edad}, Tiene cédula: {tiene_cedula}")
print(f"¿Puede votar? (edad >= 18 AND tiene_cedula): {puede_votar}")

# Ejemplo 2: Aprobación de materia
nota1 = 65
nota2 = 40
nota3 = 80

aprobado = (nota1 >= 60) and (nota2 >= 60) and (nota3 >= 60)
recupera = (nota1 < 60) or (nota2 < 60) or (nota3 < 60)

print(f"\nNotas: {nota1}, {nota2}, {nota3}")
print(f"¿Aprobó todas? (AND): {aprobado}")
print(f"¿Tiene que recuperar alguna? (OR): {recupera}")

print("\n" + "=" * 70)
print("PARTE 7: CONVERSIONES ENTRE TIPOS DE DATOS")
print("=" * 70)

print("\n7.1 CONVERSIONES BÁSICAS:")
print("-" * 30)

# De texto a números
texto_numero = "100"
print(f"Texto: '{texto_numero}' → Tipo: {type(texto_numero)}")

entero_desde_texto = int(texto_numero)
print(f"int('{texto_numero}') = {entero_desde_texto} → Tipo: {type(entero_desde_texto)}")

decimal_desde_texto = float(texto_numero)
print(f"float('{texto_numero}') = {decimal_desde_texto} → Tipo: {type(decimal_desde_texto)}")

# De números a texto
numero = 50
print(f"\nNúmero: {numero} → Tipo: {type(numero)}")

texto_desde_numero = str(numero)
print(f"str({numero}) = '{texto_desde_numero}' → Tipo: {type(texto_desde_numero)}")

# Conversiones entre números
decimal = 3.99
print(f"\nDecimal: {decimal} → Tipo: {type(decimal)}")

entero_desde_decimal = int(decimal)  # Trunca, no redondea
print(f"int({decimal}) = {entero_desde_decimal} → Tipo: {type(entero_desde_decimal)}")

# Booleanos desde números
print(f"\nDesde números a booleanos:")
print(f"bool(0) = {bool(0)}")      # 0 es False
print(f"bool(1) = {bool(1)}")      # 1 es True
print(f"bool(100) = {bool(100)}")  # Cualquier número ≠ 0 es True
print(f"bool(-5) = {bool(-5)}")    # Incluyendo negativos

print("\n7.2 CONVERSIONES CON ENTRADAS DE USUARIO:")
print("-" * 30)

# Ejemplo simulado (sin input real)
print("(Simulación de entrada de usuario)")
edad_texto = "20"  # Simula input("Ingrese su edad: ")
edad_numero = int(edad_texto)

print(f"Entrada del usuario: '{edad_texto}'")
print(f"Convertido a entero: {edad_numero}")
print(f"Edad en 5 años: {edad_numero + 5}")

print("\n" + "=" * 70)
print("PARTE 8: EJEMPLOS COMPLETOS PRÁCTICOS")
print("=" * 70)

print("\n8.1 CALCULADORA COMPLETA (sin funciones):")
print("-" * 40)

# Valores para calcular
num1 = 15
num2 = 4

print(f"NÚMERO 1: {num1}")
print(f"NÚMERO 2: {num2}")
print("-" * 30)

# Todas las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division_decimal = num1 / num2
division_entera = num1 // num2
resto_division = num1 % num2
potencia = num1 ** 2

print(f"SUMA:           {num1} + {num2} = {suma}")
print(f"RESTA:          {num1} - {num2} = {resta}")
print(f"MULTIPLICACIÓN: {num1} × {num2} = {multiplicacion}")
print(f"DIVISIÓN:       {num1} ÷ {num2} = {division_decimal}")
print(f"DIVISIÓN ENTERA: {num1} // {num2} = {division_entera}")
print(f"RESTO:          {num1} % {num2} = {resto_division}")
print(f"POTENCIA:       {num1}² = {potencia}")

print("\n8.2 CÁLCULO DE PROMEDIO Y ESTADO:")
print("-" * 40)

# Calificaciones
calificacion1 = 85
calificacion2 = 72
calificacion3 = 90

# Cálculos
suma_calificaciones = calificacion1 + calificacion2 + calificacion3
promedio = suma_calificaciones / 3

# Evaluación
aprobado = promedio >= 60
excelente = promedio >= 90
reprobado = promedio < 60

print(f"Calificación 1: {calificacion1}")
print(f"Calificación 2: {calificacion2}")
print(f"Calificación 3: {calificacion3}")
print("-" * 30)
print(f"Suma total: {suma_calificaciones}")
print(f"Promedio: {promedio:.2f}")
print("-" * 30)
print(f"¿Aprobado? (>= 60): {aprobado}")
print(f"¿Excelente? (>= 90): {excelente}")
print(f"¿Reprobado? (< 60): {reprobado}")

print("\n8.3 MANEJO DE CADENAS Y CONCATENACIÓN:")
print("-" * 40)

nombre = "Juan"
apellido = "Pérez"
edad = 21
altura = 1.75

# Concatenación básica
nombre_completo = nombre + " " + apellido

# Conversión para concatenación
edad_texto = str(edad)
altura_texto = str(altura)

# Mensaje completo
mensaje = "Estudiante: " + nombre_completo + ", Edad: " + edad_texto + ", Altura: " + altura_texto + "m"

print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Nombre completo: {nombre_completo}")
print(f"Mensaje completo: {mensaje}")

print("\n" + "=" * 70)
print("RESUMEN Y EJERCICIOS PRÁCTICOS")
print("=" * 70)

print("\nEJERCICIOS PARA PRACTICAR:")
print("-" * 30)
print("1. Calcular el área de un círculo con radio 5.5")
print("   Fórmula: área = π × radio²")
print("   Usar: pi = 3.1416")

print("\n2. Convertir 175 centímetros a pies y pulgadas")
print("   Fórmula: 1 cm = 0.3937 pulgadas")
print("           12 pulgadas = 1 pie")

print("\n3. Determinar si un número (ej: 17) es par o impar")
print("   Pista: Usar operador % (módulo)")

print("\n4. Calcular el IMC (Índice de Masa Corporal)")
print("   Fórmula: IMC = peso / altura²")
print("   Ejemplo: peso = 70kg, altura = 1.75m")

print("\n5. Convertir 90 grados Fahrenheit a Celsius")
print("   Fórmula: °C = (°F - 32) × 5/9")

print("\n" + "=" * 70)
print("¡EJECUCIÓN COMPLETADA!")
print("=" * 70)
print("\nResumen de temas vistos:")
print("1. Operadores aritméticos y precedencia")
print("2. Tipos de datos primitivos")
print("3. Sistemas numéricos (decimal, binario, hexadecimal)")
print("4. Operadores de comparación y lógicos")
print("5. Conversiones entre tipos")
print("6. Ejemplos prácticos completos")