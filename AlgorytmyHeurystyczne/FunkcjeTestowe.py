import numpy as np

# Funkcje testowe (z opisami zakresów i minimów)

def paraboloid(x):
    # Zakres: dowolny, typowo [-5, 5]
    # Minimum globalne: w x = [0, 0], f(x) = 0
    return x[0]**2 + x[1]**2

def rastrigin(x):
    # Zakres: [-5.12, 5.12]
    # Minimum globalne: w x = [0,...,0], f(x) = 0
    A = 10
    x = np.array(x)
    n = len(x)
    return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))

def rosenbrock(x):
    # Zakres: [-5, 10]
    # Minimum globalne: w x = [1,...,1], f(x) = 0
    x = np.array(x)
    return sum(100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(len(x) - 1))

def hyper_ellipsoid(x):
    # Zakres: dowolny, typowo [-5, 5]
    # Minimum globalne: w x = [0,...,0], f(x) = 0
    x = np.array(x)
    return sum(np.sum(x[:i+1])**2 for i in range(len(x)))

def shubert(x):
    # Zakres: [-10, 10]
    # Minimum globalne: wiele minimów, np. f(x) ≈ -186.7309 dla 2D
    x = np.array(x)
    wynik = 1
    for j in range(len(x)):
        suma = 0
        for i in range(1, 6):
            suma += i * np.cos((i + 1) * x[j] + i)
        wynik *= suma
    return wynik

def sphere(x):
    # Zakres: dowolny, typowo [-5, 5]
    # Minimum globalne: w x = [0,...,0], f(x) = 0
    x = np.array(x)
    return np.sum(x**2)

def sum_squares(x):
    # Zakres: dowolny, typowo [-5, 5]
    # Minimum globalne: w x = [0,...,0], f(x) = 0
    x = np.array(x)
    return np.sum([(i+1)*x[i]**2 for i in range(len(x))])

def styblinski_tang(x):
    # Zakres: [-5, 5]
    # Minimum globalne: około x = [-2.903534,...], f(x) ≈ -39.16599*n
    x = np.array(x, dtype=np.float64)
    return 0.5 * np.sum(x**4 - 16 * x**2 + 5 * x)

def weierstrass(x, a=0.5, b=3, k_max=20):
    # Zakres: [-0.5, 0.5]
    # Minimum globalne: w x = [0,...,0], f(x) ≈ -n
    x = np.array(x)
    n = len(x)
    wynik = 0
    for i in range(n):
        for k in range(k_max + 1):
            wynik += a**k * np.cos(2 * np.pi * b**k * (x[i] + 0.5))
    wynik -= n * sum([a**k * np.cos(np.pi * b**k) for k in range(k_max + 1)])
    return wynik

def beale(x):
    # Zakres: [-4.5, 4.5]
    # Minimum globalne: x = [3, 0.5], f(x) = 0
    if len(x) != 2:
        raise ValueError("Beale function is only defined for 2 dimensions.")
    x1, x2 = x
    term1 = (1.5 - x1 + x1 * x2) ** 2
    term2 = (2.25 - x1 + x1 * x2**2) ** 2
    term3 = (2.625 - x1 + x1 * x2**3) ** 2
    return term1 + term2 + term3

def griewank(x):
    # Zakres: [-600, 600]
    # Minimum globalne: x = [0,...,0], f(x) = 0
    x = np.array(x)
    sum_part = np.sum(x**2) / 4000
    prod_part = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))
    return sum_part - prod_part + 1

def ackley(x, a=20, b=0.2, c=2 * np.pi):
    # Zakres: [-5, 5]
    # Minimum globalne: x = [0,...,0], f(x) = 0
    x = np.array(x)
    n = len(x)
    sum_sq = np.sum(x**2)
    sum_cos = np.sum(np.cos(c * x))
    term1 = -a * np.exp(-b * np.sqrt(sum_sq / n))
    term2 = -np.exp(sum_cos / n)
    return term1 + term2 + a + np.exp(1)

