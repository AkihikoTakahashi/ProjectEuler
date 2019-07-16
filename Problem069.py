# coding: utf-8


def eratosthenes(N):

    is_prime = [False if i % 2 == 0 else True for i in range(N + 1)]
    is_prime[0], is_prime[1], is_prime[2] = False, False, True

    for i in range(3, int(N**0.5) + 1, 2):
        if is_prime[i]:
            for i in range(2 * i, N + 1, i):
                is_prime[i] = False

    return is_prime


def euler_phi(n):

    if n == 1:
        return 1

    if is_primes[n]:
        return n - 1

    else:
        i = 2
        tmp_n = n
        for i in range(2, n):
            if is_primes[i] and n % i == 0:
                e = 1
                while tmp_n % i == 0:
                    tmp_n //= i
                    e += 1
                e -= 1

                if tmp_n == 1:
                    return i**e - i**(e - 1)
                else:
                    return euler_phi(i**e) * euler_phi(n // (i**e))


max_i = 1000000
is_primes = eratosthenes(max_i)


def main():
    max_ratio = 0
    for i in range(2, max_i + 1):
        phi = euler_phi(i)
        ratio = i / phi

        if max_ratio < ratio:
            max_ratio = ratio
            max_ratio_i = i
    return max_ratio_i


if __name__ == "__main__":
    print(main())
