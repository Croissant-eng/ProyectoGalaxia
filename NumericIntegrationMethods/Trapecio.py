def Trapecio(fx, Intervalos : list, n):
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