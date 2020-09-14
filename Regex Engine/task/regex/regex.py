# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:45:05 2020

@author: ptolemy
"""

# write your code here
"""
JetBrains Python Regex

An empty regex should always return True.
An empty input should always return False.
An empty regex against an empty input always returns True.
"""


def char_match(expr, char):
    return expr == '' or char == expr or (expr == '.' and char != '')


def length_match(expr, text):
    if expr == '' or (expr == '$' and text == ''):
        return True
    if text == '':
        return False
    if len(expr) > 1 and expr[1] in '*?+':
        if expr[1] in '?*' and length_match(expr[2:], text):
            return True
        if char_match(expr[0], text[0]) and (
                (expr[1] in '?+' and length_match(expr[2:], text[1:])) or
                (expr[1] in '*+' and length_match(expr, text[1:]))):
            return True
    if not char_match(expr[0], text[0]):
        return False
    return length_match(expr[1:], text[1:])


def reg_exp(expr, string):
    if expr == '':
        return True
    if expr[0] == '^':
        return length_match(expr[1:], string)
    for i in range(len(string)):
        if length_match(expr, string[i:]):
            return True
    return False


print(reg_exp(*input().split('|')))
