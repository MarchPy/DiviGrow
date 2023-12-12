import os
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import LabelFrame, Label, Entry, Button

class DividendCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculadora de Dividendos')
        self.resizable(width=False, height=False)
        self._create_widgets()
        self._init_result_labels()

    def _create_widgets(self):
        self.label_frame_input = LabelFrame(self, text='Defina os parâmetros corretamente')
        self.label_qtd_investimento = Label(self.label_frame_input, text='Valor de investimento mensal:')
        self.entry_qtd_investimento = Entry(self.label_frame_input, width=10)
        self.label_preco_cota = Label(self.label_frame_input, text='Preço da cota:')
        self.entry_preco_cota = Entry(self.label_frame_input, width=10)
        self.label_ult_divid = Label(self.label_frame_input, text='Média de dividendos da cota:')
        self.entry_ult_divid = Entry(self.label_frame_input, width=10)
        self.label_tempo_invest = Label(self.label_frame_input, text='Tempo de investimento (Em anos):')
        self.entry_tempo_invest = Entry(self.label_frame_input, width=10)

        self.label_frame_input.grid(row=0, column=0, padx=10, pady=10)
        self.label_qtd_investimento.grid(row=0, column=0, sticky='W')
        self.entry_qtd_investimento.grid(row=0, column=1, padx=5)
        self.label_preco_cota.grid(row=1, column=0, sticky='W')
        self.entry_preco_cota.grid(row=1, column=1, padx=5)
        self.label_ult_divid.grid(row=2, column=0, sticky='W')
        self.entry_ult_divid.grid(row=2, column=1, padx=5)
        self.label_tempo_invest.grid(row=3, column=0, sticky='W')
        self.entry_tempo_invest.grid(row=3, column=1, padx=5)

        self.button_calculate = Button(self.label_frame_input, text='Calcular', command=self._calculate_dividends)
        self.button_calculate.grid(row=4, columnspan=2, pady=5)

        self.label_frame_result = LabelFrame(self, text='Resultado')
        self.label_frame_result.grid(row=0, column=1, padx=10, pady=10, sticky='W')

    def _init_result_labels(self):
        self.label_result_montante_final = Label(self.label_frame_result, text='Montante Final:')
        self.label_result_montante_final.grid(row=0, column=0, sticky='W')

    def _calculate_dividends(self):
        try:
            valor_investimento_mensal = float(self.entry_qtd_investimento.get())
            preco_cota = float(self.entry_preco_cota.get())
            media_dividendos = float(self.entry_ult_divid.get())
            tempo_investimento = int(self.entry_tempo_invest.get())

            # Calcula o montante final usando a fórmula de juros compostos
            montante_final = valor_investimento_mensal * ((1 + media_dividendos / preco_cota) ** (tempo_investimento * 12))

            # Atualiza o texto do rótulo do resultado com o montante final calculado
            self.label_result_montante_final.config(text='Montante Final: R${:.2f}'.format(montante_final))

        except ValueError:
            # Mostra uma mensagem de erro se os valores não forem válidos
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

if __name__ == '__main__':
    app = DividendCalculatorApp()
    app.mainloop()