def schwefel(x):
    # Zakres: [-500, 500]
    # Minimum globalne: x = [420.9687,...], f(x) ≈ 0
    x = np.array(x)
    return 418.9829 * len(x) - np.sum(x * np.sin(np.sqrt(np.abs(x))))

def michalewicz(x, m=10):
    # Zakres: [0, π]
    # Minimum globalne: trudne do określenia, zależne od m
    x = np.array(x)
    i = np.arange(1, len(x) + 1)
    return -np.sum(np.sin(x) * (np.sin(i * x**2 / np.pi)) ** (2 * m))

def zakharov(x):
    # Zakres: [-5, 10]
    # Minimum globalne: x = [0,...,0], f(x) = 0
    x = np.array(x)
    i = np.arange(1, len(x) + 1)
    sum1 = np.sum(x**2)
    sum2 = np.sum(0.5 * i * x)
    return sum1 + sum2**2 + sum2**4

def levy(x):
    # Zakres: [-10, 10]
    # Minimum globalne: x = [1,...,1], f(x) = 0
    x = np.array(x)
    return np.sum((x - 1)**2 * (1 + np.sin(3 * np.pi * x)**2))

def levy_n13(x):
    # Zakres: [-10, 10]
    # Minimum globalne: x = [1,...,1], f(x) = 0
    x = np.array(x)
    w = 1 + (x - 1) / 4
    term1 = np.sin(np.pi * w[0])**2
    term2 = np.sum((w[:-1] - 1)**2 * (1 + 10 * np.sin(np.pi * w[:-1] + 1)**2))
    term3 = (w[-1] - 1)**2 * (1 + np.sin(2 * np.pi * w[-1])**2)
    return term1 + term2 + term3

def bohachevsky(x):
    # Zakres: [-100, 100]
    # Minimum globalne: x = [0, 0], f(x) = 0
    if len(x) != 2:
        raise ValueError("Bohachevsky function is defined for 2D input.")
    x1, x2 = x
    return x1**2 + 2 * x2**2 - 0.3 * np.cos(3 * np.pi * x1) - 0.4 * np.cos(4 * np.pi * x2) + 0.7

def eggholder(x):
    # Zakres: [-512, 512]
    # Minimum globalne: x ≈ [512, 404.2319], f(x) ≈ -959.6407
    if len(x) != 2:
        raise ValueError("Eggholder function is defined for 2D input.")
    x1, x2 = x
    return -(x2 + 47) * np.sin(np.sqrt(np.abs(x2 + x1 / 2 + 47))) - x1 * np.sin(np.sqrt(np.abs(x1 - (x2 + 47))))

def holder_table(x):
    # Zakres: [-10, 10]
    # Minimum globalne: x ≈ [±8.05502, ±9.66459], f(x) ≈ -19.2085
    if len(x) != 2:
        raise ValueError("Holder Table function is only defined for 2D input.")
    x1, x2 = x
    return -abs(np.sin(x1) * np.cos(x2) * np.exp(abs(1 - np.sqrt(x1**2 + x2**2) / np.pi)))

def langermann(x):
    # Zakres: [0, 10]
    # Minimum globalne: około x ≈ [2.003, 1.994], f(x) ≈ -4.155
    x = np.array(x)
    if len(x) != 2:
        raise ValueError("Langermann function here is defined for 2D input.")
    a = np.array([[3, 5], [5, 2], [2, 1], [1, 4], [7, 9]])
    c = np.array([1, 2, 5, 2, 3])
    m = len(c)
    result = 0
    for i in range(m):
        diff = np.sum((x - a[i]) ** 2)
        result += c[i] * np.exp(-diff / np.pi) * np.cos(np.pi * diff)
    return -result

def drop_wave(x):
    # Zakres: [-5.12, 5.12]
    # Minimum globalne: x = [0, 0], f(x) = -1
    if len(x) != 2:
        raise ValueError("Drop-Wave function is only defined for 2D input.")
    x1, x2 = x
    numerator = 1 + np.cos(12 * np.sqrt(x1**2 + x2**2))
    denominator = 0.5 * (x1**2 + x2**2) + 2
    return - numerator / denominator

