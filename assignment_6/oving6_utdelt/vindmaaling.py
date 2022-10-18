import datetime
from avl_tre import AVLTre

class Vindmaaling:
    neste_id = 1

    def __init__(self, tidspunkt, vindstyrke):
        self.__tidspunkt = tidspunkt
        self.__vindstyrke = vindstyrke
        self.__id = Vindmaaling.neste_id
        Vindmaaling.neste_id += 1

    def get_tidspunkt(self):
        return self.__tidspunkt

    def get_vindstyrke(self):
        return self.__vindstyrke

    def get_id(self):
        return self.__id

    def __str__(self):
        return f"Vindmåling {self.__id}. Tidspunkt: {self.__tidspunkt}. Vindstyrke: {self.__vindstyrke}"

    def __lt__(self, other):
        return self.__tidspunkt < other.get_tidspunkt()


def les_vindmaalinger(filnavn):
    vindmaalinger = []
    with open(filnavn, "r") as fila:
        for linje in fila:
            linje.strip()
            komponenter = linje.split("\t")
            tidspunkt = datetime.datetime.fromisoformat(komponenter[1])
            vindstyrke = float(komponenter[3])
            ny_maaling = Vindmaaling(tidspunkt, vindstyrke)
            vindmaalinger.append(ny_maaling)
    return vindmaalinger

# Hjelpe funksjon for å gjøre om til datetime format
def gjor_om_til_datetime(tidspunkt: str) -> datetime:
    return datetime.datetime.fromisoformat(tidspunkt)

# Lager en avl bst fra vindmålinger
def lag_AVLtre(vindmaalinger: Vindmaaling) -> AVLTre:
    treet = AVLTre()
    for vindmaaling in vindmaalinger:
        treet.put(vindmaaling.get_tidspunkt(), vindmaaling.get_vindstyrke())
    return treet

# finn den vinden for den neste tidspunktet i treet
def finn_vindstyrke(tidspunkt: str, avltreet: AVLTre) -> float:
    tidspunkt = avltreet.next(gjor_om_til_datetime(tidspunkt))
    return avltreet.get(tidspunkt)

# finn den maksimale vindstyrken 
def finn_maks_vindstyrke(start_tidspunkt: str, avltreet: AVLTre) -> float:
    start_tidspunkt = gjor_om_til_datetime(start_tidspunkt)
    slutt_tidspunkt = start_tidspunkt + datetime.timedelta(days=1)
    alle_vindmaalinger = avltreet.between(start_tidspunkt, slutt_tidspunkt)
    max_vindmaaling = 0.0

    for vindmaaling in alle_vindmaalinger:
        if avltreet.get(vindmaaling) > max_vindmaaling:
            max_vindmaaling = avltreet.get(vindmaaling)
    return max_vindmaaling



if __name__ == "__main__":
    vindmaalinger = les_vindmaalinger("assignment_6/oving6_utdelt/vindmaalinger_redusert_mer.txt")
    print(len(vindmaalinger))
    print(vindmaalinger[0])
    print(vindmaalinger[1000])
    print(vindmaalinger[-1])

    avltreet = lag_AVLtre(vindmaalinger)
    print(finn_vindstyrke("2010-09-04 12:00", avltreet))
    print(finn_maks_vindstyrke("2011-12-07 00:00", avltreet))



