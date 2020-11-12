"""
Project 7 - Hash Tables
CSE331 - F19
Created By: Wendy Fogland
"""


class HashNode:
    """
    DO NOT EDIT
    """

    def __init__(self, key, value, available=False):
        self.key = key
        self.value = value
        self.is_available = available

    def __repr__(self):
        return "HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashTable:
    """
    Hash Table Class
    """

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=7):
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: how much the hash table can hold
        """

        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        for prime in self.primes:
            if self.capacity <= prime:
                self.prime = prime
                break

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """

        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """

        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def _is_available(self, j):
        """
        DO NOT EDIT
        Check if the index in the table is available/empty
        :param j: index in the table
        :return: True if available or empty, false otherwise
        """
        return self.table[j] is None or self.table[j].is_available is True

    def hash_first(self, key):
        """
        DO NOT EDIT
        Converts key, a string, into a bin number for the hash table
        :param key: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if val is an empty string
        """

        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def hash_second(self, key):
        """
        Hashes key based on prime number for double hashing
        DO NOT EDIT
        :param key: key to be hashed
        :return: a hashed value
        """

        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        hashed_value = self.prime - (hashed_value % self.prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

    def double_hashing(self, key, inserting=False):
        """
        double hashing method. combine hash 1 and hash 2 to populate a hash table. figures out location of where to put key in a table
        :param key: key to find location of
        :param inserting: wheather or not we are inserting or not
        :return: returns location of key in self.table
        """
        i = 0
        count = 0
        if inserting is True:
            while True:
                loco = (self.hash_first(key) + (i * self.hash_second(key))) % self.capacity
                if self.table[loco] is None or self.table[loco].is_available is True or self.table[loco].key == key:
                    return loco
                if loco == 0:
                    count += 1
                if count > 3 and loco == 0:
                    while True:
                        loco += 1
                        if self.table[loco] is None or self.table[loco].is_available is True:
                            return loco
                        elif self.table[loco].key == key:
                            return loco
                        loco += 1
                i += 1
        else:
            while True:
                loco = (self.hash_first(key) + (i * self.hash_second(key))) % self.capacity
                if self.table[loco] is None:
                    return None
                elif self.table[loco].key == key:
                    return loco
                if loco == 0:
                    count += 1
                if count > 3 and loco == 0:
                    while True:
                        loco += 1
                        if self.table[loco] is None:
                            return None
                        elif self.table[loco].key == key:
                            return loco
                        loco += 1
                i += 1

    def insert(self, key, value):
        """
        insert key and value into hash table
        :param key: key to insert
        :param value: value associated with key
        :return: no return
        """
        loco = self.double_hashing(key, True)
        self.table[loco] = HashNode(key, value, False)
        self.size += 1
        load = self.size / self.capacity
        if load >= 0.4:
            self.grow()

    def search(self, key):
        """
        searches for key in a hash table
        :param key: key to search for
        :return: returns node of item
        """

        if self.double_hashing(key, False) is None:
            return None
        return self.table[self.double_hashing(key, False)]

    def grow(self):
        """
        grows a hash table and rehashs all the items
        :return: returns rehashed and expanded list
        """
        self.capacity = self.capacity * 2

        return self.rehash()

    def rehash(self):
        """
        rehashs a hash table when the size needs to grow
        :return: no return
        """

        rehashed = HashTable(self.capacity)
        self.prime = rehashed.prime
        for node1 in self.table:
            if node1 is not None:
                if node1.key is None and node1.value is None or node1.is_available is True:
                    pass
                else:
                    loco = rehashed.double_hashing(node1.key, True)
                    rehashed.table[loco] = HashNode(node1.key, node1.value)
        self.table = rehashed.table

    def delete(self, key):
        """
        deletes a key from a hash table
        :param key: key to delete
        :return: no return
        """

        if key is None:
            return None
        if self.search(key) is None:
            return None
        else:
            self.search(key).value = None
            self.search(key).is_available = True
            self.search(key).key = None
            self.size -= 1


def anagrams(string1, string2):
    """
    make sure all letters of a word are part of another word
    :param string1: first word to compare
    :param string2: second word to compare
    :return: if they are a true anagram return true, else return false
    """

    hash1 = HashTable()
    hash2 = HashTable()
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    string1 = string1.lower()
    string2 = string2.lower()
    for char in string1:
        searchnode = hash1.search(char)
        if searchnode is not None and searchnode.key == char:
            hash1.insert(char, searchnode.value + 1)
        else:
            hash1.insert(char, 1)

    for char2 in string2:
        searchnode2 = hash2.search(char2)
        if searchnode2 is not None:
            hash2.insert(char2, searchnode2.value + 1)
        else:
            hash2.insert(char2, 1)

    for character in string1:
        if hash2.search(character) is None:
            return False
        if hash1.search(character).value != hash2.search(character).value:
            return False
    return True


if __name__ == "__main__":
    is_anagram = anagrams("listen", "silent")
    assert is_anagram

    is_anagram = anagrams("countryroad", "dountryroad")
    print(anagrams("countryroad", "dountryroad"))
    assert not is_anagram

    is_anagram = anagrams("Jumping Jamber", "big men jump jar")
    assert is_anagram

    # Even though all letters are used, the period makes it not an anagram
    is_anagram = anagrams("kinder.", "red ink")
    assert not is_anagram
