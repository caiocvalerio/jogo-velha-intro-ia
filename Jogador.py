class Jogador:
    """
    Classe que representa o jogador.

    Atributos:
        nome (str): O nome do jogador
        simbolo (str): O símbolo usado pelo jogador ('X' ou 'O')

    Metodos:
        fazer_jogada(tabuleiro):
            Realizar a jogada do respectivo jogador no tabuleiro
    """
    def __init__(self, nome, simbolo):
        """
        Inicializa um novo jogador com um nome e um símbolo.

        Parametro:
            nome (str): O nome do jogador.
            simbolo (str): O símbolo usado pelo jogador ('X' ou 'O').
        """
        self.nome = nome
        self.simbolo = simbolo
    
    def fazer_jogada(self, tabuleiro):
        """
        Permite que o respectivo jogador realize uma jogada no tabuleiro.

        Parametro:
            tabuleiro (Tabuleiro): O objeto do tabuleiro onde a jogada será feita.
        """
        while True:
            try:
                casa = int(input(f"TURNO: {self.nome}\nInsira valor da casa(1 a 9): "))
                print()
                if tabuleiro.registra_jogada(casa, self.simbolo):
                    return
            
            except ValueError:
                print("Erro JFJ01: ValueError. Insira outra casa.")
