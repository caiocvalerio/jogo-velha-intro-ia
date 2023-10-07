from Tabuleiro import Tabuleiro
from Jogador import Jogador
from Maquina import Maquina

"""
Inicializar os jogadores em caso de um único jogador adicionar a IA como oponente
"""
jogadores = int(input("Quantos jogadores?(Max: 2) "))
if jogadores > 2 or jogadores < 1:
    print("Numero de jogadores inserido inválido")
    while jogadores > 2 or jogadores < 1:
      jogadores = int(input("Quantos jogadores?(Max: 2) "))

if jogadores == 1:
  nome_jogador1 = input("Insira nome do jogador 1: ")
  jogador1 = Jogador(nome_jogador1, "X")
  jogador2 = Maquina("IA", "O", 2)

else:
  nome_jogador1 = input("Insira nome do jogador 1: ")
  simbolo_jogador1 = input("Insira o simbolo desejado(X ou O): ").upper()
  while simbolo_jogador1 != "X" and simbolo_jogador1 != "O":
    print("Simbolo inserido incorreto. Os simbolos permitidos são X ou O.")
    simbolo_jogador1 = input("Insira o simbolo desejado(X ou O): ").upper()
  jogador1 = Jogador(nome_jogador1, simbolo_jogador1)

  nome_jogador2 = input("Insira nome do jogador 2: ")
  if simbolo_jogador1 == "X":
    simbolo_jogador2 = "O"
  else:
    simbolo_jogador2 = "X"
  jogador2 = Jogador(nome_jogador2, simbolo_jogador2)
print("*************************************\n")


"""
Inicializar o tabuleiro
"""

if jogador1.simbolo == "X": #jogador 1 escolheu X, então ele começa jogando, sendo esse caso também para IA
    tabuleiro = Tabuleiro(jogador1)
  
else: #jogador 2 escolheu X, então ele começa jogando
    tabuleiro = Tabuleiro(jogador2)

"""
Loop principal do jogo da velha
"""

tabuleiro.game_loop(jogador1, jogador2)
