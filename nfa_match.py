#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Tue Jun 18 2019 21:17:23
author : Ze Gan
'''


import graph


def activate_state(c, n, next_activated_nodes_set, visited_nodes):
    if n in visited_nodes:
        return
    visited_nodes.add(n)
    for e in n.out_edges:
        next_node = e.end_node
        # epsilon edge will not consume a char
        if e.can_jump():
            # next_activated_nodes_set.add(next_node)
            activate_state(c, next_node, next_activated_nodes_set, visited_nodes)
        # normal edge will consume a char
        elif e.can_jump(c):
            next_activated_nodes_set.add(next_node)


def match_no_backtracking(nfa, subject):
    start_node = nfa.start_node
    end_node = nfa.end_node
    current_activated_nodes_set = set()
    current_activated_nodes_set.add(start_node)
    for c in subject:
        next_activated_nodes_set = set()
        visited_nodes = set()
        for n in current_activated_nodes_set:
            activate_state(c, n, next_activated_nodes_set, visited_nodes)
        current_activated_nodes_set = next_activated_nodes_set
        if end_node in current_activated_nodes_set:
            return True
    return False
