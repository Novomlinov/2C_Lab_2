#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Вариант 12
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "k", "n", "o", "q"}
    b = {"a", "b", "k", "u"}
    c = {"o", "p"}
    d = {"a", "m", "n", "y", "z"}

    x = (a.union(b)).intersection(c)
    print(f"x = {x}")

    # Найдем дополнение множества A
    an = u.difference(a)

    y = (an.intersection(d)).union(c.difference(b))
    print(f"y = {y}")