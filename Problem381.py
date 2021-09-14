# coding: utf-8

# p を素数とする.
# (p-1)! = -1 = p-1 mod p である
# (p-2)! = (p-1)! * (p-1)^(-1)
#        = (p-1)! * (p-1)
#        = -1 * -1 = 1 mod p
# (p-3)! = (p-2)! * (p-2)^(-1) = (p-2)^(-1) mod p
# (p-4)! = (p-3)! * (p-3)^(-1) mod p
# (p-5)! = (p-4)! * (p-4)^(-1) mod p


def eratosthenes(n):
    ''' Returns  a list of primes < n '''
    primes = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            primes[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if primes[i]]


def S(p):
    def inverse(n, p):
        return pow(n, p - 2, p)

    n1 = p - 1
    n2 = 1
    n3 = inverse(p - 2, p)
    n4 = n3 * inverse(p - 3, p) % p
    n5 = n4 * inverse(p - 4, p) % p
    return (n1 + n2 + n3 + n4 + n5) % p


def main():
    max_i = 10**8

    primes = eratosthenes(max_i)
    primes.remove(2)
    primes.remove(3)

    return sum([S(i) for i in primes])


if __name__ == "__main__":
    print(main())
