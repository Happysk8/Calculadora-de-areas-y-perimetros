import os
import PySimpleGUI as sg

# layouts de los inputs para cada figura
layout_cuadrado = [
    [sg.Text('Lado:')],
    [sg.InputText(key='-LADO-')],
]

layout_rectangulo = [
    [sg.Text('Lado 1:')],
    [sg.InputText(key=('-LADO1-'))],
    [sg.Text('Lado 2:')],
    [sg.InputText(key=('-LADO2-'))],
]

layout_circulo = [
    [sg.Text('Radio:')],
    [sg.InputText(key=('-RADIO-'))],
]

layout_triangulo = [
    [sg.Text('Base:')],
    [sg.InputText(key=('-BASE-'))],
    [sg.Text('Altura:')],
    [sg.InputText(key=('-ALTURA-'))],
]

# diseño de la ventana
layout = [
    [sg.Text('', size=(100, 4), justification='center',
             key='-RESULTADO-', relief='ridge')],
    [
        sg.Column([
            [sg.Button('Cuadrado', size=(10, 2))],
            [sg.Button('Rectangulo', size=(10, 2))],
            [sg.Button('Circulo', size=(10, 2))],
            [sg.Button('Triangulo', size=(10, 2))],
        ], justification='left', element_justification='left'),
        sg.Column(layout_cuadrado, key='-FIGURA-INPUTS-Cuadrado-', visible=False,
                  vertical_alignment='top'),  # Configura como invisible y vertical
        sg.Column(layout_rectangulo, key='-FIGURA-INPUTS-Rectangulo-', visible=False,
                  vertical_alignment='top'),  # Configura como invisible y vertical
        sg.Column(layout_circulo, key='-FIGURA-INPUTS-Circulo-', visible=False,
                  vertical_alignment='top'),  # Configura como invisible y vertical
        sg.Column(layout_triangulo, key='-FIGURA-INPUTS-Triangulo-',
                  visible=False, vertical_alignment='top'),


        sg.Column([[sg.Text('')],
                   [sg.Text('')],
                   [sg.Text('')],
                   [sg.Text('')],
                   [sg.Text('')],
                   [sg.Button('Calcular', size=(10, 2))]], key='-BOTON-CALCULAR-', visible=False)
    ],

    [sg.Stretch()],

]


def calcular():
    print("Hola men")


# Creacion de la ventana
window = sg.Window('Calculadora', layout, size=(600, 300))


figura_actual = None


def obtener_valores_figura(figura_actual):

    if figura_actual == 'Cuadrado':
        lado = window['-LADO-'].get()
        area = calculators.area_cuadrado(lado)
        perimetro = 0
        return f'area: {lado}\nperimetro: {perimetro}'
    elif figura_actual == 'Rectangulo':
        lado1 = window['-LADO1-'].get()
        lado2 = window['-LADO2-'].get()
        area = calculators.area_rectangulo(lado1, lado2)
        perimetro = 0
        return f'lado 1: {lado1}\n lado 2: {altura}'
    elif figura_actual == 'Circulo':
        radio = window['-RADIO-'].get()
        area = calculators.area_circulo(radio)
        perimetro = 0
        return f'Radio: {radio}'
    elif figura_actual == 'Triangulo':
        base = window['-BASE-'].get()
        altura = window['-ALTURA-'].get()
        area = calculators.area_triangulo(base, altura)
        perimetro = 0
        return f'Base: {base}\nAltura: {altura}'
    else:
        return ''


def calcular():
    resultado_text = obtener_valores_figura(figura_actual)
    window['-RESULTADO-'].update(resultado_text)


# Loop principal de la interfaz
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    # Cuando se hace clic en un botón de figura
    if event in ['Cuadrado', 'Rectangulo', 'Circulo', 'Triangulo']:

        figura_actual = event
        # Ocultar todos los layouts de entrada
        for figura in ['Cuadrado', 'Rectangulo', 'Circulo', 'Triangulo']:
            window[f'-FIGURA-INPUTS-{figura}-'].update(visible=False)
        # Muestra el layout de entrada de la figura seleccionada
        window[f'-FIGURA-INPUTS-{figura_actual}-'].update(visible=True)
        window[f'-BOTON-CALCULAR-'].update(visible=True)

    if event == 'Calcular':
        calcular()

window.close()
