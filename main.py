import adivinhacao
import forca

print("**********************************")
print("Escolha um jogo...")
print("**********************************")

escolha:int = int(input("Digite (1) para o jogo de adivinhação e (2) para o jogo da forca:"))

if 1 == escolha:
    adivinhacao.jogar()
elif 2 == escolha:
    forca.jogar()