def three_hump_camel(x):
    # Zakres: [-5, 5]
    # Minimum globalne: x = [0, 0], f(x) = 0
    if len(x) != 2:
        raise ValueError("Three-Hump Camel function is only defined for 2D input.")
    x1, x2 = x
    return 2 * x1**2 - 1.05 * x1**4 + (x1**6) / 6 + x1 * x2 + x2**2

def six_hump_camel(x):
    # Zakres: x1 ∈ [-3, 3], x2 ∈ [-2, 2]
    # Minimum globalne: x ≈ [±0.0898, ∓0.7126], f(x) ≈ -1.0316
    if len(x) != 2:
        raise ValueError("Six-Hump Camel function is only defined for 2D input.")
    x1, x2 = x
    return (4 - 2.1 * x1**2 + (x1**4) / 3) * x1**2 + x1 * x2 + (-4 + 4 * x2**2) * x2**2

def dixon_price(x):
    # Zakres: [-10, 10]
    # Minimum globalne: x = [1, 2^(1/2), 2^(2/2), ..., 2^((n-1)/2)], f(x) = 0
    x = np.array(x)
    term1 = (x[0] - 1)**2
    term2 = np.sum((2 * x[1:]**2 - x[:-1])**2 * np.arange(2, len(x)+1))
    return term1 + term2

def booth(x):
    # Zakres: [-10, 10]
    # Minimum globalne: x = [1, 3], f(x) = 0
    if len(x) != 2:
        raise ValueError("Booth function is only defined for 2D input.")
    x1, x2 = x
    return (x1 + 2 * x2 - 7)**2 + (2 * x1 + x2 - 5)**2

def matyas(x):
    # Zakres: [-10, 10]
    # Minimum globalne: x = [0, 0], f(x) = 0
    if len(x) != 2:
        raise ValueError("Matyas function is only defined for 2D input.")
    x1, x2 = x
    return 0.26 * (x1**2 + x2**2) - 0.48 * x1 * x2

def mccormick(x):
    # Zakres: x1 ∈ [-1.5, 4], x2 ∈ [-3, 4]
    # Minimum globalne: x ≈ [-0.54719, -1.54719], f(x) ≈ -1.9133
    if len(x) != 2:
        raise ValueError("McCormick function is only defined for 2D input.")
    x1, x2 = x
    return np.sin(x1 + x2) + (x1 - x2)**2 - 1.5 * x1 + 2.5 * x2 + 1

def power_sum(x, b=None):
    # Zakres: dowolny, typowo [0, 1]
    # Minimum globalne: x = [1, 1/√2, 1/√3, ..., 1/√n], f(x) = 0
    x = np.array(x)
    n = len(x)
    if b is None:
        b = np.arange(1, n + 1)
    if len(b) != n:
        raise ValueError("Length of b must match length of x.")
    return np.sum((np.sum(x ** np.arange(1, n + 1)[:, None], axis=1) - b) ** 2)

def branin(x):
    # Zakres: x ∈ [-5, 10], y ∈ [0, 15]
    # Minimum globalne: ≈ 0.397887, w punktach około (-π, 12.275), (π, 2.275), (9.42478, 2.475)
    if len(x) != 2:
        raise ValueError("Branin function is defined for 2D input.")
    x1, x2 = x
    a = 1
    b = 5.1 / (4 * np.pi**2)
    c = 5 / np.pi
    r = 6
    s = 10
    t = 1 / (8 * np.pi)
    return a * (x2 - b * x1**2 + c * x1 - r)**2 + s * (1 - t) * np.cos(x1) + s

def colville(x):
    # Zakres: [-10, 10] dla każdej zmiennej
    # Minimum globalne: 0 w punkcie [1, 1, 1, 1]
    if len(x) != 4:
        raise ValueError("Colville function is defined for 4D input.")
    x1, x2, x3, x4 = x
    return (100 * (x1**2 - x2)**2 +
            (x1 - 1)**2 +
            (x3 - 1)**2 +
            90 * (x3**2 - x4)**2 +
            10.1 * ((x2 - 1)**2 + (x4 - 1)**2) +
            19.8 * (x2 - 1) * (x4 - 1))

