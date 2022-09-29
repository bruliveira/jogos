import pygame, sys
from pygame.locals import *



class Menu():
    larguraTela, alturaTela = 1000, 500  # tamanho da tela do game
    metadeLargura = larguraTela / 2
    metadeAltura = alturaTela / 2
    tela = pygame.display.set_mode((larguraTela, alturaTela))



    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 #Posição das opções do menu
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 30, 30)
        self.offset = - 100




    #o seletor do menu
    def draw_cursor(self):
        self.game.draw_text('>>', 20, self.cursor_rect.x, self.cursor_rect.y)


    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

#Parte do Menu inicial
class MainMenu(Menu):


    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Jogar"
        self.startx, self.starty = self.mid_w, self.mid_h
        self.tutorialx, self.tutorialy = self.mid_w, self.mid_h + 40
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 80
        self.exitx, self.exity = self.mid_w, self.mid_h + 120
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)


    def display_menu(self): # Aparência do Menu

        self.run_display = True
        while self.run_display:
            #surface = pygame.display.set_mode((400, 300))
            #color = (255, 0, 0)
            #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
            #pygame.display.flip()

            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.VERDE) #Preenchendo tela da cor preta



            self.game.draw_text('Menu Inicial', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 5)
            #self.game.draw_text("Recorde Atual: ", 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 4)
            self.game.draw_text("Jogar", 30, self.startx, self.starty)
            self.game.draw_text("Como Jogar", 30, self.tutorialx, self.tutorialy)
            self.game.draw_text("História", 30, self.creditsx, self.creditsy)
            self.game.draw_text("Sair", 30, self.exitx, self.exity)
            #self.game.draw_text("Voltar: Backspace", 20, self.mid_w - 200, self.mid_h + 190)
            self.game.draw_text("Avançar: Enter", 20, self.mid_w + 200, self.mid_h + 190)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self): #Movimentação do Cursor (Setinha)

        if self.game.DOWN_KEY:#Usando ceta pra baixo
            if self.state == 'Jogar':
                self.cursor_rect.midtop = (self.tutorialx + self.offset, self.tutorialy)
                self.state = 'Como Jogar'
            elif self.state == 'Como Jogar':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'História'
            elif self.state == 'História':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Sair'
            elif self.state == 'Sair':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Jogar'

        elif self.game.UP_KEY: #Usando ceta pra cima
            if self.state == 'Jogar':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Sair'
            elif self.state == 'Sair':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'História'
            elif self.state == 'Como Jogar':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Jogar'
            elif self.state == 'História':
                self.cursor_rect.midtop = (self.tutorialx + self.offset, self.tutorialy)
                self.state = 'Como Jogar'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Jogar':
                self.game.playing = True
            elif self.state == 'Como Jogar':
                self.game.curr_menu = self.game.options
            elif self.state == 'História':
                self.game.curr_menu = self.game.historia
            elif self.state == 'Sair':
                self.game.exiting = sys.exit()
            self.run_display = False

#Parte de como Jogar. --- está meio ok
class ComoJogarMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.arrowx, self.arrowy = self.mid_w, self.mid_h + 0
        self.rightx, self.righty = self.mid_w, self.mid_h + 60
        self.leftx, self.lefty = self.mid_w, self.mid_h + 90
        self.shotx, self.shoty = self.mid_w, self.mid_h + 120
        self.shotz, self.shoth = self.mid_w, self.mid_h + 150
           
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0,0,0)) #cor preta
            self.game.draw_text('---------- Como Jogar ----------', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3- 50)
            self.game.draw_text("---> Usando teclado <---", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 80)
            self.game.draw_text(" - Direira: -->", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 60)
            self.game.draw_text(" - Esquerda: <--", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 80)
            self.game.draw_text(" - Atira: A", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 100)
            self.game.draw_text(" - Pular: Espaço", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 120)
            self.game.draw_text("Voltar: Backspace", 15, self.game.DISPLAY_W / 6, self.game.DISPLAY_H / 2 + 200)
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.START_KEY:
            pass

#Parte da História. -- meio ok
class HistoriaMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.VERDE)
            self.game.draw_text('Uma criança, e uma única curiosidade enorme..', 28, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 6 + 1)
            self.game.draw_text('Boatos de que, perto da vila tinha uma grande floresta escura e amaldiçoada,', 17, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 10)
            self.game.draw_text('onde quem iria pra lá sumia de uma forma misteriosa, ah, principalmente crianças.!', 17, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 30)
            self.game.draw_text('Um belo dia joãozinho, que é muito curioso, decidiu ir ver essa tal floresta,', 17, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 50)
            self.game.draw_text('Chegando lá, ele achou que tudo que as pessoas falavam era mentira, pois estava ', 17, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 70)
            self.game.draw_text('tudo bem. Ele estava brincando, quando apareceu vários... Zumbis??,', 17, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 90)
            self.game.draw_text('Joãozinho, se ver encuralado agora, e sem nenhuma arma, o que será dele??', 17, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 130)
            self.game.draw_text('Venha ajudar Joãozinho nesse ataque de Zumbis....', 16, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 180)

            self.game.draw_text("Voltar: Backspace", 15, self.mid_w-250, self.mid_h + 200) #Localização: esquerda - direita
            self.blit_screen()