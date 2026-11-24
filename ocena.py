def ocena(gracz: str, komputer: str):

    ZIELONY = '\033[92m'
    ZOLTY = '\033[93m'
    RESET = '\033[0m'

    for i in range(len(gracz)):
        czyJest = False
        czyTraf= False
        for j in range(len(komputer)):
            if gracz[i]==komputer[j]:
                if i == j:
                    czyTraf=True
                    czyJest=True
                else:
                    czyJest=True

        if czyJest and czyTraf:
            print(f"{ZIELONY}{gracz[i]}{RESET}", end="")
        elif czyJest:
            print(f"{ZOLTY}{gracz[i]}{RESET}", end="")
        else:
            print(gracz[i], end="")

    print(" ")
