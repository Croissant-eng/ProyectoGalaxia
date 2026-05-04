def simpson_compuesto(fx, Intervalos: list, n: int) -> float:
    """
    Regla Compuesta de Simpson 1/3 para integración numérica.
    
    Fórmula:
        ∫[a,b] f(x) dx ≈ (h/3)[f(x₀) + 4·Σf(xᵢ) + 2·Σf(xᵢ) + f(xₙ)]
        donde:
        - Primer sumatoria: i = 1, 3, 5, ..., n-1 (índices impares)
        - Segunda sumatoria: i = 2, 4, 6, ..., n-2 (índices pares)
    
    Parámetros:
    -----------
    fx : callable
        Función a integrar
    Intervalos : list
        [a, b] - Límites de integración
    n : int
        Número de subintervalos (DEBE SER PAR)
    
    Retorna:
    --------
    float
        Aproximación de la integral
    
    Lanza:
    ------
    ValueError
        Si n no es par
    """
    if n % 2 != 0:
        raise ValueError('n debe ser par para la Regla Compuesta de Simpson 1/3')
    
    a = Intervalos[0]
    b = Intervalos[1]
    h = (b - a) / n
    
    # Generar puntos xi
    xi = [a + i * h for i in range(n + 1)]
    
    # Aplicar fórmula compuesta de Simpson
    suma = fx(xi[0]) + fx(xi[-1])  # f(x₀) + f(xₙ)
    
    # Puntos impares (i = 1, 3, 5, ...) con coeficiente 4
    for i in range(1, n, 2):
        suma += 4 * fx(xi[i])
    
    # Puntos pares (i = 2, 4, 6, ..., n-2) con coeficiente 2
    for i in range(2, n - 1, 2):
        suma += 2 * fx(xi[i])
    
    area = (h / 3) * suma
    
    return area