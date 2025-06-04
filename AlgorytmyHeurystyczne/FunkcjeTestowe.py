import numpy as np

#funkcje matematyczne testowe
def paraboloid(x):
    return x[0]**2 + x[1]**2

def rastrigin(x):
    A=10
    x = np.array(x)
    n = len(x)
    return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))

def rosenbrock(x):
    x = np.array(x)
    return sum(100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(len(x) - 1))

def hyper_ellipsoid(x):
    x = np.array(x)
    return sum(np.sum(x[:i+1])**2 for i in range(len(x)))

def shubert(x):
    x = np.array(x)
    wynik = 1
    for j in range(len(x)):
        suma = 0
        for i in range(1, 6):
            suma += i * np.cos((i + 1) * x[j] + i)
        wynik *= suma
    return wynik

def sphere(x):
    x = np.array(x)
    return np.sum(x**2)

def sum_squares(x):
    x = np.array(x)
    return np.sum([(i+1)*x[i]**2 for i in range(len(x))])

def styblinski_tang(x):
    x = np.array(x, dtype=np.float64)  # wymuszamy float64
    return 0.5 * np.sum(x**4 - 16 * x**2 + 5 * x)

def weierstrass(x, a=0.5, b=3, k_max=20):
    x = np.array(x)
    n = len(x)
    wynik = 0
    for i in range(n):
        for k in range(k_max + 1):
            wynik += a**k * np.cos(2 * np.pi * b**k * (x[i] + 0.5))
    wynik -= n * sum([a**k * np.cos(np.pi * b**k) for k in range(k_max + 1)])
    return wynik