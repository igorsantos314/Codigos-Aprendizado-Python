from tkinter import *
from random import randint, choice

class mapaTricolor:

    def __init__(self):
        self.colors = ['#00FFFF', '#00CED1', '#40E0D0', '#48D1CC', '#20B2AA', '#008B8B', '#008080']

        self.window = Tk()
        self.window.geometry('1080x820')

        self.matrizColors()
        #print(self.desenho()[10][10])

        self.window.mainloop()

    def matrizColors(self):

        for posX, x in enumerate(range(10, 1000, 30)):
            for posY, y in enumerate(range(10, 800, 30)):
        
                try:
                    if self.desenho()[posY][posX] == ['']:
                        corNumber = 'black'

                    elif self.desenho()[posY][posX] == ['+']:
                        corNumber = 'red'

                    else:
                        corNumber = self.getColor()

                except:
                    pass

                self.btModelo = Button(text='', width=1, height=1)
                self.btModelo['bg'] = corNumber
                self.btModelo.place(x=x, y=y)

    def desenho(self):

        ilustracao =  [
            ['','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','o','o','o','','o','','','','o','','','','o','o','o','','o','','','o',''],
            ['','','','','','','','o','','','','o','','','','o','','','','o','','','','o','','','o',''],
            ['','','','','','','','o','o','','','o','','','','o','','','','o','o','','','o','o','','o',''],
            ['','','','','','','','o','','','','o','','','','o','','','','o','','','','o','','o','o',''],
            ['','','','','','','','o','o','o','','o','o','o','','o','o','o','','o','o','o','','o','','','o',''],
            ['','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','+','+','','','','','','+','+','','','','','','',''],
            ['','','','','','','','','','','','+','+','+','+','','','','+','+','+','+','','','','','',''],
            ['','','','','','','','','','','+','','','','','+','','+','+','+','+','+','+','','','','',''],
            ['','','','','','','','','','+','','','','','','','+','+','+','+','+','+','+','+','','','',''],
            ['','','','','','','','','+','','','','','','','','+','+','+','+','+','+','+','+','+','','',''],
            ['','','','','','','','','+','','','','','','','','+','+','+','+','+','+','+','+','+','','',''],
            ['','','','','','','','','','+','','','','','','','+','+','+','+','+','+','+','+','','','',''],
            ['','','','','','','','','','','+','','','','','','+','+','+','+','+','+','+','','','','',''],
            ['','','','','','','','','','','','+','','','','','+','+','+','+','+','+','','','','','',''],
            ['','','','','','','','','','','','','+','','','','+','+','+','+','+','','','','','','',''],
            ['','','','','','','','','','','','','','+','','','+','+','+','+','','','','','','','',''],
            ['','','','','','','','','','','','','','','+','','+','+','+','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','+','+','+','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','+','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
            ['','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
        ]

        self.novaLista = []

        for i in ilustracao:
            
            listaInterior = []
            
            for j in i:
                listaInterior.append([j])

            self.novaLista.append(listaInterior)

        return self.novaLista

        print(x, y)

    def changeColor(self):
        cor = 'orange'

        self.btModelo['bg'] = cor

    def getColor(self):

        n = randint(0, 60)
        cor = ''

        if n < 11:
            cor = self.colors[0]

        elif n < 21:
            cor = self.colors[1]

        elif n < 31:
            cor = self.colors[2]

        elif n < 41:
            cor = self.colors[3]

        elif n < 51:
            cor = self.colors[4]

        elif n < 61:
            cor = self.colors[5]

        return cor

mapaTricolor()
        


