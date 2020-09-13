# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:45:05 2020

@author: ptole
"""

# write your code here
"""
JetBrains Python Regex

An empty regex should always return True.
An empty input should always return False.
An empty regex against an empty input always returns True.
"""
[regular_expression, input_text] = input().split('|')
regular_expression = regular_expression.strip()
input_text = input_text.strip()


def check_char(reg_char, char):
    if not reg_char and not char:
        return True
    elif not char:
        return False
    elif reg_char == '.':
        return True
    elif reg_char == char:
        return True
    elif not reg_char:
        return True
    else:
        return False


def check_equal_word(regex, cmp_word):
    result = False
    if not regex:
        return True
    if not cmp_word:
        return False
    if len(regex) > len(cmp_word):
        return False
    c = 0
    if check_char(regex[0], cmp_word[0]):
        result = True
        for _ in cmp_word[1:]:
            c += 1
            letter_check = check_char(regex[c], cmp_word[c])
            if not letter_check:
                result = letter_check
                break
    return result


def check_dot_text(expr, text):
    result = False
    len_expr = len(expr)
    len_text = len(text)

    if len_expr > len_text:
        return result

    if not expr:
        return not result

    if not text:
        return result

    if len(expr) == len(text) and not is_start_wild(expr) and not is_end_wild(expr):
        return check_equal_word(expr, text)

    depth = (len_text - len_expr + 1)
    for offset in range(0, len_text - len_expr + 1):
        partial_text = text[offset:offset + len_expr]
        if len(partial_text) == len_expr:
            result = (result or check_equal_word(expr, partial_text))
            if result:
                break
        else:
            break
    return result


def is_start_wild(expr):
    return expr[0] == '^' if len(expr) > 0 else False


def is_end_wild(expr):
    return expr[- 1] == '$' if len(expr) > 0 else False


def are_sides_wild(expr):
    return is_start_wild(expr) and is_end_wild(expr)


def is_start_match(expr, text):
    if len(expr) == 0:
        return True
    if is_start_wild(expr):
        expr = expr[1:]
    if is_end_wild(expr):
        expr = expr[:-1]
    if len(expr) == 0:
        return True
    exp_length = len(expr)
    text_length = len(text)
    if text_length >= exp_length:
        return check_dot_text(expr, text[0:exp_length + 1])
    else:
        return False


def is_end_match(expr, text):
    if len(expr) == 0:
        return True
    if is_end_wild(expr):
        expr = expr[:-1]
    if is_start_wild(expr):
        expr = expr[1:]
    if len(expr) == 0:
        return True
    exp_length = len(expr)
    text_length = len(text)
    if text_length >= exp_length:
        return check_dot_text(expr, text[- exp_length:])
    else:
        return False


def are_sides_match(expr, text):
    if are_sides_wild(expr):
        expr = expr[1:-1]
        return len(expr) == len(text) and check_dot_text(expr, text)
    else:
        return False


def sides_dots_match(expr, text):
    if are_sides_wild(expr):
        return are_sides_match(expr, text)
    elif is_start_wild(expr) or is_end_wild(expr):
        if is_start_wild(expr):  # start_match or end_match:
            return is_start_match(expr, text)
        elif is_end_wild(expr):
            return is_end_match(expr, text)
    else:
        return check_dot_text(expr, text)


print(sides_dots_match(regular_expression, input_text))
