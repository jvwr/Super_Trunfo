import json
import random

print("Bom dia, boa tarde, boa noite!!!\nApresento a vocês o jogo Super Trunfo.\n")

print("Super Trunfo é um jogo de cartas em que cada carta tem vários atributos. Na sua vez, o jogador escolhe um atributo da carta do topo do seu monte, e todos os jogadores comparam esse valor. Quem tiver o maior, vence a rodada e pega as cartas.\n")


def jogo_completo():
    
    while True:


        def sorteador():
            with open(r"C:\Users\João Vitor\Desktop\Python\Super_Trunfo\baralho.json","r",encoding="utf-8") as file:
                baralho = json.load(file)
                
                while True:
                    carta_1=random.choice(baralho)

                    carta_2=random.choice(baralho)

                    if carta_1==carta_2:
                        continue

                    else:
                        return carta_1,carta_2


        def jogo():

            carta_1, carta_2=sorteador()

            print(f"- Nome: {carta_1['nome']}\n- Força: {carta_1['forca']}\n- Inteligencia: {carta_1['inteligencia']}\n- Influencia: {carta_1['influencia']}\n")

            comparar=str(input("Qual valor vai ser comparado:")).lower().strip()

            if carta_1['trunfo']==True:
                print("Jogador ganhou")
                print("Carta Trunfo")
                
            elif carta_2['trunfo']==True:
                print("PC ganhou")
                print("Carta Trunfo")

            elif comparar=="forca":
                if carta_1['forca'] > carta_2['forca']:
                    print("Jogador ganhou")
                
                elif carta_1['forca'] == carta_2['forca']:
                    print("Rodada empatada")
                
                else:
                    print("PC ganhou")
            
            elif comparar=="inteligencia":
                if carta_1['inteligencia'] > carta_2['inteligencia']:
                    print("Jogador ganhou")

                elif carta_1['inteligencia'] == carta_2['inteligencia']:
                    print("Rodada empatada")

                else:
                    print("PC ganhou")

            elif comparar=="influencia":
                if carta_1['influencia'] > carta_2['influencia']:
                    print("Jogador ganhou")
                
                elif carta_1['influencia'] == carta_2['influencia']:
                    print("Rodada empatada")

                else:
                    print("PC ganhou")
            else:
                print("\nValor invalido\n")
                print("Tente novamente!\n")
                return jogo_completo()



        jogo()

        carta_1, carta_2=sorteador()
        print("\nCartas do PC:")
        print(f"\n- Nome: {carta_2['nome']}\n- Força: {carta_2['forca']}\n- Inteligencia: {carta_2['inteligencia']}\n- Influencia: {carta_2['influencia']}\n")


        novamente=str(input("Se quiser jogar novamente digite 'sim':"))

        if novamente=="sim":
            jogo_completo()
        else:
            ("Jogatina encerada")
            break


jogo_completo()