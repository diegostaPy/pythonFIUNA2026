"""
============================================================
LO MÁS IMPORTANTE DE NUMPY - Script para clase
============================================================
"""

import numpy as np

print("=" * 50)
print("1. CREAR ARRAYS - La base de todo")
print("=" * 50)

# Desde listas
arr_lista = np.array([1, 2, 3, 4, 5])
print("Desde lista:", arr_lista)

# Ceros y unos
print("Ceros 2x3:\n", np.zeros((2, 3)))
print("Unos 2x2:\n", np.ones((2, 2)))

# Secuencias
print("arange:", np.arange(0, 10, 2))        # inicio, fin, paso
print("linspace:", np.linspace(0, 1, 5))     # inicio, fin, num_muestras

# Aleatorios
print("Aleatorio 2x2:\n", np.random.randint(0, 100, (2, 2)))

print("\n" + "=" * 50)
print("2. ATRIBUTOS BÁSICOS - Conoce tu array")
print("=" * 50)

a = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", a)
print("Forma:", a.shape)         # dimensiones
print("Dimensiones:", a.ndim)    # número de ejes
print("Total elementos:", a.size)
print("Tipo de dato:", a.dtype)

print("\n" + "=" * 50)
print("3. INDEXACIÓN Y SLICING - Accede a tus datos")
print("=" * 50)

matriz = np.array([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])

print("Matriz:\n", matriz)
print("Elemento [1,2]:", matriz[1, 2])       # fila 1, columna 2
print("Fila 0:", matriz[0, :])                # toda la primera fila
print("Columna 1:", matriz[:, 1])             # toda la segunda columna
print("Submatriz 2x2:\n", matriz[1:, 1:])     # desde fila 1, columna 1

# Indexación booleana
print("Elementos > 50:", matriz[matriz > 50])

print("\n" + "=" * 50)
print("4. OPERACIONES VECTORIZADAS - Sin bucles")
print("=" * 50)

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("Suma:", a + b)
print("Resta:", b - a)
print("Multiplicación:", a * b)
print("División:", b / a)

# Funciones universales (ufunc)
print("Cuadrado:", np.square(a))
print("Raíz:", np.sqrt(b))
print("Seno:", np.sin(a))
print("Exponencial:", np.exp(a))

print("\n" + "=" * 50)
print("5. FUNCIONES ESTADÍSTICAS - Analiza tus datos")
print("=" * 50)

datos = np.array([15, 22, 18, 30, 25, 28, 19, 35])
print("Datos:", datos)
print("Suma:", datos.sum())
print("Media:", datos.mean())
print("Mínimo:", datos.min())
print("Máximo:", datos.max())
print("Desviación estándar:", datos.std())

# Por eje
matriz = np.array([[1, 2, 3],
                    [4, 5, 6]])
print("Matriz:\n", matriz)
print("Suma por filas:", matriz.sum(axis=1))
print("Máximo por columnas:", matriz.max(axis=0))

print("\n" + "=" * 50)
print("6. CAMBIO DE FORMA - Manipula tus arrays")
print("=" * 50)

arr = np.arange(12)
print("Original:", arr)
print("reshape 3x4:\n", arr.reshape(3, 4))
print("reshape 2x6:\n", arr.reshape(2, 6))
print("Aplanado:", arr.ravel())

print("\n" + "=" * 50)
print("7. CONCATENAR Y APILAR - Une tus datos")
print("=" * 50)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Horizontal:", np.hstack((a, b)))
print("Vertical:\n", np.vstack((a, b)))
print("Concatenar:", np.concatenate((a, b)))

print("\n" + "=" * 50)
print("8. ÁLGEBRA LINEAL - Producto punto")
print("=" * 50)

m1 = np.array([[1, 2],
                [3, 4]])
m2 = np.array([[5, 6],
                [7, 8]])

print("Producto punto:\n", np.dot(m1, m2))
print("Matmul:\n", np.matmul(m1, m2))
print("Transpuesta:\n", m1.T)

print("\n" + "=" * 50)
print("9. EJEMPLO REAL COMPACTO - Análisis de datos")
print("=" * 50)

# Simular notas de 5 estudiantes en 3 materias
notas = np.random.randint(40, 100, (5, 3))
print("Notas (5 estudiantes x 3 materias):\n", notas)

# Promedio por estudiante
promedios = notas.mean(axis=1)
print("Promedio por estudiante:", promedios)

# ¿Quiénes aprueban? (promedio >= 60)
aprobados = promedios >= 60
print("¿Aprueba?:", aprobados)

# Nota más alta por materia
print("Nota máxima por materia:", notas.max(axis=0))

print("\n¡Fin del resumen de NumPy!")