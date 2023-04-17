import random
from time import *

# Define o tamanho do código e as cores disponíveis
quantidade_cor = 4
colors = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo', 'ciano']
cores_disponivel = ['\033[41m vermelho \033[m', '\033[44m azul \033[m', '\033[42m verde \033[m', '\033[43m amarelo \033[m', '\033[45m roxo \033[m', '\033[46m ciano \033[m']

# Gera a senha
senha = random.sample(colors, quantidade_cor)
#guarda a quantidade de tentativas
chances = 0

# Obtém uma jogada do jogador
def chute():
    #loop para perguntar
    
    while True:
        global chances
        palpite = input('Digite a sua jogada (ex: vermelho azul verde amarelo): ').split()
        chances += 1
        #verifica se foi digitado 4 cores
        if len(palpite) == quantidade_cor and all(color in colors for color in palpite):
            return palpite
        print('Jogada inválida. Tente novamente.')
        
        
    
# Calcula quantas cores estão corretas e quantas estão na posição correta
def verifica_palpite(code, palpite):
    #se o palpite é igual a senha, posiçã correta e cor certa
    correta = sum(1 for i in range(quantidade_cor) if palpite[i] == code[i])
    #cor correta e posição errada
    color_correta = sum(min(code.count(palpite[i]), palpite.count(palpite[i])) for i in range(quantidade_cor)) - correta
    return correta, color_correta

# Imprime as dicas para a jogada atual
def impressao(palpite, correta, color_correta):
    sleep(0.5)
    print("Calculando...")
    #se estiver tudo correto
    if correta == quantidade_cor:
        print('\033[42mPARABÉNS, você acertou o código!\033[m')
        return True
    #PINOS PRETO - maior que zero pq incrementa
    if correta > 0:       
        print(f'\033[1mPINOS PRETOS\033[m: {correta} cor(es) estão correta(s) e na posição certa.')
    #PINOS BRANCOS - maior que 0 pq incrementa o minimo
    if color_correta > 0:
        print(f'\033[47mPINOS BRANCOS\033[m: {color_correta} cor(es) estão correta(s) mas na posição errada.')
    #nada incrementado, nada certo
    if correta == 0 and color_correta == 0:
        print('Nenhuma cor está correta.')
    print('=' * 10)
    return False

# inicio do jogo

print('=' * 25)
print(f'Bem-vindo ao Mastermind!')
print('=' * 25)
print(f'Tente adivinhar a senha de {quantidade_cor} cores.')
print(f'>> Cores disponiveis:')
print('-'.join(cores_disponivel))
print('Você possui 10 tentativas')
print('=' * 25)
code = senha
while True:
    #para verificar na linha 65
    palpite = chute()
    #verifica os digitos
    correta, color_correta = verifica_palpite(code, palpite)
    #caso não acerte em 10 tentativas
    match chances :
        case 10:
            print('Você perdeu, a senha: {} '.format('-'.join(senha)))
            break
    #se estiver correta - fim
    if impressao(palpite, correta, color_correta):
        break


