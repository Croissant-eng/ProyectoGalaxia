import numpy as np

# Importar funciones
from NumericIntegrationMethods.Trapecio import trapecio_compuesto
from NumericIntegrationMethods.Simpson import simpson_compuesto

print("Cálculo de la longitud de la órbita de Mercurio")

# Datos
a = 0.387
e = 0.206
b = a * np.sqrt(1 - e**2)

# Función a integrar
def f(theta):
    return np.sqrt(a**2 * np.cos(theta)**2 + b**2 * np.sin(theta)**2)

# Intervalo y subintervalos
intervalo = [0, 2 * np.pi]
n = 10  # debe ser par para Simpson

# Aplicar métodos
res_trap = trapecio_compuesto(f, intervalo, n)
res_simp = simpson_compuesto(f, intervalo, n)

# Conversión
UA_km = 150_000_000

# Resultados
print("\n--- RESULTADOS ---")
print(f"Trapecio (UA): {res_trap:.6f}")
print(f"Simpson  (UA): {res_simp:.6f}")

print(f"Trapecio (km): {res_trap * UA_km:.2f}")
print(f"Simpson  (km): {res_simp * UA_km:.2f}")
