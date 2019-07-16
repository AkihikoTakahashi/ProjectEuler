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

    is_prime = [False if i % 2 == 0 else True for i in range(n + 1)]
    is_prime[0], is_prime[1], is_prime[2] = False, False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if is_prime[i]:
            for i in range(2 * i, n + 1, i):
                is_prime[i] = False

    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes


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
