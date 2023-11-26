#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def area_calculator(type_=0):
    def calculate_triangle_area(base, height):
        return 0.5 * base * height

    def calculate_rectangle_area(length, width):
        return length * width

    if type_ == 0:
        return calculate_triangle_area
    else:
        return calculate_rectangle_area


if __name__ == '__main__':
    # Вызов внешней функции с параметром type = 0 для вычисления площади треугольника
    triangle_area = area_calculator(0)
    result_triangle = triangle_area(10, 8)  # Вычисление площади треугольника с основанием 10 и высотой 8

    print('Площадь треугольника:', result_triangle)

    # Вызов внешней функции с параметром type != 0 для вычисления площади прямоугольника
    rectangle_area = area_calculator(10)
    result_rectangle = rectangle_area(10, 9)  # Вычисление площади прямоугольника с длиной 10 и шириной 9

    print('Площадь прямоугольника:', result_rectangle)
