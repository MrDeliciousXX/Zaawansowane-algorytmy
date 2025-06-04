def AlgorytmGaussaWyznaczaniaDatyWielkanocy(rok):
    t = [
        [-10000,1582,15,6],
        [1583,1699,22,2],
        [1700,1799,23,3],
        [1800,1899,23,4],
        [1900,2099,24,5],
        [2100,2199,24,6],
        [2200,2299,25,0],
        [2300,2399,26,1],
        [2400,2499,25,1]
    ]
    a = rok % 19
    b = rok % 4
    c = rok % 7

    for wiersz in t:
        if wiersz[0] <= rok <= wiersz[1]:
            A = wiersz[2]
            B = wiersz[3]
            break
    d = (a * 19 + A) % 30
    e = (2 * b + 4 * c + 6 * d + B) % 7
    wielkanoc = 22 + d + e
    miesiac = "marca"
    if wielkanoc > 31:
        miesiac = "kwietnia"
        wielkanoc = wielkanoc - 31

    if d == 29 and e == 6:
        return "19 kwietnia"
    elif d == 28 and e == 6:
        return "18 kwietnia"
    else:
        return f"{wielkanoc} {miesiac}"