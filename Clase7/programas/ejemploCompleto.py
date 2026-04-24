"""
============================================================
CLASE: Manejo de Archivos y Visualización de Datos en Python
============================================================
"""

# ============================================================
# 1. IMPORTS NECESARIOS
# ============================================================
import numpy as np
import matplotlib.pyplot as plt

# Configuración global de gráficos
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("📊 Librerías cargadas exitosamente\n")


# ============================================================
# 2. MANEJO DE ARCHIVOS
# ============================================================

# 2.1 Escritura de archivo de ejemplo
print("=== MANEJO DE ARCHIVOS ===\n")
print("2.1 Creando archivo de datos...")

datos_ejemplo = np.random.randint(1, 100, 20)
np.savetxt('datos_clase.txt', datos_ejemplo, fmt='%d')
print(f"   Archivo 'datos_clase.txt' creado con {len(datos_ejemplo)} valores\n")

# 2.2 Lectura segura con manejo de excepciones
print("2.2 Leyendo archivo de forma segura...")

nombre_archivo = 'datos_clase.txt'
try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.readlines()
    print(f"   ✅ Archivo '{nombre_archivo}' leído correctamente")
    print(f"   Primeras 5 líneas: {contenido[:5]}")
except FileNotFoundError:
    print(f"   ❌ El archivo '{nombre_archivo}' no existe")
except PermissionError:
    print(f"   ❌ No tienes permiso para leer '{nombre_archivo}'")
finally:
    print("   Operación de lectura finalizada.\n")

# 2.3 Lectura con NumPy
print("2.3 Leyendo datos con NumPy...")

try:
    datos = np.loadtxt('datos_clase.txt')
    print(f"   ✅ Datos cargados con np.loadtxt")
    print(f"   Array: {datos}")
    print(f"   Media: {np.mean(datos):.2f}")
    print(f"   Desviación: {np.std(datos):.2f}\n")
except FileNotFoundError:
    print("   ❌ Archivo no encontrado\n")


# ============================================================
# 3. CONCEPTOS BÁSICOS DE MATPLOTLIB
# ============================================================
print("=== INTRODUCCIÓN A MATPLOTLIB ===\n")

# 3.1 Primer gráfico: Figura y Ejes
print("3.1 Creando figura y ejes...")

x = np.linspace(0, 10, 100)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y, color='blue', linewidth=2)
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Mi Primer Gráfico: y = x²')
ax.grid(True, alpha=0.3)
plt.show()
print("   ✅ Primer gráfico mostrado\n")


# ============================================================
# 4. TIPOS DE GRÁFICOS
# ============================================================
print("=== TIPOS DE GRÁFICOS ===\n")

# 4.1 Gráfico de Líneas
print("4.1 Gráfico de líneas: función seno y coseno")

x = np.arange(0, 2 * np.pi, 0.1)
y_sen = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y_sen, color='blue', linestyle='-', linewidth=2, label='Sen(x)')
ax.plot(x, y_cos, color='red', linestyle='--', linewidth=2, label='Cos(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Funciones Trigonométricas')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()
fig.savefig('lineas.png', dpi=150)
print("   ✅ Guardado como 'lineas.png'\n")


# 4.2 Gráfico de Barras
print("4.2 Gráfico de barras: ventas por trimestre")

categorias = ['Q1', 'Q2', 'Q3', 'Q4']
ventas = [23000, 45000, 56000, 78000]

fig, ax = plt.subplots()
barras = ax.bar(categorias, ventas, color='skyblue', edgecolor='black', linewidth=1.5)
ax.set_xlabel('Trimestre')
ax.set_ylabel('Ventas ($)')
ax.set_title('Ventas Trimestrales 2024')
# Agregar valores sobre cada barra
for barra, valor in zip(barras, ventas):
    ax.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 1000,
            f'${valor:,}', ha='center', va='bottom', fontsize=10)
plt.show()
print("   ✅ Gráfico de barras mostrado\n")


# 4.3 Histograma
print("4.3 Histograma: distribución de datos")

datos_normal = np.random.normal(100, 15, 1000)

fig, ax = plt.subplots()
ax.hist(datos_normal, bins=25, color='lightgreen', edgecolor='black', alpha=0.7)
ax.axvline(np.mean(datos_normal), color='red', linestyle='--', linewidth=2,
           label=f'Media: {np.mean(datos_normal):.1f}')
ax.set_xlabel('Valor')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma de Datos con Distribución Normal')
ax.legend()
plt.show()
print(f"   ✅ Histograma mostrado - Media de los datos: {np.mean(datos_normal):.2f}\n")


# 4.4 Gráfico de Dispersión (Scatter)
print("4.4 Gráfico de dispersión: relación entre variables")

np.random.seed(42)
x_scatter = np.random.uniform(0, 10, 100)
y_scatter = 2 * x_scatter + 1 + np.random.normal(0, 2, 100)

fig, ax = plt.subplots()
scatter = ax.scatter(x_scatter, y_scatter, c='purple', alpha=0.6, s=50, edgecolors='black')
ax.set_xlabel('Variable X')
ax.set_ylabel('Variable Y')
ax.set_title('Gráfico de Dispersión: Relación Lineal con Ruido')
ax.grid(True, alpha=0.3)
plt.show()
print("   ✅ Gráfico de dispersión mostrado\n")


