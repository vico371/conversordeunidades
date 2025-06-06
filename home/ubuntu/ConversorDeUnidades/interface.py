# -*- coding: utf-8 -*-
"""Módulo responsável pela interface gráfica do Conversor de Unidades."""

import tkinter as tk
from tkinter import ttk, messagebox
from funcoes import (converter_comprimento, converter_peso,
                     converter_temperatura, obter_unidades_por_categoria)

class JanelaPrincipal(tk.Tk):
    """Classe que representa a janela principal da aplicação."""
    def __init__(self):
        """Inicializa a janela principal e seus componentes."""
        super().__init__()
        self.title("Conversor de Unidades")
        # self.geometry("450x300") # Define um tamanho inicial (opcional)
        self.resizable(False, False) # Impede redimensionamento

        # Variáveis de controle
        self.categoria_var = tk.StringVar()
        self.unidade_origem_var = tk.StringVar()
        self.unidade_destino_var = tk.StringVar()
        self.valor_entrada_var = tk.StringVar()
        self.resultado_var = tk.StringVar(value="Resultado...")

        # Lista de categorias
        self.categorias = ["Comprimento", "Peso", "Temperatura"]

        # Cria os frames para organizar os widgets
        self.frame_principal = ttk.Frame(self, padding="10")
        self.frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.frame_selecao = ttk.LabelFrame(self.frame_principal, text="Seleção de Unidades", padding="10")
        self.frame_selecao.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)

        self.frame_conversao = ttk.LabelFrame(self.frame_principal, text="Conversão", padding="10")
        self.frame_conversao.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)

        self.frame_resultado = ttk.LabelFrame(self.frame_principal, text="Resultado", padding="10")
        self.frame_resultado.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)

        # --- Widgets do Frame de Seleção ---
        ttk.Label(self.frame_selecao, text="Categoria:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_categoria = ttk.Combobox(self.frame_selecao, textvariable=self.categoria_var,
                                            values=self.categorias, state="readonly", width=15)
        self.combo_categoria.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.combo_categoria.bind("<<ComboboxSelected>>", self.atualizar_unidades)

        ttk.Label(self.frame_selecao, text="De:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_origem = ttk.Combobox(self.frame_selecao, textvariable=self.unidade_origem_var,
                                         state="disabled", width=15)
        self.combo_origem.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.frame_selecao, text="Para:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_destino = ttk.Combobox(self.frame_selecao, textvariable=self.unidade_destino_var,
                                          state="disabled", width=15)
        self.combo_destino.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # --- Widgets do Frame de Conversão ---
        ttk.Label(self.frame_conversao, text="Valor:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_valor = ttk.Entry(self.frame_conversao, textvariable=self.valor_entrada_var, width=18)
        self.entry_valor.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.botao_converter = ttk.Button(self.frame_conversao, text="Converter", command=self.realizar_conversao)
        self.botao_converter.grid(row=0, column=2, padx=15, pady=5, sticky=tk.E)

        # --- Widgets do Frame de Resultado ---
        self.label_resultado = ttk.Label(self.frame_resultado, textvariable=self.resultado_var, font=("Arial", 12, "bold"))
        self.label_resultado.grid(row=0, column=0, padx=5, pady=10, sticky=tk.W)

        # Configura o comportamento de redimensionamento das colunas/linhas se necessário
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frame_principal.columnconfigure(1, weight=1)

        # Define a categoria inicial (opcional)
        # self.categoria_var.set(self.categorias[0])
        # self.atualizar_unidades() # Chama para popular as unidades iniciais

    def atualizar_unidades(self, event=None):
        """Atualiza as opções dos comboboxes de unidades com base na categoria selecionada."""
        categoria_selecionada = self.categoria_var.get()
        unidades = obter_unidades_por_categoria(categoria_selecionada)

        if unidades:
            self.combo_origem["values"] = unidades
            self.combo_destino["values"] = unidades
            self.combo_origem.config(state="readonly")
            self.combo_destino.config(state="readonly")
            self.unidade_origem_var.set(unidades[0]) # Define a primeira unidade como padrão
            self.unidade_destino_var.set(unidades[1] if len(unidades) > 1 else unidades[0]) # Define a segunda ou primeira
        else:
            self.combo_origem.config(state="disabled")
            self.combo_destino.config(state="disabled")
            self.unidade_origem_var.set("")
            self.unidade_destino_var.set("")
        self.resultado_var.set("Resultado...") # Limpa o resultado ao mudar categoria

    def realizar_conversao(self):
        """Obtém os valores da interface, chama a função de conversão apropriada e exibe o resultado."""
        categoria = self.categoria_var.get()
        origem = self.unidade_origem_var.get()
        destino = self.unidade_destino_var.get()
        valor_str = self.valor_entrada_var.get()

        # Validações básicas
        if not categoria or not origem or not destino:
            messagebox.showerror("Erro", "Por favor, selecione a categoria e as unidades.")
            return
        if not valor_str:
            messagebox.showerror("Erro", "Por favor, insira um valor para converter.")
            return

        # Tenta realizar a conversão
        try:
            # Chama a função de conversão correta baseada na categoria
            if categoria == "Comprimento":
                resultado = converter_comprimento(valor_str, origem, destino)
            elif categoria == "Peso":
                resultado = converter_peso(valor_str, origem, destino)
            elif categoria == "Temperatura":
                resultado = converter_temperatura(valor_str, origem, destino)
            else:
                resultado = "Erro: Categoria inválida"

            # Verifica se a função de conversão retornou um erro
            if isinstance(resultado, str) and resultado.startswith("Erro:"):
                 messagebox.showerror("Erro de Conversão", resultado)
                 self.resultado_var.set("Resultado...")
            else:
                # Formata a exibição do resultado
                resultado_formatado = f"{valor_str} {origem.split('(')[0].strip()} = {resultado} {destino.split('(')[0].strip()}"
                self.resultado_var.set(resultado_formatado)

        except Exception as e:
            messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")
            self.resultado_var.set("Resultado...")

# Este bloco é apenas para teste local do módulo interface.py
# O arquivo principal será o main.py
if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()

