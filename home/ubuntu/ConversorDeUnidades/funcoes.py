# -*- coding: utf-8 -*-
"""Módulo contendo as funções de lógica e conversão de unidades."""

def converter_comprimento(valor, unidade_origem, unidade_destino):
    """Realiza a conversão entre unidades de comprimento."""
    # Fator de conversão para metros (unidade base)
    fatores = {
        'Metros (m)': 1,
        'Centímetros (cm)': 0.01,
        'Milímetros (mm)': 0.001,
        'Quilômetros (km)': 1000
    }

    if unidade_origem not in fatores or unidade_destino not in fatores:
        return "Unidade inválida"

    try:
        valor_float = float(valor)
    except ValueError:
        return "Erro: Valor inválido (não numérico)"

    # Converte valor de origem para metros
    valor_em_metros = valor_float * fatores[unidade_origem]

    # Converte de metros para a unidade de destino
    valor_convertido = valor_em_metros / fatores[unidade_destino]

    return f"{valor_convertido:.4f}"

def converter_peso(valor, unidade_origem, unidade_destino):
    """Realiza a conversão entre unidades de peso."""
    # Fator de conversão para quilogramas (unidade base)
    fatores = {
        'Quilogramas (kg)': 1,
        'Gramas (g)': 0.001,
        'Miligramas (mg)': 0.000001
    }

    if unidade_origem not in fatores or unidade_destino not in fatores:
        return "Unidade inválida"

    try:
        valor_float = float(valor)
    except ValueError:
        return "Erro: Valor inválido (não numérico)"

    # Converte valor de origem para quilogramas
    valor_em_kg = valor_float * fatores[unidade_origem]

    # Converte de quilogramas para a unidade de destino
    valor_convertido = valor_em_kg / fatores[unidade_destino]

    return f"{valor_convertido:.4f}"

def converter_temperatura(valor, unidade_origem, unidade_destino):
    """Realiza a conversão entre unidades de temperatura."""
    unidades_validas = ['Celsius (°C)', 'Fahrenheit (°F)', 'Kelvin (K)']

    if unidade_origem not in unidades_validas or unidade_destino not in unidades_validas:
        return "Unidade inválida"

    try:
        valor_float = float(valor)
    except ValueError:
        return "Erro: Valor inválido (não numérico)"

    # Lógica de conversão
    if unidade_origem == unidade_destino:
        return f"{valor_float:.2f}"

    # Celsius para...
    if unidade_origem == 'Celsius (°C)':
        if unidade_destino == 'Fahrenheit (°F)':
            resultado = (valor_float * 9/5) + 32
        elif unidade_destino == 'Kelvin (K)':
            resultado = valor_float + 273.15
    # Fahrenheit para...
    elif unidade_origem == 'Fahrenheit (°F)':
        if unidade_destino == 'Celsius (°C)':
            resultado = (valor_float - 32) * 5/9
        elif unidade_destino == 'Kelvin (K)':
            resultado = (valor_float - 32) * 5/9 + 273.15
    # Kelvin para...
    elif unidade_origem == 'Kelvin (K)':
        if unidade_destino == 'Celsius (°C)':
            resultado = valor_float - 273.15
        elif unidade_destino == 'Fahrenheit (°F)':
            resultado = (valor_float - 273.15) * 9/5 + 32

    return f"{resultado:.2f}"

def obter_unidades_por_categoria(categoria):
    """Retorna a lista de unidades para uma dada categoria."""
    unidades = {
        'Comprimento': ['Metros (m)', 'Centímetros (cm)', 'Milímetros (mm)', 'Quilômetros (km)'],
        'Peso': ['Quilogramas (kg)', 'Gramas (g)', 'Miligramas (mg)'],
        'Temperatura': ['Celsius (°C)', 'Fahrenheit (°F)', 'Kelvin (K)']
    }
    return unidades.get(categoria, [])

