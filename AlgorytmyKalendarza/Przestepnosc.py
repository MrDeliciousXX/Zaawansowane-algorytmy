def AlgorytmWyznaczaniaLatPrzestepnych(rok):
    if rok % 4 == 0 and rok % 100 != 0:
        return True
    elif rok % 400 == 0:
        return True
    else:
        return False