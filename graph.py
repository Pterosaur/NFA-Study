#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Thu Jun 13 2019 17:58:10
author : Ze Gan
'''

import queue


class Node(object):
    def __init__(self):
        self.out_edges = []
        self.in_edges = []

    def add_out_edges(self, edge):
        self.out_edges.append(edge)

    def add_in_edges(self, edge):
        self.in_edges.append(edge)


class Edge(object):

    def __init__(self, condition = None):
        self.start_node = None
        self.end_node = None
        self.condition = condition

    def set_start(self, node):
        self.start_node = node
        self.start_node.add_out_edges(self)
        return self

    def set_end(self, node):
        self.end_node = node
        self.end_node.add_in_edges(self)
        return self

    def can_jump(self, value = None):
        if self.condition is None:
            return True
        return self.condition(value)


def breadth_first_traversal(node, node_visitor = None, edge_visitor = None):
    visit_queue = queue.Queue()
    visit_queue.put(node)
    visited = set()
    while not visit_queue.empty():
        node = visit_queue.get()
        if node in visited:
            continue
        if node_visitor:
            node_visitor(node)
        visited.add(node)
        for edge in node.out_edges:
            if edge_visitor:
                edge_visitor(edge)
            visit_queue.put(edge.start_node)
            visit_queue.put(edge.end_node)


class AdjacencyTable(object):
    def __init__(self, node = None):
        self.nodes = []
        self.edges = []
        if node:
            breadth_first_traversal(
                node, node_visitor=self.add_node, edge_visitor=self.add_edge)

    def add_node(self, node):
        node.id = len(self.nodes)
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def serialize(self):
        table = {}
        for node in self.nodes:
            table[self.nodes.index(node)] = []
        for edge in self.edges:
            table[self.nodes.index(edge.start_node)].append(
                self.nodes.index(edge.end_node))
        return table