# 4.5 Boxplot (Diagrama de Caja)
print("4.5 Boxplot: comparación entre grupos")

# Generar datos para 4 grupos
grupo1 = np.random.normal(70, 10, 100)
grupo2 = np.random.normal(75, 12, 100)
grupo3 = np.random.normal(80, 8, 100)
grupo4 = np.random.normal(78, 15, 100)
datos_box = [grupo1, grupo2, grupo3, grupo4]

fig, ax = plt.subplots()
bp = ax.boxplot(datos_box, patch_artist=True, labels=['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D'])
colores = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
for caja, color in zip(bp['boxes'], colores):
    caja.set_facecolor(color)
ax.set_xlabel('Grupos')
ax.set_ylabel('Valores')
ax.set_title('Boxplot: Comparación entre Grupos')
ax.grid(True, alpha=0.3, axis='y')
plt.show()
print("   ✅ Boxplot mostrado\n")


# 4.6 Visualización de Imágenes
print("4.6 Visualización de matriz como imagen")

# Crear matriz con patrón
matriz = np.fromfunction(lambda i, j: np.sin(i/3) * np.cos(j/3), (30, 30))

fig, ax = plt.subplots()
im = ax.imshow(matriz, cmap='coolwarm', interpolation='bilinear', aspect='auto')
plt.colorbar(im, ax=ax, label='Valor')
ax.set_title('Visualización de Patrón con imshow()')
ax.set_xlabel('Columna')
ax.set_ylabel('Fila')
plt.show()
print("   ✅ Imagen de matriz mostrada\n")


# ============================================================
# 5. SUBPLOTS (MÚLTIPLES GRÁFICOS)
# ============================================================
print("=== SUBPLOTS: MÚLTIPLES GRÁFICOS EN UNA FIGURA ===\n")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Dashboard de Análisis', fontsize=16, fontweight='bold')

# Gráfico 1: Líneas
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x), color='blue')
axes[0, 0].set_title('Función Seno')
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('sen(x)')
axes[0, 0].grid(True, alpha=0.3)

# Gráfico 2: Histograma
datos = np.random.normal(0, 1, 500)
axes[0, 1].hist(datos, bins=20, color='green', edgecolor='black', alpha=0.7)
axes[0, 1].set_title('Histograma Normal')
axes[0, 1].set_xlabel('Valor')
axes[0, 1].set_ylabel('Frecuencia')

# Gráfico 3: Barras
cat = ['A', 'B', 'C', 'D']
val = [23, 45, 56, 78]
axes[1, 0].bar(cat, val, color='orange', edgecolor='black')
axes[1, 0].set_title('Gráfico de Barras')
axes[1, 0].set_xlabel('Categoría')
axes[1, 0].set_ylabel('Valor')

# Gráfico 4: Dispersión
x_s = np.random.uniform(0, 10, 50)
y_s = x_s + np.random.normal(0, 1, 50)
axes[1, 1].scatter(x_s, y_s, color='red', alpha=0.6)
axes[1, 1].set_title('Dispersión')
axes[1, 1].set_xlabel('X')
axes[1, 1].set_ylabel('Y')

plt.tight_layout()
plt.show()
fig.savefig('dashboard.png', dpi=200)
print("✅ Dashboard guardado como 'dashboard.png'\n")


# ============================================================
# 6. APLICACIÓN INTEGRADORA: VISUALIZACIÓN DE ORDENAMIENTO
# ============================================================
print("=== APLICACIÓN INTEGRADORA ===\n")
print("Visualización del algoritmo de ordenamiento burbuja...\n")

def ordenamiento_burbuja(arr):
    """Ordena un array y guarda todos los pasos intermedios"""
    n = len(arr)
    pasos = [arr.copy()]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                pasos.append(arr.copy())
    return pasos

# Generar array aleatorio
array = np.random.randint(1, 100, 15)
print(f"Array original: {array}\n")

# Obtener pasos del ordenamiento
pasos = ordenamiento_burbuja(array.copy())

# Visualizar
fig, ax = plt.subplots(figsize=(12, 6))

for i, paso in enumerate(pasos):
    ax.clear()
    colores = ['skyblue'] * len(paso)
    
    # Marcar elementos ya ordenados al final
    if i > 0:
        for k in range(len(paso) - (i-1)//len(paso), len(paso)):
            if k >= 0 and k < len(paso):
                colores[k] = 'lightgreen'
    
    ax.bar(range(len(paso)), paso, color=colores, edgecolor='black')
    ax.set_title(f'Ordenamiento Burbuja - Paso {i+1} de {len(pasos)}', fontsize=14)
    ax.set_xlabel('Índice')
    ax.set_ylabel('Valor')
    ax.set_xticks(range(len(paso)))
    ax.set_ylim(0, 105)
    
    plt.pause(0.3)
    plt.draw()

plt.show()
print(f"✅ Array ordenado: {pasos[-1]}")
print("✅ Visualización completada\n")