def goldstein_price(x):
    # Zakres: x, y ∈ [-2, 2]
    # Minimum globalne: 3 w punkcie [0, -1]
    if len(x) != 2:
        raise ValueError("Goldstein-Price function is defined for 2D input.")
    x1, x2 = x
    a = (1 + (x1 + x2 + 1)**2 *
         (19 - 14 * x1 + 3 * x1**2 - 14 * x2 + 6 * x1 * x2 + 3 * x2**2))
    b = (30 + (2 * x1 - 3 * x2)**2 *
         (18 - 32 * x1 + 12 * x1**2 + 48 * x2 - 36 * x1 * x2 + 27 * x2**2))
    return a * b

def powell(x):
    # Zakres: [-4, 5] dla każdej zmiennej
    # Minimum globalne: 0 w punkcie [0, 0, 0, 0]
    if len(x) != 4:
        raise ValueError("Powell function is defined for 4D input.")
    x1, x2, x3, x4 = x
    return ((x1 + 10 * x2)**2 +
            5 * (x3 - x4)**2 +
            (x2 - 2 * x3)**4 +
            10 * (x1 - x4)**4)

def cross_in_tray(x):
    # Zakres: x, y ∈ [-10, 10]
    # Minimum globalne: ≈ -2.06261, w 4 punktach m.in. (±1.3491, ±1.3491)
    if len(x) != 2:
        raise ValueError("Cross-in-Tray function is defined for 2D input.")
    x1, x2 = x
    exp_term = np.exp(abs(100 - np.sqrt(x1**2 + x2**2) / np.pi))
    return -0.0001 * (abs(np.sin(x1) * np.sin(x2) * exp_term) + 1)**0.1

def schaffer_n2(x):
    # Zakres: x, y ∈ [-100, 100]
    # Minimum globalne: 0 w punkcie [0, 0]
    if len(x) != 2:
        raise ValueError("Schaffer N.2 function is defined for 2D input.")
    x1, x2 = x
    num = np.sin(x1**2 - x2**2)**2 - 0.5
    denom = (1 + 0.001 * (x1**2 + x2**2))**2
    return 0.5 + num / denom

def schaffer_n4(x):
    # Zakres: x, y ∈ [-100, 100]
    # Minimum globalne: ≈ 0.292579 w punkcie [0, 1.25313]
    if len(x) != 2:
        raise ValueError("Schaffer N.4 function is defined for 2D input.")
    x1, x2 = x
    num = np.cos(np.sin(abs(x1**2 - x2**2)))**2 - 0.5
    denom = (1 + 0.001 * (x1**2 + x2**2))**2
    return 0.5 + num / denom

def bukin_n6(x):
    # Zakres: x1 ∈ [-15, -5], x2 ∈ [-3, 3]
    # Minimum globalne: 0 w punkcie [-10, 1]
    if len(x) != 2:
        raise ValueError("Bukin N.6 function is defined for 2D input.")
    x1, x2 = x
    return 100 * np.sqrt(np.abs(x2 - 0.01 * x1**2)) + 0.01 * np.abs(x1 + 10)

def perm_function(x, beta=10):
    # Zakres: [-d, d] dla każdej zmiennej
    # Minimum globalne: 0 w punkcie [1, 2, ..., d]
    x = np.array(x)
    d = len(x)
    i = np.arange(1, d + 1)
    result = 0
    for j in range(1, d + 1):
        inner = np.sum((i**j + beta) * ((x / i)**j - 1))
        result += inner**2
    return result

def sum_different_powers(x):
    # Zakres: [-1, 1] dla każdej zmiennej
    # Minimum globalne: 0 w punkcie [0, ..., 0]
    x = np.array(x)
    exponents = np.arange(2, len(x) + 2)
    return np.sum(np.abs(x)**exponents)

