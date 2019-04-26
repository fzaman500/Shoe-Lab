import numpy as np
import matplotlib.pyplot as plt


def cor_shoes(n):
    perm = np.random.permutation(n)
    return count_matches(perm)


def exp_value(n, t):
    return np.mean([cor_shoes(n) for _ in range(t)])

# t = trials

def count_matches(perm):
    count = 0
    for i in range(len(perm)):
        if perm[i] == i:
            count += 1
    return count


def match_perm(n):
    perm = np.random.permutation(n)
    while not has_match(perm):
        perm = np.random.permutation(n)
    return perm


def has_match(perm):
    for i in range(len(perm)):
        if perm[i] == i:
            return True

    return False


def prob_match(n, t):
    return np.mean([has_match(np.random.permutation(n)) for _ in range(t)])

def exactly_one_match(n):
    perm = match_perm(n)
    return count_matches(perm) == 1

def prob_exactly_one_match(n, t):
    return np.mean([exactly_one_match(n) for _ in range(t)])

def cor_shoes_match(n):
    perm = match_perm(n)
    return count_matches(perm)

def exp_one_match(n, t):
    return np.mean([cor_shoes_match(n) for _ in range(t)])


