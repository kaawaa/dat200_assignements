# Kjøretid er O(n)
def recursiv_palindrom_check(word: str) -> bool:
    ## Base case
    if len(word) <= 1:
        return True
    ## Sjekk for siste og første bokstod, kaller så funksjonen rekursiv
    if word[0] == word[-1]:
        return recursiv_palindrom_check(word[1:len(word)-1])
    return False

# Kjøretid er O(n)
def iterativ_palindrom_check(word: str) -> bool:
    if len(word) <= 1:
        return True
    for letter in range(len(word)):
        if word[letter] != word[-letter-1]:
            return False
    return True
        
def main() -> None:
    print(recursiv_palindrom_check("hallo"))
    print(recursiv_palindrom_check("regninger"))
    print(iterativ_palindrom_check("hallo"))
    print(iterativ_palindrom_check("regninger"))

if __name__ == "__main__":
    main()