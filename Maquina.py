from Jogador import Jogador
from collections import deque

class Maquina(Jogador):
    """
    Classe que representa a IA do jogo da velha.

    Atributos:
        nome (str): O nome da Maquina ('IA' por padrão).
        simbolo (str): O símbolo usado pela IA ('O' por padrão).

    Métodos:
        fazer_jogada(tabuleiro):
            Realiza a jogada da IA no tabuleiro, usando o algoritmo de busca em largura.

        bfs(tabuleiro, profundidade_maxima, profundidade_atual):
            Implementa o algoritmo de busca em largura.
    """
    def __init__(self, nome, simbolo, algoritmo):
        """
        Inicializa a IA.

        Parâmetros:
            nome (str): O nome da Maquina ('IA' por padrão).
            simbolo (str): O símbolo usado pela IA ('O' por padrão).
            algoritmo (int): Decide qual algoritmo utilizar na maquina(1 = MinMax, 2 = BFS)

        """
        self.algoritmo = algoritmo #1 = minmax, 2 = bfs
        super().__init__(nome, simbolo)

    def fazer_jogada(self, tabuleiro):
        """
        Realiza a jogada da IA no tabuleiro, usando o algoritmo de busca em largura.

        Parâmetros:
            tabuleiro (Tabuleiro): O objeto do tabuleiro onde a respectiva jogada será feita.
        """
        print("TURNO: IA\n")
        if self.algoritmo == 1:
            jogada = self.minmax(tabuleiro)
            tabuleiro.registra_jogada(jogada, self.simbolo)
        else:
            jogada = self.bfs(tabuleiro)
            if jogada is not None:
                tabuleiro.registra_jogada(jogada, self.simbolo)
            else:
                while jogada is None:
                    jogada = self.bfs(tabuleiro)
                tabuleiro.registra_jogada(jogada, self.simbolo)

    def minmax(self, tabuleiro):
        """
        Implementa o algoritmo de minmax para determinar a jogada.

        Parâmetros:
            tabuleiro (Tabuleiro): O objeto do tabuleiro onde a respectiva jogada será avaliada.
            profundidade_maxima (int): A profundidade máxima da busca.
            profundidade_atual (int): A profundidade atual da busca.

        Retorno:
            int: O número da casa onde a IA deseja jogar.

        """
        if tabuleiro.verifica_vitoria(self.simbolo):
            return 1
        elif tabuleiro.verifica_vitoria("X"):
            return -1
        elif tabuleiro.verifica_empate():
            return 0

        melhor_valor = -float("inf")
        melhor_jogada = None

        # Verifica primeiro se o jogador pode ganhar na próxima jogada
        for jogada in range(1, 10):
            linha = (jogada - 1) // 3
            coluna = (jogada - 1) % 3

            if tabuleiro.tabuleiro[linha][coluna] != " ":
                continue  # Ignore casas já ocupadas

            tabuleiro.registra_jogada(jogada, "X")

            # Verifica se a próxima jogada do jogador levaria à vitória
            if tabuleiro.verifica_vitoria("X"):
                tabuleiro.desfaz_jogada(jogada)
                return jogada  # Bloqueia a vitória do jogador

            tabuleiro.desfaz_jogada(jogada)

        # Se o jogador não pode ganhar na próxima jogada, realize jogada para vitória
        for jogada in range(1, 10):
            linha = (jogada - 1) // 3
            coluna = (jogada - 1) % 3

            if tabuleiro.tabuleiro[linha][coluna] != " ":
                continue  # Ignore casas já ocupadas

            tabuleiro.registra_jogada(jogada, self.simbolo)

            valor = -self.minmax(tabuleiro)
            tabuleiro.desfaz_jogada(jogada)

            if valor > melhor_valor:
                melhor_valor = valor
                melhor_jogada = jogada

        return melhor_jogada
    
    def bfs(self, tabuleiro):
        """
        Implementa o algoritmo de busca em largura (Breadth-First Search - BFS) para a jogada da IA.

        Parâmetros:
            tabuleiro (Tabuleiro): O objeto do tabuleiro atual.

        Retorno:
            int or None: O número da casa onde a IA deseja jogar, ou None se nenhuma jogada estratégica for encontrada.

        """
        fila = deque()

        # Gerar todas as jogadas possíveis para a IA (símbolo "O")
        for jogada in range(1, 10):
            linha = (jogada - 1) // 3
            coluna = (jogada - 1) % 3
            if tabuleiro.tabuleiro[linha][coluna] == " ":
                novo_tabuleiro = tabuleiro.copia()
                novo_tabuleiro.registra_jogada(jogada, self.simbolo)
                fila.append((novo_tabuleiro, jogada))

        # Verificar se alguma dessas jogadas resulta em vitória para a IA
        for estado, jogada in fila:
            if estado.verifica_vitoria(self.simbolo):
                return jogada

        # Se não houver jogadas vencedoras para a IA, tentamos bloquear as jogadas do jogador "X"
        for estado, jogada in fila:
            for nova_jogada in range(1, 10):
                linha = (nova_jogada - 1) // 3
                coluna = (nova_jogada - 1) % 3
                if estado.tabuleiro[linha][coluna] == " ":
                    estado.registra_jogada(nova_jogada, "X")
                    if estado.verifica_vitoria("X"):
                        return jogada

        # Se nenhuma jogada vencedora ou bloqueadora for encontrada, retorne None
        return None