import numpy as np

from NumericIntegrationMethods.Trapecio import Trapecio
from NumericIntegrationMethods.Simpson import Simpson

print("Cálculo de la longitud de la órbita de Mercurio")

a = 0.387
e = 0.206
b = a * np.sqrt(1 - e**2)

def f(theta):
    return np.sqrt(a**2 * np.cos(theta)**2 + b**2 * np.sin(theta)**2)

intervalo = [0, 2*np.pi]
n = 10

res_trap = Trapecio(f, intervalo, n)
res_simp = Simpson(f, intervalo, n)

UA_km = 150000000

print("\n--- RESULTADOS ---")
print("Trapecio (UA):", res_trap)
print("Simpson (UA):", res_simp)

print("Trapecio (km):", res_trap * UA_km)
print("Simpson (km):", res_simp * UA_km)
