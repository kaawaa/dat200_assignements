def binaer_form(tall):
    resultat = []
    faktor = 2
    while faktor <= tall*2:
        print("test")
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

if __name__ == "__main__":
    binaer_form(200000000)