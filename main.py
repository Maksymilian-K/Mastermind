from ocena import ocena

print("\n=============Mastermind==============\n")
komputer = "1234"
max_prob = 12
proba = 0

while proba < max_prob:
    gracz = input(f"Próba {proba + 1}/{max_prob} — Zgadnij liczbę (4 cyfry): ").strip()

    if not gracz.isdigit():
        print("To nie wordle bialasie")
        continue

    if len(gracz) != 4:
        print("Za duza liczba")
        continue

    if gracz == komputer:
        print(f"Zgadłeś liczbę {komputer}!!")
        break

    wynik = ocena(gracz, komputer)
    if wynik is not None:
        print(wynik)

    proba += 1
else:
    print(f"Przegrales. Szukana liczba to {komputer}.")
