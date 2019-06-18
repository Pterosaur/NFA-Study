#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Thu Jun 13 2019 17:59:34
author : Ze Gan
'''


import copy

import graph


def test_graph_build():
    n1 = graph.Node()
    n2 = graph.Node()
    e = graph.Edge()
    e.set_start(n1)
    e.set_end(n2)
    assert(e.start_node == n1)
    assert(e.end_node == n2)
    assert(e in n1.out_edges)
    assert(e not in n1.in_edges)
    assert(e in n2.in_edges)
    assert(e not in n2.out_edges)


def test_graph_condition_jump():
    no_condition = graph.Edge()
    assert(no_condition.can_jump())
    assert(no_condition.can_jump('a'))
    match_a = graph.Edge(lambda x: x == 'a')
    assert(match_a.can_jump('a'))
    assert( not match_a.can_jump('b'))


diamond_graph = [
    graph.Node(),
    graph.Node(),
    graph.Node(),
    graph.Node()
]
graph.Edge().set_start(diamond_graph[0]).set_end(diamond_graph[1])
graph.Edge().set_start(diamond_graph[0]).set_end(diamond_graph[2])
graph.Edge().set_start(diamond_graph[1]).set_end(diamond_graph[3])
graph.Edge().set_start(diamond_graph[2]).set_end(diamond_graph[3])


def test_breadth_first_traversal():
    expect_visit_queue = [
        diamond_graph[0],
        diamond_graph[1],
        diamond_graph[2],
        diamond_graph[3],
    ]
    visit_queue = []
    graph.breadth_first_traversal(
        diamond_graph[0],
        lambda n: visit_queue.append(n))
    assert(visit_queue == expect_visit_queue)


def test_adjacency_table():
    tbl = graph.AdjacencyTable(diamond_graph[0])
    assert(tbl.serialize() == {0:[1,2,], 1:[3], 2:[3], 3:[]})

