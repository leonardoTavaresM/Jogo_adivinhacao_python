import random


def jogar():
    print('Bem vindo ao pycharm')
    print("********************")
    print("Jogo de Adivinhação")
    print("********************")

    numero_secreto = round(random.randrange(1, 101))
    total_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nivel: '))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        # print(f'Tentativa {rodada} de {total_tentativas}')
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('Voce acertou e fez {} pontos'.format(pontos))
            break
        else:
            if (maior):
                print('voce errou! O seu chute foi maior que o numero secreto')
            elif (menor):
                print('voce errou! O seu chute foi menor que o numero secreto')
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("Fim do jogo")

    print('o numero secreto era {}'.format(numero_secreto))


if (__name__ == '__main__'):
    jogar()
