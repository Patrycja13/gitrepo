#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def fib_iter(n):
    """f(0) = 0
    f(1) =1
    f(n) = F(n-2)+F(n-1)
    """
    a, b = (0, 1)
    for i in range(1, n - 1):
        a = b
        b = a + b
    if n < 2:
        return b
    else:
        return a


def main(args):
    n = int(input('podaj wyraz ciągu: '))
    assert fib_iter(0) == 0
    assert fib_iter(1) == 1
    assert fib_iter(2) == 1
    assert fib_iter(3) == 2
    assert fib_iter(4) == 3
    assert fib_iter(5) == 5
    assert fib_iter(6) == 8
    assert fib_iter(10) == 55
    print("wyraz {:d} = {:d}".format(n, fib_iter(n)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