def trid(x):
    # Zakres: [-d^2, d^2] gdzie d to liczba wymiarów
    # Minimum globalne: -d(d+4)(d-1)/6 w punkcie [i for i in range(1, d+1)]
    x = np.array(x)
    sum1 = np.sum((x - 1)**2)
    sum2 = np.sum(x[1:] * x[:-1])
    return sum1 - sum2

def dejong_n5(x):
    # Zakres: [-65.536, 65.536]
    # Minimum globalne: ≈ 1 w punkcie (-32, -32)
    if len(x) != 2:
        raise ValueError("De Jong Function N.5 is defined for 2D input.")
    x = np.array(x)
    a = np.array([[-32, -16, 0, 16, 32]] * 5).T.flatten()
    b = np.array([[-32] * 5, [-16] * 5, [0] * 5, [16] * 5, [32] * 5]).flatten()
    total = 0
    for j in range(25):
        total += 1 / (j + 1 + (x[0] - a[j])**6 + (x[1] - b[j])**6)
    return 1 / (0.002 + total)

def easom(x):
    # Zakres: x ∈ [-100, 100]
    # Minimum globalne: -1 w punkcie (π, π)
    if len(x) != 2:
        raise ValueError("Easom function is defined for 2D input.")
    x1, x2 = x
    return -np.cos(x1) * np.cos(x2) * np.exp(-((x1 - np.pi)**2 + (x2 - np.pi)**2))

def shekel(x, m=10):
    # Zakres: [0, 10] dla każdego wymiaru (zwykle 4D)
    # Minimum globalne zależy od m, przy m=10 ~ -10.5364
    x = np.array(x)
    if len(x) != 4:
        raise ValueError("Shekel function is defined for 4-dimensional input.")

    C = np.array([
        [4, 1, 8, 6, 3, 2, 5, 8, 6, 7],
        [4, 1, 8, 6, 7, 9, 5, 1, 2, 3],
        [4, 1, 8, 6, 3, 2, 3, 8, 6, 7],
        [4, 1, 8, 6, 7, 9, 3, 1, 2, 3]
    ])
    beta = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5])

    result = 0
    for i in range(m):
        result += 1 / (np.sum((x - C[:, i]) ** 2) + beta[i])
    return -result

def hartmann(x):
    """
        Hartmann Function — wersje 3D, 4D i 6D.

        Zakres wejściowy: x_i ∈ [0, 1]

         Minimum globalne:
        - 3D:  f(x*) ≈ -3.86278  w x* ≈ [0.114614, 0.555649, 0.852547]
        - 4D:  f(x*) ≈ -3.32237  w x* ≈ [0.4047, 0.8828, 0.8732, 0.5743]
        - 6D:  f(x*) ≈ -3.32237  w x* ≈ [0.20169, 0.150011, 0.476874, 0.275332, 0.311652, 0.6573]
        """
    x = np.array(x)
    d = len(x)

    if d == 3:
        alpha = np.array([1.0, 1.2, 3.0, 3.2])
        A = np.array([
            [3.0, 10, 30],
            [0.1, 10, 35],
            [3.0, 10, 30],
            [0.1, 10, 35]
        ])
        P = 1e-4 * np.array([
            [3689, 1170, 2673],
            [4699, 4387, 7470],
            [1091, 8732, 5547],
            [381, 5743, 8828]
        ])
    elif d == 4:
        alpha = np.array([1.0, 1.2, 3.0, 3.2])
        A = np.array([
            [10, 3, 17, 3.5],
            [0.05, 10, 17, 0.1],
            [3, 3.5, 1.7, 10],
            [17, 8, 0.05, 10]
        ])
        P = 1e-4 * np.array([
            [1312, 1696, 5569, 124],
            [2329, 4135, 8307, 3736],
            [2348, 1451, 3522, 2883],
            [4047, 8828, 8732, 5743]
        ])
    elif d == 6:
        alpha = np.array([1.0, 1.2, 3.0, 3.2])
        A = np.array([
            [10, 3, 17, 3.5, 1.7, 8],
            [0.05, 10, 17, 0.1, 8, 14],
            [3, 3.5, 1.7, 10, 17, 8],
            [17, 8, 0.05, 10, 0.1, 14]
        ])
        P = 1e-4 * np.array([
            [1312, 1696, 5569, 124, 8283, 5886],
            [2329, 4135, 8307, 3736, 1004, 9991],
            [2348, 1451, 3522, 2883, 3047, 6650],
            [4047, 8828, 8732, 5743, 1091, 381]
        ])
    else:
        raise ValueError("Hartmann function is only defined for 3, 4, or 6 dimensions.")

    outer = 0
    for i in range(4):
        inner = np.sum(A[i] * (x - P[i])**2)
        outer += alpha[i] * np.exp(-inner)
    return -outer

