#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Fri Jun 14 2019 13:34:35
author : Ze Gan
'''


import copy

import graph
import thompson_nfa


def test_thompson_nfa_build():
    nfa = thompson_nfa.ThompsonNfa()

    nfa.build(r"ab")
    table = graph.AdjacencyTable(nfa.start_node)
    table = table.serialize()
    assert(table == {0:[1], 1:[2], 2:[] })

    nfa.build(r"(ab)cd")
    table = graph.AdjacencyTable(nfa.start_node)
    table = table.serialize()
    assert(table == {0:[1], 1:[2], 2:[3], 3:[4], 4:[] })

    nfa.build(r"a|b")
    table = graph.AdjacencyTable(nfa.start_node)
    table = table.serialize()
    assert(table == {0:[1, 2], 1:[3], 2:[3], 3:[] })

    nfa.build(r"a+b")
    table = graph.AdjacencyTable(nfa.start_node)
    table = table.serialize()
    assert(table == {0:[1], 1:[0, 2], 2:[3], 3:[] })

    nfa.build(r"a*b")
    table = graph.AdjacencyTable(nfa.start_node)
    table = table.serialize()
    assert(table == {0:[1, 2], 1:[0], 2:[3], 3:[] })

    nfa.build(r"a?b")
    table = graph.AdjacencyTable(nfa.start_node)
    table = table.serialize()
    assert(table == {0:[1, 2], 1:[2], 2:[3], 3:[] })

    nfa.build(r"a(bc|de|fg)+h")
    table = graph.AdjacencyTable(nfa.start_node)
    table = table.serialize()
    assert(table == {0: [1], 1: [2, 3], 2: [4, 5], 3: [6], 4: [7], 5: [
           8], 6: [9], 7: [9], 8: [9], 9: [1, 10], 10: [11], 11: []})


