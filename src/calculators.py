import math


def perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro


def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3


def perimetro_cuadrado(lado):
    return 4 * lado


def perimetro_rectangulo(lado1, lado2):
    return 2 * (lado1 + lado2)

import numpy as np

def area_cuadrado(lado):
    area = lado ** 2
    return area

def area_rectangulo(lado_a, lado_b):
    area = lado_a * lado_b
    return area

def area_circulo(radio):
    area = np.pi * radio ** 2
    return area

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area