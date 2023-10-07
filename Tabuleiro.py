class Tabuleiro:
    """
    Classe responsável pelo tabuleiro no jogo da velha

    Atributos:
        tabuleiro (lista): lista que representa o tabuleiro

    Metodos:
        mostrar_tabuleiro():
            Expõe o atual estado do tabuleiro
        
        registra_jogada(casa, jogador):
            Realiza o registro da jogada no tabuleiro
        
        verifica_vitoria(jogador):
            Verifica se o respectivo jogador ganhou o jogo

        verifica_empate():
            Verifica se o jogo terminou em empate
        
        msg_vitoria(jogador):
            Apresenta a mensagem de vitória ao respectivo jogador
        
        msg_empate():
            Apresenta a mensage de empate aos respectivos jogadores.
    """
    def __init__(self, jogador_atual):
        """
        Cria um novo tabuleiro com um jogador atual específico.

        Parametros:
            jogador_atual(Jogador): o próximo a jogar
        
        Atributos:
            tabuleiro (list): uma lista 3x3 que representa o tabuleiro do jogo
            jogador_atual (Jogador): o próximo a jogar
        """
        self.tabuleiro = [[" "] * 3 for _ in range(3)]
        self.jogador_atual = jogador_atual
    
    def mostrar_tabuleiro(self):
        """
        Imprime o estado atual do tabuleiro, sendo que para casa vazia substituir pelo respectivo número(1...9) 
        e caso contrário substituir pelo respectivo valor(X ou O)
        """
        for i, linha in enumerate(self.tabuleiro):
            for j, valor in enumerate(linha):
                if valor == " ":
                    """
                    Calculo do respectivo número a ser inserido em cada casa que não conter um valor inserido
                    """
                    casa = (i * 3) + j + 1
                    print(f" {casa} ", end="")
                else:
                    print(f" {valor} ", end="")

                if j < 2:
                    print("|", end="")

            print()
            if i < 2:
                print("---+---+---")

    def registra_jogada(self, casa, jogador):
        """
        Realiza o registro da jogada de um jogador no tabuleiro

        Parametros:
            casa(int): número da respectiva casa a inserir o valor do respectivo jogador (1 a 9)
            jogador(str): simbolo do respectivo jogador (X ou O)

        Retorno:
            bool: retorna se a jogada foi bem sucedida(True) ou não(False).
        """

        if casa < 1 or casa > 9:
            print("Entrada inválida. Digite um valor de 1 a 9.")
            return False

        linha = (casa - 1)//3
        coluna = (casa - 1)%3

        if self.tabuleiro[linha][coluna] != "X" and self.tabuleiro[linha][coluna]!= "O":
            self.tabuleiro[linha][coluna] = jogador
            return True
        else:
            print("Casa ocuada. Escolha outra casa.")
            return False

    def verifica_vitoria(self, jogador):
        """
        Verifica se um jogador venceu

        Parametro:
            jogador(str): O simbolo correspondente do jogador(X ou O).

        Retorno:
            bool: Verdadeiro em caso de vitória e falso caso contrário
        """
        for linha in self.tabuleiro:
            if linha.count(jogador) == 3:
                return True

        for coluna in range(3):
            if all(self.tabuleiro[linha][coluna] == jogador for linha in range(3)):
                return True

        if all(self.tabuleiro[i][i] == jogador for i in range(3)) or \
           all(self.tabuleiro[i][2 - i] == jogador for i in range(3)):
            return True

        return False    

    def verifica_empate(self):
        """
        Verifica se o jogo terminou em empate

        Retorno:
            bool: Verdadeiro em caso de empate e falso caso contrário
        """
        for linha in self.tabuleiro:
            for casa in linha:
                if casa != "X" and casa != "O":
                    return False
        
        return True
    
    def msg_vitoria(self, jogador):
        """
        Apresenta a mensagem de vitória ao respectivo jogador

        Parametro:
            jogador(str): O nome do jogador que ganhou.
        """
        self.mostrar_tabuleiro()
        print(f"Vitória do {jogador}!")
        input("Pressione enter para fechar.")

    def msg_empate(self):
        """
        Apresenta a mensagem de empate do respectivo jogo.
        """

        self.mostrar_tabuleiro()
        print("Empate!")
        input("Pressione enter para fechar.")

    def game_loop(self, jogador1, jogador2):
        """
        Método responsável pelo loop principal do jogo da velha

        Parametro:
            jogador1(Jogador): jogador numero 1
            jogador2(Jogador): jogador numero 2
        """
        jogador_atual = self.jogador_atual
        while True:
            self.mostrar_tabuleiro() 
            jogador_atual.fazer_jogada(self)
            
            if self.verifica_vitoria(jogador_atual.simbolo):
                self.msg_vitoria(jogador_atual.nome)
                break
            
            if self.verifica_empate():
                self.msg_empate()
                break

            jogador_atual = jogador2 if jogador_atual == jogador1 else jogador1
    
    def desfaz_jogada(self, casa):
        """
        Desfaz uma jogada anterior realizada no tabuleiro, se a casa não estiver vazia.

        Parâmetros:
            casa (int): O número da casa (1 a 9) onde deseja desfazer a jogada.

        """

        linha = (casa - 1) // 3
        coluna = (casa - 1) % 3

        if self.tabuleiro[linha][coluna] != " ":
            self.tabuleiro[linha][coluna] = " "
        else:
            print("Erro ao desfazer jogada: a casa já estava vazia.")

    def copia(self):
        """
        Cria uma cópia do estado atual do tabuleiro.

        Retorna:
            Tabuleiro: Uma nova instância do tabuleiro com o mesmo estado do tabuleiro atual.

        """
        novo_tabuleiro = Tabuleiro(self.jogador_atual)

        for i in range(3):
            for j in range(3):
                novo_tabuleiro.tabuleiro[i][j] = self.tabuleiro[i][j]

        return novo_tabuleiro