def perm_d_beta(x, beta=0.5):
    # Zakres: [-d, d]
    # Minimum globalne: 0 w [1, 2, ..., d]
    x = np.array(x)
    d = len(x)
    result = 0
    for j in range(1, d + 1):
        inner = np.sum((i**j + beta) * ((x / i)**j - 1) for i in range(1, d + 1))
        result += inner**2
    return result

def qing(x):
    """
    Zakres: x_i ∈ [-500, 500]
    Minimum: f(x*) = 0 at x_i = ±√i
    """
    x = np.array(x)
    i = np.arange(1, len(x) + 1)
    return np.sum((x**2 - i)**2)

def salomon(x):
    """
    Zakres: x_i ∈ [-100, 100]
    Minimum: f(x*) = 0 at x* = [0,...,0]
    """
    x = np.array(x)
    norm = np.linalg.norm(x)
    return 1 - np.cos(2 * np.pi * norm) + 0.1 * norm

def xin_she_yang_1(x):
    """
    Zakres: x_i ∈ [-5, 5]
    Minimum: f(x*) = 0 at x* = [0,...,0]
    """
    x = np.array(x)
    rand = np.random.rand(len(x))  # stała losowa wartość dla każdego wymiaru
    wynik = np.sum(rand * np.abs(x)**np.arange(1, len(x)+1))
    return wynik

def penalty_function_I(x):
    """
    Zakres: x_i ∈ [-50, 50]
    Minimum: f(x*) = 0 at x* = [1,...,1]
    """
    x = np.array(x)
    n = len(x)
    y = 1 + (x + 1) / 4

    sum1 = np.pi / n * (10 * np.sin(np.pi * y[0])**2 +
           np.sum((y[:-1] - 1)**2 * (1 + 10 * np.sin(np.pi * y[1:])**2)) +
           (y[-1] - 1)**2)

    penalty = np.sum([100 * (xi - 1)**4 if xi > 10 or xi < -10 else 0 for xi in x])
    return sum1 + penalty

def alpine_1(x):
    """
    Zakres: x_i ∈ [0, 10]
    Minimum: f(x*) = 0 at x* = [0,...,0]
    """
    x = np.array(x)
    return np.sum(np.abs(x * np.sin(x) + 0.1 * x))

def bent_cigar(x):
    """
    Zakres: x_i ∈ [-100, 100]
    Minimum: f(x*) = 0 at x* = [0,...,0]
    """
    x = np.array(x)
    return x[0]**2 + 1e6 * np.sum(x[1:]**2)

def discus(x):
    """
    Zakres: x_i ∈ [-100, 100]
    Minimum: f(x*) = 0 at x* = [0,...,0]
    """
    x = np.array(x)
    return 1e6 * x[0]**2 + np.sum(x[1:]**2)

def sharp_ridge(x):
    """
    Zakres: x_i ∈ [-100, 100]
    Minimum: f(x*) = 0 at x* = [0,...,0]
    """
    x = np.array(x)
    return x[0]**2 + 100 * np.sqrt(np.sum(x[1:]**2))

def hgbat(x):
    """
    Zakres: x_i ∈ [-100, 100]
    Minimum: f(x*) = 0 at x* = [0,...,0]
    """
    x = np.array(x)
    sum_sq = np.sum(x**2)
    sum_abs = np.sum(x)
    return np.abs(sum_sq**2 - sum_abs**2)**0.5 + (0.5 * sum_sq + sum_abs) / len(x)