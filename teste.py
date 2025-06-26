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
                carta1=(f"- Nome: {carta_aleatoria_1['nome']}\n- Força: {carta_aleatoria_1['forca']}\n- Intelugencia: {carta_aleatoria_1['inteligencia']}\n- Influencia: {carta_aleatoria_1['influencia']}\n")
                carta2=(f"- Nome: {carta_aleatoria_2['nome']}\n- Força: {carta_aleatoria_2['forca']}\n- Intelugencia: {carta_aleatoria_2['inteligencia']}\n- Influencia: {carta_aleatoria_2['influencia']}")
                break
    


def jogo():

