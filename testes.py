import json
import random

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


sorteador()
historico()