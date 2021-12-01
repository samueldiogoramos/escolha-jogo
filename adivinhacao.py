import random

def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("**********************************")

    limite_rodada:int = 0
    
    while 0 == limite_rodada:
        nivel_jogo:int = int(input("Escolhe entre 1 (baixo) e 3 (alto) qual nível de dificuldade deseja jogar: ")) 

        if 1 == nivel_jogo:
            limite_rodada = 20
        elif 2 == nivel_jogo:
            limite_rodada = 10
        elif 3 == nivel_jogo:
            limite_rodada = 5
        else:
            print("Informe um nível válido entre 1 e 3")

    numero_secreto:int = random.randrange(1, 101)
    acertou:bool = False

    for count in range(1, limite_rodada):
        print("Tentativa {} de {}".format(count, limite_rodada))

        chute:int = int(input("Digite o seu numero:"))

        if chute < 1 or chute > 100:
            print("Favor informar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        chute_maior:bool = chute > numero_secreto

        if (acertou):
            print("Acertou miseravi", end="\n\n")
            break
        elif (chute_maior):
            print("Seu chute foi maior que o número secreto")
        else:
            print("Seu chute foi menor que o número secreto")

    print("Fim do jogo")

if __name__ == "__main__":
    jogar()