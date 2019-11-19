"""
Author: Max Martinez
Date: October 2019

Description: Given a string s, determine which is the longest palindrome hidden in s allowing to remove any character
but not sorting s

Complexity: O(n^2)

Proof:
Complexity = # guesses * time_guess = n^2 * O(1) = O(n^2)
"""
memo = {}
def L(s):

    if s in memo:
        return memo[s]
    if len(s) == 1:
        memo[s] = s
        return s

    # If initial character i and final character j are equal, return i + L(s[1:-1]) + j
    if s[0] == s[-1]:
        sol = s[0] + L(s[1:-1]) + s[-1]
        memo[s] = sol
        return sol

    # If the characters are unequal, guess removing the first or the last character and opt for the max
    else:
        l1 = L(s[1:])
        l2 = L(s[:-1])
        if len(l1)>len(l2):
            memo[s] = l1
            return l1
        else:
            memo[s] = l2
            return l2

print(L('turboventilator'))