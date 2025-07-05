import json
import random
from InquirerPy import prompt

baralho = r"C:\Users\João Vitor\Desktop\Python\Super_Trunfo\baralho.json"

partida = r"C:\Users\João Vitor\Desktop\Python\Super_Trunfo\partida.txt"


def sorteador():

    with open(baralho, "r", encoding="utf-8") as file:
        cartas = json.load(file)

    while True:
        carta_1 = random.choice(cartas)

        carta_2 = random.choice(cartas)

        if carta_1 != carta_2:
            return carta_1, carta_2


def historico():

    carta_1, carta_2 = sorteador()

    with open(partida, "a", encoding="utf-8") as rodadas:

        rodadas.write("=== CARTA DO JOGADOR ===\n")
        rodadas.write(f"Nome: {carta_1['nome']}\n")
        rodadas.write(f"Força: {carta_1['forca']}\n")
        rodadas.write(f"Inteligência: {carta_1['inteligencia']}\n")
        rodadas.write(f"Influência: {carta_1['influencia']}\n\n")

        rodadas.write("=== CARTA DO PC ===\n")
        rodadas.write(f"Nome: {carta_2['nome']}\n")
        rodadas.write(f"Força: {carta_2['forca']}\n")
        rodadas.write(f"Inteligência: {carta_2['inteligencia']}\n")
        rodadas.write(f"Influência: {carta_2['influencia']}\n")


def jogo():

    carta_1, carta_2 = sorteador()

    print(f"- Nome: {carta_1['nome']}\n- Força: {carta_1['forca']}\n- Inteligencia: {carta_1['inteligencia']}\n- Influencia: {carta_1['influencia']}\n")

    comparar = [
        {
            "type": "list",
            "name": "atributo",
            "message": "Qual valor vai ser comparado: ",
            "choices": ['forca', 'inteligencia', 'influencia']
        }
    ]

    resultado = prompt(comparar)["atributo"]

    if carta_1['trunfo'] is True:
        print("Jogador ganhou")
        print("Carta Trunfo")
        return

    elif carta_2['trunfo'] is True:
        print("PC ganhou")
        print("Carta Trunfo")
        return

    if resultado not in ['forca', 'inteligencia', 'influencia']:
        print("Valor invalido!")
        return False

    if carta_1[resultado] > carta_2[resultado]:
        print("Jogador ganhou")

    elif carta_1[resultado] == carta_2[resultado]:
        print("Empate")

    else:
        print("PC ganhou")

        print("\nCartas do PC:")

    print(f"\n- Nome: {carta_2['nome']}\n- Força: {carta_2['forca']}\n- Inteligência: {carta_2['inteligencia']}\n- Influência: {carta_2['influencia']}\n")


sorteador()
jogo()
