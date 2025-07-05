import json
import random
from InquirerPy import prompt
from colorama import init, Fore, Style

init(autoreset=True)

rodada = 1

jogador = 0

pc = 0

with open(r"C:\Users\João Vitor\Desktop\Python\Super_Trunfo\partida.txt", "w", encoding="utf-8") as file:
    pass

baralho = r"C:\Users\João Vitor\Desktop\Python\Super_Trunfo\baralho.json"

partida = r"C:\Users\João Vitor\Desktop\Python\Super_Trunfo\partida.txt"

print("Bom dia, boa tarde, boa noite!!!\nApresento a vocês o jogo Super Trunfo.\n")

print("Super Trunfo é um jogo de cartas em que cada carta tem vários atributos. Na sua vez, o jogador escolhe um atributo da carta do topo do seu monte, e todos os jogadores comparam esse valor. Quem tiver o maior, vence a rodada e pega as cartas.")


def sorteador():

    with open(baralho, "r", encoding="utf-8") as file:
        cartas = json.load(file)

    while True:
        carta_1 = random.choice(cartas)

        carta_2 = random.choice(cartas)

        if carta_1 != carta_2:
            return carta_1, carta_2


def jogo():

    global jogador
    global pc

    carta_1, carta_2 = sorteador()

    print("\n\n=== CARTA DO JOGADOR ===")
    print(f"- Nome: {carta_1['Nome']}\n- Força: {carta_1['Força']}\n- Inteligência: {carta_1['Inteligência']}\n- Influência: {carta_1['Influência']}\n")

    comparar = [
        {
            "type": "list",
            "name": "atributo",
            "message": "Qual valor vai ser comparado: ",
            "choices": ['Força', 'Inteligência', 'Influência']
        }
    ]

    resultado = prompt(comparar)["atributo"]

    if carta_1['Trunfo'] is True:
        print(Fore.RED + Style.BRIGHT + "Jogador ganhou!")
        print("Carta Trunfo")
        vencedor = "Jogador ganhou!"
        jogador += 1

    elif carta_2['Trunfo'] is True:
        print(Fore.RED + Style.BRIGHT + "PC ganhou!")
        print("Carta Trunfo")
        vencedor = "PC ganhou!"
        pc += 1

    if resultado not in ['Força', 'Inteligência', 'Influência']:
        print("\nValor invalido!")
        return False

    if carta_1[resultado] > carta_2[resultado]:
        print(Fore.RED + Style.BRIGHT + "\nJogador ganhou!")
        vencedor = "Jogador ganhou!"
        jogador += 1

    elif carta_1[resultado] == carta_2[resultado]:
        print(Fore.RED + Style.BRIGHT + "\nEmpate!")
        print("\nNova Rodada")
        vencedor = "Empate!"

    else:
        print(Fore.RED + Style.BRIGHT + "\nPC ganhou!")
        vencedor = "PC ganhou!"
        pc += 1

        print("\nCartas do PC:")

    print("\n=== CARTA DO PC ===")
    print(f"- Nome: {carta_2['Nome']}\n- Força: {carta_2['Força']}\n- Inteligência: {carta_2['Inteligência']}\n- Influência: {carta_2['Influência']}\n")

    return carta_1, carta_2, vencedor


def historico(carta_1, carta_2, vencedor):

    with open(partida, "a", encoding="utf-8") as rodadas:

        rodadas.write(f"=== CARTA DO JOGADOR NA RODADA {rodada} ===\n")
        rodadas.write(f"Nome: {carta_1['Nome']}\n")
        rodadas.write(f"Força: {carta_1['Força']}\n")
        rodadas.write(f"Inteligência: {carta_1['Inteligência']}\n")
        rodadas.write(f"Influência: {carta_1['Influência']}\n\n")

        rodadas.write(f"=== CARTA DO PC NA RODADA {rodada} ===\n")
        rodadas.write(f"Nome: {carta_2['Nome']}\n")
        rodadas.write(f"Força: {carta_2['Força']}\n")
        rodadas.write(f"Inteligência: {carta_2['Inteligência']}\n")
        rodadas.write(f"Influência: {carta_2['Influência']}\n\n")

        rodadas.write(f"RESULTADO DA RODADA {rodada}")
        rodadas.write(f"\n{vencedor}\n\n\n\n")


def resultado_final():

    global jogador
    global pc

    with open(partida, "a", encoding="utf-8") as rodadas:
        rodadas.write("Quantidade de rodadas ganham pelo:\n")
        rodadas.write(f"Jogador ganhou {jogador} \n")
        rodadas.write(f"PC ganhou {pc} ")

        if pc > jogador:
            rodadas.write("\nPC ganhou essa partida de Super Trunfo! ")
        else:
            rodadas.write("\nJogador ganhou essa partida de Super Trunfo! ")


def main():

    while True:

        resultado = jogo()

        if resultado is False:
            continue

        carta_1, carta_2, vencedor = resultado
        historico(carta_1, carta_2, vencedor)

        global rodada
        rodada += 1

        novamente = [
            {
                "type": "list",
                "name": "atributo",
                "message": "Querer jogar mais uma rodada? ",
                "choices": ['Sim', 'Não']
            }
        ]

        decisao = prompt(novamente)["atributo"]

        if decisao == "Não":
            print("Jogatina encerada")
            resultado_final()
            break


if __name__ == "__main__":
    main()
