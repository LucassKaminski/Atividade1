import pygame

pygame.init()

preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
largura = 950
altura = 700
rodando = True

pygame.display.set_caption('Forca 3!')
tela = pygame.display.set_mode((largura, altura))
fonte = pygame.font.Font(None, 50)
fonte_pequena = pygame.font.Font(None, 28)


def forca(stade):
    pygame.draw.line(tela, preto, (150, 500), (450, 500), 5)  # Base
    pygame.draw.line(tela, preto, (300, 500), (300, 150), 5)  # Poste
    pygame.draw.line(tela, preto, (300, 150), (400, 150), 5)  # Viga
    pygame.draw.line(tela, preto, (400, 150), (400, 200), 5)  # Corda

    # Desenho do boneco conforme o estado
    if stade >= 1:  # Cabeça
        pygame.draw.circle(tela, preto, (400, 250), 25, 5)
    if stade >= 2:  # Corpo
        pygame.draw.line(tela, preto, (400, 275), (400, 375), 5)
    if stade >= 3:  # Braço esquerdo
        pygame.draw.line(tela, preto, (400, 300), (350, 350), 5)
    if stade >= 4:  # Braço direito
        pygame.draw.line(tela, preto, (400, 300), (450, 350), 5)
    if stade >= 5:  # Perna esquerda
        pygame.draw.line(tela, preto, (400, 375), (350, 450), 5)
    if stade >= 6:  # Perna direita
        pygame.draw.line(tela, preto, (400, 375), (450, 450), 5)


estado = 0
palavra_secreta = str(input('Digite a palavra secreta: '))


while rodando:
    tela.fill(branco)
    forca(estado)
    palavra_jogo = ' '.join(palavra_secreta)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            break
    pygame.display.flip()
pygame.quit()
