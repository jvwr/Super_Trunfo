import json
import random

def sorteador():
    with open("baralho.json","r",encoding="utf-8") as file:
        baralho = json.load(file)
        
        while True:
            carta_aleatoria_1=random.choice(baralho)

            carta_aleatoria_2=random.choice(baralho)

            if carta_aleatoria_1==carta_aleatoria_2:
                continue

            else:
                return carta_aleatoria_1,carta_aleatoria_2


def jogo():

    carta_aleatoria_1, carta_aleatoria_2=sorteador()

    print(f"- Nome: {carta_aleatoria_1['nome']}\n- Força: {carta_aleatoria_1['forca']}\n- Inteligencia: {carta_aleatoria_1['inteligencia']}\n- Influencia: {carta_aleatoria_1['influencia']}\n")

    comparar=str(input("Qual valor vai ser comparado:"))

    if comparar=="forca":
        if {carta_aleatoria_1['forca']} > {carta_aleatoria_2['forca']}:
            print("Jogador ganhou")

        else:
            print("PC ganhou")
    
    if comparar=="inteligencia":
        if {carta_aleatoria_1['inteligencia']} > {carta_aleatoria_2['inteligencia']}:
            print("Jogador ganhou")

        else:
            print("PC ganhou")

    if comparar=="influencia":
        if {carta_aleatoria_1['influencia']} > {carta_aleatoria_2['influencia']}:
            print("Jogador ganhou")

        else:
            print("PC ganhou")




sorteador()

jogo()