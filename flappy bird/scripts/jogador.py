import pygame

class Jogador: # cria uma classe jogador

    def __init__(self,tela, x, y): # def indica uma função, e __init__ é uma palavra reservada que sempre é
        # chama quando usamos a classe; self também é reservado e indica que o objeto criado terá informações
        # próprias, ou seja, a variável pode receber a posição do jogador. x e y são passados na tela em que
        # definimos nosso jogador
        self.posicao = [x, y] # a posicão do jogador é o x y que usamos ao criar a classe
        self.tamanho = [32, 32] # cria um valor, self.varavel que indica um valor da classe
        self.rect = pygame.Rect(self.posicao, self.tamanho) # rect é uma classe do pygame amplamente utilizada
        # para detectar colisão.

        self.contador = 0 # cria uma variável para contar quantas atualizações necessárias antes de mudar de imagem
        self.imagemAtual = 0 # variável que indica qual a imagem atual
        self.tela = tela # tela reflete a tela da classe jogador como a tela que passamos
        self.listaImagens = [] # cria uma lista onde vamos inserir as imagens do jogador

        for i in range(3): # laço que vai pegar as 3 imagens do jogador e adicionar na lista
            imagem = pygame.image.load('assets/passaro-'+str(i)+'.png')
            # a função load serve para “pegar” as imagens e guardar na variável imagem
            imagem = pygame.transform.scale(imagem, self.tamanho)
            # a função scale muda a imagem para o tamanho especificado
            self.listaImagens.append(imagem)
            # por fim usamos a função append para inserir a imagem na lista de imagens

        # cria variáveis para gerenciar a velocidade, 1/60 serve para calcular em segundos
        self.velocidadeAtual = 0
        self.gravidade = 1/60*10
        self.velocidadeMaxima = 1/60*100


    def desenhar(self): # cria uma função que desenha o jogador
        self.contador += 1 # soma 1 no contador
        if self.contador > 5: # verifica se o contador é maior que 5
            self.contador = 0 # caso seja maior que 5, define como zero
            self.imagemAtual = (self.imagemAtual + 1) % 3 # adiciona 1 na variável imagemAtual e pega o resto da
            # divisão por 3 usando o sinal %, que pode apenas, 0, 1 ou 2.
        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao) # usa a função blit para desenhar a
        # imagem em tela


    def atualizar(self): # cria uma função que atualiza o jogador
        self.velocidadeAtual = min(self.velocidadeAtual + self.gravidade, self.velocidadeMaxima) # adiciona a
        # velocidade atual
        self.posicao = [self.posicao[0], self.posicao[1] + self.velocidadeAtual] # adiciona a velocidade atual no Y
        self.rect = pygame.Rect(self.posicao, self.tamanho) # atualiza o rect para o novo tamanho do jogador

        self.teclas = pygame.key.get_pressed() # pega todas as teclas pressionadas
        if self.teclas[pygame.K_SPACE]: # verifica se a tecla espaço foi pressionada
            self.velocidadeAtual = -self.velocidadeMaxima*2 # define a velocidade como negativa e multiplica por 2,
            # fazendo o jogador subir


    def getRect(self):
        return pygame.Rect(self.posicao,self.tamanho)
        # retorna a rect do jogador para fins de colisão
