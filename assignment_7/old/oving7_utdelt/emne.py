class Emne:
    def __init__(self, emnekode, emnenavn, semester, studiepoeng):
        self.__emnekode = emnekode
        self.emnenavn = emnenavn
        self.semester = semester
        self.studiepoeng = studiepoeng

    @property
    def emnekode(self):
        return self.__emnekode

    def __str__(self):
        return f"Emne {self.emnekode} - {self.emnenavn}. Semester: {self.semester}. Antall studiepoeng: {self.studiepoeng}."


def les_emner(emne_fil):
    emner = []
    with open(emne_fil) as fila:
        for linje in fila:
            atributter = linje.split("\t")
            emner.append(Emne(atributter[0].strip(), atributter[1].strip(), atributter[2].strip(), int(atributter[3].strip())))
    return emner


if __name__ == "__main__":
    emner = les_emner("emner.txt")
    for emne in emner:
        print(emne)
