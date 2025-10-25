import pygame
import colors

cl = colors.colors
def main():
    pygame.init()
    tela = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Janela PyGame")
    clock = pygame.time.Clock()
    sup1 = pygame.Surface((200, 200))
    sup1.fill(cl['cinza_claro'])
    sup2 = pygame.Surface((150, 150))
    sup2.fill(cl['cinza_medio'])
    sup3 = pygame.Surface((100, 100))
    sup3.fill(cl['cinza_escuro'])

    ret = pygame.Rect(10, 10, 45, 45)

    # Loop principal
    executando = True
    while executando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ret.move_ip(-5,0)
                if event.key == pygame.K_RIGHT:
                    ret.move_ip(5,0)
                if event.key == pygame.K_UP:
                    ret.move_ip(0,-5)
                if event.key == pygame.K_DOWN:
                    ret.move_ip(0,5)
                if event.key == pygame.K_SPACE:
                    ret.move_ip(5,5)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(1280/2, 720/2)

        clock.tick(30)
        tela.fill(cl['branco'])
        tela.blit(sup1,[3,15])
        tela.blit(sup2,[3,15])
        pygame.draw.rect(tela, cl['vermelho_claro'], ret)
        tela.blit(sup3,[3,15])
        ret.left, ret.top = pygame.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2
        pygame.display.update()
    pygame.quit()

main()