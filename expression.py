#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Thu Jun 13 2019 20:11:25
author : Ze Gan
'''


import enum


class REGEX_NOTATION(enum.Enum):
    # Defined notations in Regex
    OR = "|"
    REPEAT_OR_ZERO = "*"
    REPEAT_MORE_THAN_ONE = "+"
    PARENTHESES_BEGIN = "("
    PARENTHESES_END = ")"
    ZERO_OR_ONE = "?"
    # Customized notations just for programming
    CONCATENATION = enum.auto()

    @classmethod
    def get_item_from_value(cls, value):
        for item in cls:
            if item.value == value:
                return item
        raise KeyError(value)


INFIX_OPERATORS = (
    REGEX_NOTATION.OR,
)


POSTFIX_OPERATORS = (
    REGEX_NOTATION.REPEAT_OR_ZERO,
    REGEX_NOTATION.REPEAT_MORE_THAN_ONE, 
    REGEX_NOTATION.ZERO_OR_ONE, 
    REGEX_NOTATION.CONCATENATION,
)


class RegexPattern(object):
    def __init__(self, pattern):
        self.pattern = pattern

    def get_postfix_expression(self):
        expression = []
        operators_stack = []
        none_notation_numbers = [0]
        for c in self.pattern:
            try:
                c = REGEX_NOTATION.get_item_from_value(c)
            except KeyError:
                pass
            if c in INFIX_OPERATORS:
                while none_notation_numbers[-1] > 0 \
                    and len(operators_stack) > 0 \
                        and operators_stack[-1] not in INFIX_OPERATORS \
                            and operators_stack[-1] != REGEX_NOTATION.PARENTHESES_BEGIN:
                    expression.append(operators_stack.pop())
                    none_notation_numbers[-1] -= 1
                operators_stack.append(c)
                none_notation_numbers[-1] = 0
            elif c in POSTFIX_OPERATORS:
                expression.append(c)
                if len(operators_stack) > 0 and operators_stack[-1] == REGEX_NOTATION.CONCATENATION:
                    expression.append(operators_stack.pop())
            elif c == REGEX_NOTATION.PARENTHESES_BEGIN:
                if none_notation_numbers[-1] > 0 :
                    operators_stack.append(REGEX_NOTATION.CONCATENATION)
                operators_stack.append(c)
                none_notation_numbers.append(0)
            elif c == REGEX_NOTATION.PARENTHESES_END:
                buffer_ = []
                while len(operators_stack) > 0:
                    c = operators_stack.pop()
                    if c == REGEX_NOTATION.PARENTHESES_BEGIN:
                        break
                    expression.append(c)
                none_notation_numbers.pop()
                none_notation_numbers[-1] += 1
            else:
                if none_notation_numbers[-1] > 0:
                    operators_stack.append(REGEX_NOTATION.CONCATENATION)
                expression.append(c)
                none_notation_numbers[-1] += 1

        while len(operators_stack) > 0:
            expression.append(operators_stack.pop())
        return expression


class MatchFunction(object):
    def __init__(self, value):
        self.value = value
    
    def __call__(self, value):
        return self.value == value


