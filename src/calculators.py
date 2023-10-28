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
