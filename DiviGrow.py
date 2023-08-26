import os
import tkinter as tk
import pandas as pd
from tkinter import messagebox
from tkinter.ttk import LabelFrame, Label, Entry, Button
from datetime import datetime


class DividendCalculator:
    @staticmethod
    def calculate(qtd_cotas, preco_cota, media_dividendos, tempo_investimento, qtd_compra):
        df = pd.DataFrame()
        
        ano_atual = int(datetime.now().strftime("%Y"))
        for ano in range(ano_atual, ano_atual + tempo_investimento + 1):
            for mes in range(1, 13):
                retorno_dividendos = qtd_cotas * media_dividendos
                qtd_cotas += int(retorno_dividendos / preco_cota) + qtd_compra
                line = {
                    'Ano': [ano],
                    'Mês': [mes],
                    'Quantidade de Cotas': [qtd_cotas],
                    'Valor Total Investido': [round(qtd_cotas * preco_cota, 2)],
                    'Retorno de dividendos': [round(retorno_dividendos, 2)],
                }
                df_tmp = pd.DataFrame(line)
                df = pd.concat([df, df_tmp])
        
        df.to_excel("Resultado dos juros compostos.xlsx", index=True)
          
        data = {
            'Ano Final': ano,
            'Quantidade de Cotas': qtd_cotas,
            'Valor Total Investido': round(qtd_cotas * preco_cota, 2),
            'Recebimento de dividendos (último mês)': round(retorno_dividendos, 2),
        }
        return data

class DividendCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculadora de Dividendos')
        self.resizable(width=False, height=False)
        self.iconbitmap(os.path.join(os.getcwd(), 'image/dividends-icon.ico')) 
        self._create_widgets()
        self._init_result_labels()

    def _create_widgets(self):
        self.label_frame_input = LabelFrame(self, text='Defina os parâmetros corretamente')
        self.label_qtd_cotas = Label(self.label_frame_input, text='Quantidade de cotas:')
        self.entry_qtd_cotas = Entry(self.label_frame_input, width=10)
        self.label_preco_cota = Label(self.label_frame_input, text='Preço da cota:')
        self.entry_preco_cota = Entry(self.label_frame_input, width=10)
        self.label_ult_divid = Label(self.label_frame_input, text='Média de dividendos da cota:')
        self.entry_ult_divid = Entry(self.label_frame_input, width=10)
        self.entry_resultado_div = Entry(self.label_frame_input, width=10)
        self.label_tempo_invest = Label(self.label_frame_input, text='Tempo de investimento (Em anos):')
        self.entry_tempo_invest = Entry(self.label_frame_input, width=10)
        self.label_qtd_compra = Label(self.label_frame_input, text='Quantidade de cotas por mês:')
        self.entry_qtd_compra = Entry(self.label_frame_input, width=10)

        self.label_frame_input.grid(row=0, column=0, padx=10, pady=10)
        self.label_qtd_cotas.grid(row=0, column=0, sticky='W')
        self.entry_qtd_cotas.grid(row=0, column=1, padx=5)
        self.label_preco_cota.grid(row=1, column=0, sticky='W')
        self.entry_preco_cota.grid(row=1, column=1, padx=5)
        self.label_ult_divid.grid(row=2, column=0, sticky='W')
        self.entry_ult_divid.grid(row=2, column=1, padx=5)
        self.label_tempo_invest.grid(row=4, column=0, sticky='W')
        self.entry_tempo_invest.grid(row=4, column=1, padx=5)
        self.label_qtd_compra.grid(row=5, column=0, sticky='W')
        self.entry_qtd_compra.grid(row=5, column=1)
        self.button_calculate = Button(self.label_frame_input, text='Calcular', command=self._calculate_dividends)
        self.button_calculate.grid(row=6, column=1, pady=5)
        self.label_frame_result = LabelFrame(self, text='Resultado')
        self.label_frame_result.grid(row=0, column=1, padx=10, pady=10, sticky='W')

    def _init_result_labels(self):
        self.label_result_ano_final = Label(self.label_frame_result, text='Ano Final:')
        self.label_result_qtd_cotas = Label(self.label_frame_result, text='Quantidade de Cotas:')
        self.label_result_valor_total = Label(self.label_frame_result, text='Valor Total Investido:')
        self.label_resultado_divid = Label(self.label_frame_result, text='Próximo pagamento de dividendos:')
        self.label_result_ano_final.grid(row=0, column=0, sticky='W')
        self.label_result_qtd_cotas.grid(row=1, column=0, sticky='W')
        self.label_result_valor_total.grid(row=2, column=0, sticky='W')
        self.label_resultado_divid.grid(row=3, column=0, sticky='W')

    def _calculate_dividends(self):
        try:
            qtd_cotas = int(self.entry_qtd_cotas.get())
            preco_cota = float(self.entry_preco_cota.get())
            dividendo_cota = float(self.entry_ult_divid.get())
            tempo_investimento = int(self.entry_tempo_invest.get())
            qtd_compra = int(self.entry_qtd_compra.get())

            calculator = DividendCalculator()
            result = calculator.calculate(
                qtd_cotas=qtd_cotas,
                preco_cota=preco_cota,
                media_dividendos=dividendo_cota,
                tempo_investimento=tempo_investimento,
                qtd_compra=qtd_compra
            )

        except ValueError:
            # Mostra uma mensagem de erro se os valores não forem válidos
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

        try:
            self.label_result_ano_final.config(text='Ano Final: ' + str(result['Ano Final']))
            self.label_result_qtd_cotas.config(text='Quantidade de Cotas: ' + str(result['Quantidade de Cotas']))
            self.label_result_valor_total.config(text='Valor Total Investido: ' + str(result['Valor Total Investido']))
            self.label_resultado_divid.config(text='Resultado Total de Dividendos: ' + str(result['Recebimento de dividendos (último mês)']))
            
        except UnboundLocalError:
            pass

if __name__ == '__main__':
    app = DividendCalculatorApp()
    app.mainloop()
