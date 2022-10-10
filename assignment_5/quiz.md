1. Given a hash table with 7 elements, use mod as the hash function, which starts empty. Insert the keys 100, 77, 37, 18, 35 in that order. Use linear probing to handle collisions. Show the hash table elements. Mark empty cells with a minus sign "-".

**( 77, 35, 100, 37, 18, -, -)**


2. Given a hash table with length 7 contains elements 98, 43, 2, -, 70, -, -. The hash table uses quadratic probing to handle collisions.

    1. Delete item 43 and put a mark M there.

    2. Then try to find item 70.

did you find element 70? **ja**

How many cells you have checked to find 70? **3**

3. Suppose that an open-address hash table has a capacity of 811 and it contains 81 elements. What is the table's load factor? (An appoximation is fine.)

**0.099876695**

4. What is the search complexity in direct addressing?
- [x] O(1)
- [ ] O(n)
- [ ] O(logn)

5. What is the load factor?
- [ ] Average array size
- [ ] Average key size
- [ ] Average chain length
- [x] Average hash table length

6. What is simple uniform hashing?
- [ ] Elements are hashed based on priority
- [ ] Elements has Random probability of hashing into array slots
- [ ] A weighted probabilistic method is used to hash elements into the slots
- [x] Every element has equal probability of hashing into any of the slots
