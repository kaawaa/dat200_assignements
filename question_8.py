def minste_faktor(tall):
    for testfaktor in range(2, tall//2):
        print("javel")
        if delelig(tall, testfaktor):
            print("hello")
            return testfaktor
    return tall


def delelig(tall, faktor):
    if tall%faktor == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(minste_faktor(6))