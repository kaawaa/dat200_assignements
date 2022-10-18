hashmap = [None] * 7

def hashfunc_insert(num: int, n: int):
    hash_of_num = num % n
    if hashmap[hash_of_num] == None:
        hashmap[hash_of_num] = num

def main() -> None: 
    hashfunc_insert(23, 7)
    print(hashmap)

if __name__ == "__main__":
    main()