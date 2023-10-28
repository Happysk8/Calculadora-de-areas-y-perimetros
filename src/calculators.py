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