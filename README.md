# Proyecto Galaxia

## Descripción

Este proyecto calcula la longitud de la órbita de Mercurio utilizando métodos de integración numérica.

La órbita se modela como una elipse y su longitud se aproxima mediante la Regla del Trapecio y la Regla de Simpson 1/3.

---

## Modelo matemático

La posición está dada por:

r(θ) = a·sin(θ) i + b·cos(θ) j

La longitud de la órbita se calcula con:

s = ∫₀²π √(a² cos²θ + b² sin²θ) dθ

---

## Métodos numéricos

### Regla del Trapecio

Aproxima el área bajo la curva mediante segmentos lineales.
Orden de error: O(h²)

### Regla de Simpson 1/3

Utiliza aproximaciones cuadráticas para mejorar la precisión.
Orden de error: O(h⁴)

---

## Datos utilizados

* Semieje mayor: a = 0.387 UA

* Excentricidad: e = 0.206

* Semieje menor:
  b = a √(1 − e²)

* 1 UA = 150,000,000 km

---

## Resultados

| Método   | Longitud (UA) | Longitud (km) |
| -------- | ------------- | ------------- |
| Trapecio | ≈ 2.4056      | ≈ 360,838,000 |
| Simpson  | ≈ 2.4056      | ≈ 360,838,000 |

---

## Ejecución

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPO>
```

2. Ejecutar el programa:

```bash
python main.py
```

---

## Estructura del proyecto

```
ProyectoGalaxia/
│
├── NumericIntegrationMethods/
│   ├── Trapecio.py
│   ├── Simpson.py
│   └── __init__.py
│
├── main.py
└── README.md

## Conclusión

Los métodos numéricos permiten aproximar integrales que no tienen solución analítica simple.
En este caso, ambos métodos convergen a un valor muy similar, lo que valida la precisión del cálculo.

Autores: Sergio Uriel Bustamante, Max Emiliano Sotelo, Romina Moreno Ramos


