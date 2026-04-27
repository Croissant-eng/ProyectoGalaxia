def Trapecio(fx, Intervalos : list, n : int):
    
    """
    Esta función nos ayuda a calcular el área aproximada
    de una integral que no tiene un valor exacto por el método de
    integración numérica de la Regla del Trapecio.
    
    Su fórmula es:
    (h/2)[f(x0) + 2*f(x1) + 2*f(x2) + ... + 2*f(xn-1) + f(xn)]
    
    donde:
    - h = (b - a) / n
    - xi = a + i*h para i = 0, 1, 2, ..., n
    
    Parámetros:
    -----------
    fx : function
        Función a integrar. Debe aceptar un valor numérico y retornar un número.
    Intervalos : list
        Lista de dos elementos [a, b] que definen los límites de integración.
        a : límite inferior
        b : límite superior
    n : int
        Número de subintervalos a utilizar en la aproximación.
        Mientras mayor sea n, más precisa será la aproximación.
    
    Retorna:
    --------
    float
        El valor aproximado del área bajo la curva (integral definida).
    
    Ejemplo:
    --------
    >>> f = lambda x: x**2
    >>> resultado = trapecio(f, [0, 1], 100)
    >>> print(f"{resultado:.6f}")
    0.333350  # Aproximado a 1/3
    
    Notas:
    ------
    - El método del trapecio aproxima el área bajo la curva dividiéndola
      en n trapecios y sumando sus áreas individuales.
    - El error de aproximación es proporcional a h² (orden O(h²)).
    """

    # Definimos las variables de A, xi y deltaX ya con su valor
    Area = 0
    xi = []
    deltaX = (Intervalos[1]-Intervalos[0])/n

    # Declaramos cada valor de xi
    for i in range(0, n+1):
        xn = Intervalos[0] + i * deltaX
        xi.append(xn)

    # Aproximamos el valor del area por el metodo de Trapecio
    for i in range(n):
        areaTrapecio = (deltaX / 2) * (fx(xi[i]) + fx(xi[i+1]))
        Area += areaTrapecio
    return Area