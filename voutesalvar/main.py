from game import Jogo #Pegando o arquivo game e importando a classe jogo

jogo = Jogo() #facilitar

while jogo.running:
    jogo.curr_menu.display_menu()
    jogo.jogo_loop()

pygame.quit()
pygame.quit()