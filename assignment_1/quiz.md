1. Hva er det dominante leddet til funksjonen f(n) = 0.5n + 40 i O-notasjon?
- [] O(2**n)
- [] O(n**n)
- [] O(n*log(n))
- [] O(log(n))
- [] O(n**2)
- [] O(1)
- [] O(n**3)
- [x] O(n)


2. Hva er det dominante leddet til funksjonen f(n) = n**2 + 10n + 40 i O-notasjon? 
- [] O(n)
- [] O(n**3)
- [] O(1)
- [] O(log(n))
- [x] O(n**2)
- [] O(n*log(n))
- [] O(n**n)
- [] O(2**n)


3.  Hva er det dominante leddet til funksjonen f(n) = 4n**3 + 10n**2 + n + 100 i O-notasjon?
- [] O(n)
- [x] O(n**3)
- [] O(2n)
- [] O(nn)
- [] O(log(n))
- [] O(n*log(n))
- [] O(1)
- [] O(n**2)


4. Hva er det dominante leddet til funksjonen f(n) = n*log(n) + 5n i O-notasjon?
- [] O(n**n)
- [x] O(n*log(n))
- [] O(log(n))
- [] O(n)
- [] O(1)
- [] O(n**3)
- [] O(n**2)
- [] O(2**n)


5. Hva er det dominante leddet til funksjonen f(n) = 15*log(n) + 5*n i O-notasjon?
- [] O(n*log(n))
- [] O(n**2)
- [] O(1)
- [x] O(n)
- [] O(2**n)
- [] O(n**n)
- [] O(n**3)
- [] O(log(n))


6. Hva er det dominante leddet til funksjonen f(n) = n**n + n100 i O-notasjon? 
- [] O(n100)
- [] O(n**2)
- [] O(1)
- [] O(log(n))
- [x] O(n**n)
- [] O(n)
- [] O(n**3)
- [] O(2**n)
- [] O(n*log(n))


7. Hva er kjøretida til til følgende Python funksjon i O-notasjon?

def sum(tall_liste):
    sum = 0
    for tall in tall_liste:
        sum += tall
    return sum

- [] O(n*log(n))
- [] O(1)
- [x] O(n)
- [] O(2n)
- [] O(n**3)
- [] O(log(n))
- [] O(n**2)
- [] O(n**n)


8. Hva er best-case kjøretid til Python funksjonen minste_tall i O-notasjon? Problemstørrelsen er størrelsen til tallet. Husk at du må finne kjøretida til funksjonen "delelig" for å finne kjøretida til funksjonen minste_faktor.

Fragment b
def minste_faktor(tall):
    for testfaktor in range(2, tall//2):
        if delelig(tall, testfaktor):
            return testfaktor
    return tall


def delelig(tall, faktor):
    if tall%faktor == 0:
        return True
    else:
        return False

- [] O(n)
- [] O(n*log(n))
- [x] O(1)
- [] O(2**n)
- [] O(log(n))
- [] O(n**n)
- [] O(n**2)
- [] O(n**3)


9. Hva er worst-case kjøretid til Python funksjonen minste_tall i O-notasjon? Problemstørrelsen er størrelsen til tallet. Husk at du må finne kjøretida til funksjonen "delelig" for å finne kjøretida til funksjonen minste_faktor.

Fragment b
def minste_faktor(tall):
    for testfaktor in range(2, tall//2):
        if delelig(tall, testfaktor):
            return testfaktor
    return tall


def delelig(tall, faktor):
    if tall%faktor == 0:
        return True
    else:
        return False

- [] O(n**n)
- [] O(log(n))
- [] O(2**n)
- [x] O(n)
- [] O(n**2)
- [] O(1)
- [] O(n*log(n))
- [] O(n**3)


10. Hva er kjøretida til følgende Python funksjon i O-notasjon?

def outlier(tall_liste):
    gjennomsnitt = 0.0
    differanse = 0.0
    maxdiff = 0.0
    outlier_value = 0
    for tall in tall_liste:
        gjennomsnitt += tall
    gjennomsnitt /= len(tall_liste)
    for tall in tall_liste:
        differanse = abs(gjennomsnitt-tall)
        if differanse > maxdiff:
            maxdiff = differanse
            outlier_value = tall
    return outlier_value

- [] O(n**3)
- [] O(n**n)
- [] O(1)
- [] O(n2)
- [] O(n*log(n))
- [] O(2**n)
- [] O(log(n))
- [x] O(n)


11. Hva er kjøretida til følgende Python funksjon i O-notasjon? Problemstørrelsen er tallverdien av "storrelse" variabelen.

Fragment d
def skriv_ut_firkant(storrelse, tegn):
    for y in range(storrelse):
        for x in range(storrelse):
            print(tegn, end="")
        print()

- [] O(n*log(n))
- [] O(n**n)
- [] O(n**3)
- [] O(2**n)
- [] O(log(n))
- [] O(n)
- [x] O(n**2)
- [] O(1)


12. Hva er kjøretida til følgende Python funksjon i O-notasjon?

def diamant(storrelse):
    for y in range(storrelse):
        for x in range(storrelse):
            if x == storrelse - y - 1:
                print("*", end="")
            else:
                print(" ", end="")
        for x in range(storrelse - 1):
            if x == y - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for y in range(1, storrelse):
        for x in range(storrelse):
            if x == y:
                print("*", end="")
            else:
                print(" ", end="")
        for x in range(storrelse):
            if x == storrelse - y - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()
- [] O(2**n)
- [] O(n**n)
- [x] O(n**2)
- [] O(log(n))
- [] O(1)
- [] O(n**3)
- [] O(n)
- [] O(n*log(n))


13. va er kjøretida til følgende Python funksjon i O-notasjon? Problemstørrelsen er størrelsen til tallet. Du kan bruke O(lengden til lista) som kjøretid for metodekallet resultat.reverse().

def binaer_form(tall):
    resultat = []
    faktor = 2
    while faktor <= tall*2:
        if tall % faktor != 0:
            resultat.append(1)
            tall -= (tall % faktor)
        else:
            resultat.append(0)
        faktor *= 2
    resultat.reverse()
    for tall in resultat:
        print(tall, end="")
    print()

- [x] O(n) <- feil
- [] O(log(n)) <- er nok korrekt
- [] O(n*log(n))
- [] O(n**2)
- [] O(2**n)
- [] O(n**3)
- [] O(n**n)
- [] O(1)
