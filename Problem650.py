# coding: utf-8

# B(n) = nC0 * nC1 * nC2 * ... * nCn
#      = n! / 0!(n-0)! * n! / 1!(n-1)! * n! / 2!(n-2)! * ... * n! / n!(n-n)!
#      = n!^(n+1) / (0!*1!*2!* ... * n!)^2
#      = {(n-1)!^n / (0!*1!*2!* ... * (n-1)!)^2} * (n-1)! * n^(n+1) / n!^2
#      = B(n-1) * n^n / n!

from functools import lru_cache, reduce


@lru_cache(maxsize=4096)
def B(n):
    if n == 1:
        return 1
    else:
        return B(n - 1) * n**n // reduce(lambda x, y: x * y, range(1, n + 1))
