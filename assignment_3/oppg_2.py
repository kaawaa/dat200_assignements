from dataclasses import dataclass, field
import time
from tokenize import String


## Dataclass for å lage og manipulere hanoi tårn, samt print ut fornuftig format
@dataclass
class Hanoi():
    discs: int = 1
    start: list = field(init=False)
    end: list = field(init=False)
    aux: list = field(init=False)

    def __post_init__(self):
        self.start = []
        self.end = []
        self.aux = []
        for i in range(self.discs, 0, -1):
            self.start.append(i)
    
    def __repr__(self):
        return f"Start:\t{self.start}\nEnd:\t{self.end}\nAux:\t{self.aux}\n"

# Rekursiv funksjon for å løse puzzle
# Kjøretiden for funksjonen er O(2**n)
def hanoi_puzzle_solver(start: list, end: list, aux: list, discs: int, h: Hanoi) -> None:
    # Base case
    if discs == 0:
        return
    hanoi_puzzle_solver(start, aux, end, discs-1, h)
    end.append(start.pop())
    print(h)
    time.sleep(1.0)
    hanoi_puzzle_solver(aux, end, start, discs-1, h)

# Start funksjon
def start_solving(h: Hanoi) -> None:
    hanoi_puzzle_solver(h.start, h.end, h.aux, h.discs, h)

def main() -> None:
    h = Hanoi(5)
    start_solving(h)

if __name__ == "__main__":
    main()