import random

def jogar():
    mensagem_inicio()

    palavra_secreta:str = escolha_palavra_secreta()
    array_palavra_secreta:str = cria_array_palavra_secreta(palavra_secreta)

    limite_qtd_tentativa:int = define_limite_qtd_tentativa(len(palavra_secreta))
    qtd_tentativa:int = 0
    enforcou:bool = False

    while not enforcou:
        chute:str = input("Qual letra: ")

        if existe_letra_palavra_certa(chute, palavra_secreta):
            verifica_chute(palavra_secreta=palavra_secreta, chute=chute, array_palavra_secreta=array_palavra_secreta)

            if not "_" in array_palavra_secreta:
                print("\nVc venceu!!! Paravra secreta é {}.\n".format(palavra_secreta.upper()))

                break

            if qtd_tentativa == limite_qtd_tentativa:
                print("\nVc perdeu!!! Paravra secreta era {}.\n".format(palavra_secreta.upper()))

                break

        qtd_tentativa = qtd_tentativa + 1
        print(array_palavra_secreta)

    mensagem_fim()

def mensagem_inicio():
    print("**********************************")
    print("Bem vindo ao jogo da forca")
    print("**********************************")

def mensagem_fim():
    print("**********************************")
    print("Fim do jogo")
    print("**********************************")

def define_limite_qtd_tentativa(tamanho_palavra:int):
    return tamanho_palavra + 3

def verifica_chute(palavra_secreta:str, chute:str, array_palavra_secreta:str):
    index:int = 0

    for letra in palavra_secreta:
        if letra.upper() == chute.upper().strip():
            array_palavra_secreta[index] = chute

        index = index + 1

def convert_list_to_str(lista:str) -> str:
    return ''.join([str(texto) for texto in lista]).upper()

def existe_letra_palavra_certa(letra:str, palavra_secreta:str) -> bool:
    return True if palavra_secreta.find(letra) > -1 else False

def cria_array_palavra_secreta(palavra_secreta:str):
    separador:str = "_"
    array_palavra_secreta:str = []

    for i in palavra_secreta:
        array_palavra_secreta.append(separador)

    return array_palavra_secreta

def escolha_palavra_secreta() -> str:
    palavras_secretas:str = []

    with open("palavras_secretas.txt", "r") as _:
        palavras_secretas = _.readlines()

    return palavras_secretas[random.randrange(0, len(palavras_secretas))].strip()

if __name__ == "__main__":
    jogar()