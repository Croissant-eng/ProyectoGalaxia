def Simpson(fx, Intervalos : list, n : int):
    """
    Calcula la integral definida de una función utilizando la Regla de Simpson 1/3.
    
    Este método aproxima el área bajo la curva dividiendo el intervalo [a, b] en 'n'
    subintervalos y evaluando la función en los extremos, puntos interiores y puntos
    medios de cada subintervalo. Es significativamente más preciso que la regla del
    trapecio para funciones suaves.
    
    Fórmula implementada:
        ∫[a,b] f(x) dx ≈ ((b-a) / 6n) * [f(x₀) + 4Σf(xᵢ) + 2Σf(xᵢ) + f(xₙ)]
        donde:
        - x̄ = (xᵢ + xᵢ₊₁) / 2  (puntos medios)
        - xᵢ = a + i*h,  h = (b-a)/n
    
    Parámetros:
    -----------
    fx : callable
        Función a integrar. Debe recibir un valor numérico (float) y retornar un float.
    Intervalos : list[float, float]
        Lista con dos elementos [a, b] que definen los límites de integración.
        a : límite inferior
        b : límite superior
    n : int
        Número de subintervalos. Debe ser un entero par positivo.
    
    Retorna:
    --------
    float
        Valor aproximado de la integral definida en el intervalo dado.
    
    Lanza:
    ------
    ValueError
        Si 'n' no es un número par, ya que la Regla de Simpson 1/3 requiere
        un número par de subintervalos para ajustar parábolas correctamente.
    
    Ejemplo:
    --------
    >>> import math
    >>> f = lambda x: math.sin(x)
    >>> Simpson(f, [0, math.pi], 10)
    2.000109517...  # El valor exacto es 2.0
    
    Notas:
    ------
    - Esta implementación utiliza la forma equivalente con puntos medios, 
      matemáticamente idéntica a la fórmula clásica: (h/3)[f₀ + 4f₁ + 2f₂ + ... + fₙ]
    - El error de truncamiento es de orden O(h⁴), lo que garantiza mayor precisión
      que el método del trapecio O(h²) con el mismo número de evaluaciones.
    - Se recomienda usar n ≥ 10 para funciones con curvatura pronunciada.
    """
    
    # Verificar que n sea par
    if n % 2 != 0:
        raise ValueError('n debe ser par')
    
    # Inicializar listas
    xi = []
    xmi = []
    
    # Calcular h
    h = (Intervalos[1] - Intervalos[0]) / n
    
    # Generar puntos xi (CORREGIDO)
    for i in range(n + 1):
        x_i = Intervalos[0] + i * h
        xi.append(x_i)
    
    # Generar puntos medios
    for i in range(n):
        xm_i = (xi[i] + xi[i + 1]) / 2
        xmi.append(xm_i)
    
    # Evaluar f(x) en puntos interiores (i=1 hasta n-1)
    fxi = [fx(xi[i]) for i in range(1, n)]
    
    # Evaluar f(x) en puntos medios
    fxmi = [fx(xmi[i]) for i in range(n)]
    
    # Calcular sumatorias
    sum_xi = sum(fxi)
    sum_xmi = sum(fxmi)
    
    # Aplicar fórmula de Simpson
    AreaAprox = ((xi[-1] - xi[0]) / (6 * n)) * (
        fx(xi[0]) + 4 * sum_xmi + 2 * sum_xi + fx(xi[-1])
    )
    
    return AreaAprox