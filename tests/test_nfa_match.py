#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Tue Jun 18 2019 21:47:15
author : Ze Gan
'''


import nfa_match
import thompson_nfa


def test_thompson_nfa_match():
    nfa = thompson_nfa.ThompsonNfa()

    nfa.build("abc")
    assert(nfa_match.match_no_backtracking(nfa, "abc"))
    assert(not nfa_match.match_no_backtracking(nfa, "123abc"))

    nfa.build("(a|b)c")
    assert(nfa_match.match_no_backtracking(nfa, "ac"))
    assert(nfa_match.match_no_backtracking(nfa, "bc"))

    nfa.build("a+c")
    assert(nfa_match.match_no_backtracking(nfa, "aac"))

    nfa.build("a*c")
    assert(nfa_match.match_no_backtracking(nfa, "c"))

    nfa.build("a(bc+|d*e|fg)+h")
    assert(nfa_match.match_no_backtracking(nfa, "abcdedeh"))
    assert(not nfa_match.match_no_backtracking(nfa, "abcdh"))
    assert(nfa_match.match_no_backtracking(nfa, "abccch"))
    assert(nfa_match.match_no_backtracking(nfa, "aeh"))
    assert(nfa_match.match_no_backtracking(nfa, "abceeeeh"))

