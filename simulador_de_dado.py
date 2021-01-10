# Simulador de dado
#Simular o uso de um dado, gerando um numero de 1 até 6

import random
import PySimpleGUI as sg




class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6       

        #Layout 
        self.layout = [
            [sg.Text('Jogar o dado')],
            [sg.Button('sim'),sg.Button('nãos')]
        ]
        
    
    def Iniciar(self):
        #Janela
        self.janela = sg.Window('Simulador de dado',Layout=self.layout)
        #Ler valores da janela
        self.eventos, self.valores = self.janela.Read()
        #Manipular valores
        while True:       
            try:
                if self.eventos == 'sim' or self.eventos == 's':
                    self.GerarValorDoDado()
                elif self.eventos == 'não' or self.eventos == 'n':
                    print('Agradecemos sua participação!')
                else:
                    print('Favor digitar sim ou não')
            except:
                print('Ocorreu um erro ao receber sua resposta')


    
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()