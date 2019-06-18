#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Thu Jun 13 2019 20:6:55
author : Ze Gan
'''


import graph
import expression


class Fragment(object):
    def __init__(self):
        self.start_node = None
        self.out_edges = []


class ThompsonNfa(object):
    def __init__(self):
        self.start_node = None
        self.end_node = None

    def _build(self, pattern = [], fragments_stack = []):
        if not pattern:
            return
        for c in pattern:
            fragment = Fragment()
            if c == expression.REGEX_NOTATION.CONCATENATION:
                fragment_latter = fragments_stack.pop()
                fragment_former = fragments_stack.pop()
                for edge in fragment_former.out_edges:
                    edge.set_end(fragment_latter.start_node)
                fragment.start_node = fragment_former.start_node
                fragment.out_edges = fragment_latter.out_edges
            elif c == expression.REGEX_NOTATION.OR:
                fragment_branch_1 = fragments_stack.pop()
                fragment_branch_2 = fragments_stack.pop()
                node = graph.Node()
                graph.Edge().set_start(node).set_end(fragment_branch_1.start_node)
                graph.Edge().set_start(node).set_end(fragment_branch_2.start_node)
                fragment.start_node = node
                fragment.out_edges = fragment_branch_1.out_edges + fragment_branch_2.out_edges
            elif c == expression.REGEX_NOTATION.REPEAT_MORE_THAN_ONE:
                fragment_last = fragments_stack.pop()
                node = graph.Node()
                for edge in fragment_last.out_edges:
                    edge.set_end(node)
                graph.Edge().set_start(node).set_end(fragment_last.start_node)
                edge = graph.Edge()
                edge.set_start(node)
                fragment.start_node = fragment_last.start_node
                fragment.out_edges.append(edge)
            elif c == expression.REGEX_NOTATION.REPEAT_OR_ZERO:
                fragment_last = fragments_stack.pop()
                node = graph.Node()
                for edge in fragment_last.out_edges:
                    edge.set_end(node)
                graph.Edge().set_start(node).set_end(fragment_last.start_node)
                edge = graph.Edge()
                edge.set_start(node)
                fragment.start_node = node
                fragment.out_edges.append(edge)
            elif c == expression.REGEX_NOTATION.ZERO_OR_ONE:
                fragment_last = fragments_stack.pop()
                node = graph.Node()
                graph.Edge().set_start(node).set_end(fragment_last.start_node)
                edge = graph.Edge()
                edge.set_start(node)
                fragment.start_node = node
                fragment.out_edges = fragment_last.out_edges
                fragment.out_edges.append(edge)
            else:
                node = graph.Node()
                edge = graph.Edge(expression.MatchFunction(c))
                edge.set_start(node)
                fragment.start_node = node
                fragment.out_edges.append(edge)
            fragments_stack.append(fragment)

    def build(self, pattern):
        post_expression = expression.RegexPattern(pattern).get_postfix_expression()
        fragments_stack = []
        self._build(post_expression, fragments_stack)
        if len(fragments_stack) > 0:
            fragment = fragments_stack.pop()
            self.start_node = fragment.start_node
            self.end_node = graph.Node()
            for edge in fragment.out_edges:
                edge.set_end(self.end_node)
            # identify each node
            graph.AdjacencyTable(self.start_node)
            return self.start_node
        raise ValueError("Bad pattern")

