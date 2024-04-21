import random

# Definir as cores e os números das cartas
cores = ['Vermelho', 'Amarelo', 'Verde', 'Azul']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Criar o baralho
baralho = []
for cor in cores:
    for numero in numeros:
        baralho.append(cor + ' ' + numero)

# Embaralhar o baralho
random.shuffle(baralho)

# Distribuir as cartas para o jogador e a máquina
mao_jogador = []
mao_maquina = []
for _ in range(7):
    mao_jogador.append(baralho.pop())
    mao_maquina.append(baralho.pop())

# Função para mostrar a mão do jogador
def mostrar_mao_jogador():
    print('Sua mão:')
    for carta in mao_jogador:
        print(carta)

# Função para mostrar a carta do topo da pilha
def mostrar_carta_topo():
    print('Carta do topo:', baralho[-1])

# Função para jogar uma carta
def jogar_carta(carta):
    if carta in mao_jogador:
        mao_jogador.remove(carta)
        baralho.append(carta)
        return True
    else:
        return False

# Loop principal do jogo
while True:
    mostrar_mao_jogador()
    mostrar_carta_topo()

    # Jogada do jogador
    carta_jogador = input('Escolha uma carta para jogar (ou "passar" para comprar uma carta): ')
    if carta_jogador.lower() == 'passar':
        mao_jogador.append(baralho.pop())
    else:
        if jogar_carta(carta_jogador):
            print('Você jogou a carta', carta_jogador)
        else:
            print('Carta inválida!')

    # Jogada da máquina
    carta_maquina = random.choice(mao_maquina)
    if jogar_carta(carta_maquina):
        print('A máquina jogou a carta', carta_maquina)
    else:
        mao_maquina.append(baralho.pop())
        print('A máquina comprou uma carta')

    # Verificar se o jogador ou a máquina ganhou
    if len(mao_jogador) == 0:
        print('Você ganhou!')
        break
    elif len(mao_maquina) == 0:
        print('A máquina ganhou!')
        break