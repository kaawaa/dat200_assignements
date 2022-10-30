class Student:
    def __init__(self, studentnummer, etternavn, fornavn, fodselsaar, studieretning, aarskurs):
        self.__studentnummer = studentnummer
        self.etternavn = etternavn
        self.fornavn = fornavn
        self.fodselsaar = fodselsaar
        self.studieretning = studieretning
        self.aarskurs = aarskurs

    @property
    def studentnummer(self):
        return self.__studentnummer

    def __str__(self):
        return f"Student {self.studentnummer}: {self.etternavn}, {self.fornavn}, går i {self.aarskurs}. årskurs {self.studieretning}"


def les_studentfil(fil_med_studenter):
    with open(fil_med_studenter) as fila:
        studentliste = []
        for linje in fila:
            attributter = linje.split("\t")
            studentliste.append(Student(int(attributter[0].strip()), attributter[1], attributter[2], int(attributter[3].strip()),
                                        attributter[4], int(attributter[5].strip())))
    return studentliste


if __name__ == "__main__":
    studentliste = les_studentfil("studenter.txt")
    for student in studentliste:
        print(student)

