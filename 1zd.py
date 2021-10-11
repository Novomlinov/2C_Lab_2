#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    glasnie = set("aeiouy")

    stroka = input("Введите строку ")

    count = 0
    for letter in stroka:
        if letter in glasnie:
            count +=1

    print (f"Количество гласных букв: {count}")