import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor, tamanho):
        self.tela = tela
        self.texto = texto
        self.posicao = (x, y)
        self.cor = cor
        self.tamanho = tamanho

        pygame.font.init()
        self.fonte = pygame.font.Font(None, self.tamanho)
        self.imagemTexto = self.fonte.render(self.texto, True, self.cor)

    def desenhar(self):
        self.tela.blit(self.imagemTexto, self.posicao)

    def atualizarTexto(self, novoTexto):
        self.imagemTexto = self.fonte.render(novoTexto, True, self.cor)


class Botao:
    def __init__(self, tela, texto, x, y, tamanho, corFundo, CorTexto):
        self.tela = tela
        self.texto = Texto(tela, texto, x, y, CorTexto, tamanho)
        self.posicao = (x, y)
        self.corFundo = corFundo

    def desenhar(self):
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())
        pygame.draw.rect(self.tela, self.corFundo, rect)
        self.texto.desenhar()

    def get_click(self):
        posMouse = pygame.mouse.get_pos()
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())

        if rect.collidepoint(posMouse) and pygame.mouse.get_pressed()[0]:
            return True
        return False
