import json
import random

baralho = r"C:\Users\João Vitor\Desktop\Python\Super_Trunfo\baralho.json"



print("Bom dia, boa tarde, boa noite!!!\nApresento a vocês o jogo Super Trunfo.\n")

print("Super Trunfo é um jogo de cartas em que cada carta tem vários atributos. Na sua vez, o jogador escolhe um atributo da carta do topo do seu monte, e todos os jogadores comparam esse valor. Quem tiver o maior, vence a rodada e pega as cartas.\n")



def sorteador():

    with open(baralho, "r", encoding="utf-8") as file:
        cartas = json.load(file)

    while True:
        carta_1 = random.choice(cartas)

        carta_2 = random.choice(cartas)

        if carta_1 != carta_2:
            return carta_1, carta_2


def jogo():

    carta_1, carta_2 = sorteador()

    print(f"- Nome: {carta_1['nome']}\n- Força: {carta_1['forca']}\n- Inteligencia: {carta_1['inteligencia']}\n- Influencia: {carta_1['influencia']}\n")

    comparar = str(input("Qual valor vai ser comparado:")).lower().strip()

    if carta_1['trunfo'] == True:
        print("Jogador ganhou")
        print("Carta Trunfo")
        return

    elif carta_2['trunfo'] == True:
        print("PC ganhou")
        print("Carta Trunfo")
        return

    if comparar not in ['forca', 'inteligencia', 'influencia']:
        print("Valor invalido!")
        return False


    if carta_1[comparar] > carta_2[comparar]:
        print("Jogador ganhou")

    elif carta_1[comparar] == carta_2[comparar]:
        print("Empate")

    else:
        print("PC ganhou")

        print("\nCartas do PC:")

    print(f"\n- Nome: {carta_2['nome']}\n- Força: {carta_2['forca']}\n- Inteligencia: {carta_2['inteligencia']}\n- Influencia: {carta_2['influencia']}\n")




def main():
    while True:
        resultado = jogo()
        if resultado is False:
            continue
        novamente = str(input("Querer jogar mais uma rodada? "))
        if novamente != "sim":
            print("Jogatina encerada")
            break

if __name__ == "__main__":
    main()
