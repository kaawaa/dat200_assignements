import oving7_utdelt.student as std
import oving7_utdelt.emne as emn
import oving7_utdelt.eksamensresultat as eks


def finn_student(studentnr, studentliste):
    for student in studentliste:
        if student.studentnummer == studentnr:
            return student
    return None


def finn_emne(emnekode, emneliste):
    for emne in emneliste:
        if emne.emnekode == emnekode:
            return emne
    return None


def les_eksamensresultater(studentliste, emneliste):
    eksamensliste = []
    with open("eksamensresultater.txt") as eksamens_fil:
        for linje in eksamens_fil:
            atributter = linje.split("\t")
            studenten = finn_student(int(atributter[0].strip()), studentliste)
            emnet = finn_emne(atributter[1].strip(), emneliste)
            nytt_eksamensresultat = eks.Eksamensresultat(studenten, emnet, atributter[2].strip())
            eksamensliste.append(nytt_eksamensresultat)
    return eksamensliste


if __name__ == "__main__":
    studentliste = std.les_studentfil("studenter.txt")
    emneliste = emn.les_emner("Emner.txt")
    eksamensliste = les_eksamensresultater(studentliste, emneliste)

    for eksamensresultat in eksamensliste:
        print(eksamensresultat)
