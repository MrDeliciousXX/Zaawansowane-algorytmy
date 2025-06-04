def WyszukaniePalindromow(tekst):
    N = len(tekst)
    print(tekst)
    # szukamy palindromów
    for i in range(N-1):
        for j in range(i+2, N+1):
            i_l, i_p, t = i, j-1, True
            while i_l < i_p:
                if tekst[i_l] != tekst[i_p]:
                    t = False
                    break
                i_l += 1
                i_p -= 1
            if t:
                for k in range(i):
                    print(" ", end="")
                print(tekst[i:j])