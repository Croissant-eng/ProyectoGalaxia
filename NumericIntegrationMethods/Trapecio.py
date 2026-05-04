def trapecio_compuesto(fx, Intervalos: list, n: int) -> float:
    """
    Regla Compuesta del Trapecio para integración numérica.
    
    Fórmula:
        ∫[a,b] f(x) dx ≈ (h/2)[f(x₀) + 2·Σf(xᵢ) + f(xₙ)]
        donde i = 1, 2, ..., n-1
    
    Parámetros:
    -----------
    fx : callable
        Función a integrar
    Intervalos : list
        [a, b] - Límites de integración
    n : int
        Número de subintervalos
    
    Retorna:
    --------
    float
        Aproximación de la integral
    """
    a = Intervalos[0]
    b = Intervalos[1]
    h = (b - a) / n
    
    # Generamos puntos xi
    xi = [a + i * h for i in range(n + 1)]
    
    # Aplicamos fórmula compuesta del trapecio
    suma = fx(xi[0]) + fx(xi[-1])  # f(x₀) + f(xₙ)
    
    # Suma de los puntos interiores con coeficiente 2
    for i in range(1, n):
        suma += 2 * fx(xi[i])
    
    area = (h / 2) * suma
    
    return area