#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    for a in range(len(A) - 1):
        if A[a] == A[a + 1]:
            print(a, a + 1)
            break