# -*- coding: utf-8 -*-
"""Arquivo principal para execução do Conversor de Unidades."""

# Importa a classe da interface gráfica
from interface import JanelaPrincipal

# Bloco principal que será executado quando o script for rodado
if __name__ == "__main__":
    # Cria uma instância da janela principal
    app = JanelaPrincipal()
    # Inicia o loop principal do Tkinter, que mantém a janela aberta e responsiva
    app.mainloop()

