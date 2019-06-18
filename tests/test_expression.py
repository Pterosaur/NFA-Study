#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Mon Jun 17 2019 16:46:4
author : Ze Gan
'''

import expression


def check_expression(infix_expression, post_expression):
    buffer_ = ""
    for c in expression.RegexPattern(infix_expression).get_postfix_expression():
        if c == expression.REGEX_NOTATION.CONCATENATION:
            c = "."
        try:
            c = c.value
        except AttributeError:
            pass
        buffer_ += c
    assert(buffer_ == post_expression)


def test_to_postfix_expression():
    check_expression(r"ab", "ab.")
    check_expression(r"a(b)", "ab.")
    check_expression(r"a(b+)", "ab+.")
    check_expression(r"a(b)+", "ab+.")
    check_expression(r"a(b+)+", "ab++.")
    check_expression(r"a(bb)+a", "abb.+.a.")
    check_expression(r"a(b|c)d", "abc|d..")
    check_expression(r"a(bc|d)+e", "abc.d|+.e.")
    check_expression(r"a(bc|de)+f", "abc.de.|+.f.")
    check_expression(r"a(bc|de|fg)+h", "abc.de.fg.||+.h.")
    check_expression(r"a*b", "a*b.")
    check_expression(r"a?b", "a?b.")
    check_expression(r"(ab)cd", "ab.cd..")
    check_expression(r"a(bc+|d*e|fg)+h", "abc+.d*e.fg.||+.h.")

