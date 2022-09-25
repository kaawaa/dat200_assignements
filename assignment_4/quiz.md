1. Gitt følgende liste: arr = [-20, -16, 8, -3, 9, 14, 1, -8, -17, 5] 

Vis hvordan lista ser ut etter at Insertation Sort har gjort etter  5 passes av sortering på den.

**(-20, -16, -3, 8, 9, 14, 1, -8, -17, 5)** <- korrekt


2. Gitt lista fra forrige oppgave. Vis hvordan lista ser ut etter at Insertion Sort har gjort etter 8 passes av sortering.

**(-20, -17, -16, -8, -3, 1, 8, 9, 14, 5)** <- korrekt


3. Oppgave går ut på å vise QuickSort algoritmen på samme liste som for oppgave 1:

[-20, 8, -3, -16, 9, 14, 1, -8, -17, 5]

Hva blir pivot element av denne lista hvis du velger siste element? 

**5**

Hva blir "pi" etter første splitting av lista?

```python
pi = partition(array, low, high)
```

Etter første splitting av lista, hvilke elementer blir med i første del som er mindre enn pivot? Oppgi elementene i samme rekkefølge som i den opprinnelige lista. Det kan hende det er for mange bokser, for alle de som er til overs, oppgi "-" (minus tegn) som svar:

**( -20, -3, -16, 1, -8, -17)** <- korrekt (mest sannsynlig)

Etter første splitting av lista, hvilke elementer blir med i siste del som er større enn pivot? Oppgi på samme vis som for første del.

**( 8, 9, 14, -, -, -)** <- korrekt (mest sannsynlig)



4. Hvilke sorteringsalgoritmer er in-place?

Gruppe av svaralternativer
- [x] Insertion Sort <- korrekt
- [x] Quick Sort <- korrekt
- [ ] Merge Sort <- korrekt
