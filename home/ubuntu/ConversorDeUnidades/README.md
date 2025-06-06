# Conversor de Unidades em Python com Tkinter

Este projeto é uma aplicação de desktop desenvolvida em Python utilizando a biblioteca Tkinter para a interface gráfica. O objetivo é fornecer um conversor de unidades simples e funcional para as categorias de Comprimento, Peso e Temperatura.

## Funcionalidades

-   Conversão entre diferentes unidades de Comprimento (Metros, Centímetros, Milímetros, Quilômetros).
-   Conversão entre diferentes unidades de Peso (Quilogramas, Gramas, Miligramas).
-   Conversão entre diferentes unidades de Temperatura (Celsius, Fahrenheit, Kelvin).
-   Interface gráfica intuitiva para seleção de categoria, unidades de origem/destino e entrada de valor.
-   Exibição clara do resultado da conversão.
-   Tratamento básico de erros para entradas inválidas (não numéricas).

## Estrutura do Projeto

O código está organizado de forma modular para facilitar a manutenção e compreensão:

-   `main.py`: Ponto de entrada da aplicação. Responsável por instanciar e executar a interface gráfica.
-   `interface.py`: Contém a classe `JanelaPrincipal` (herdando de `tk.Tk`) que define todos os elementos visuais (widgets) e a lógica de interação da interface gráfica (eventos, atualizações).
-   `funcoes.py`: Agrupa todas as funções responsáveis pela lógica de negócio, ou seja, as funções que realizam os cálculos de conversão para cada categoria e a função auxiliar para obter as unidades por categoria.

## Como Executar

1.  Certifique-se de ter o Python 3 instalado.
2.  Navegue até o diretório `ConversorDeUnidades` pelo terminal.
3.  Execute o comando: `python main.py`
4.  A janela do conversor de unidades será exibida.

## Requisitos

-   Python 3.x
-   Tkinter (geralmente já incluído na instalação padrão do Python)

## Desenvolvimento

O desenvolvimento seguiu as boas práticas de programação, incluindo:

-   **Programação Orientada a Objetos (POO):** A interface gráfica foi construída utilizando uma classe.
-   **Modularidade:** Separação clara de responsabilidades entre os arquivos (`main.py`, `interface.py`, `funcoes.py`).
-   **Clareza:** Código comentado e bem estruturado para facilitar a leitura.
-   **Tratamento de Erros:** Validações básicas para garantir que o usuário forneça entradas adequadas.

