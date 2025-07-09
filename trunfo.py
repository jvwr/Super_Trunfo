import json
import random
from InquirerPy import prompt
from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

rodada = 1

jogador = 0

pc = 0

baralho = "baralho.json"
partida = "partida.txt"

with open(partida, "w", encoding="utf-8") as file:
    pass


print("Seja bem-vindo ao Super Trunfo!")
print("Pegue sua carta, escolha com sabedoria... ou só confie no seu bom azar mesmo.\n")

print("Super Trunfo é um jogo de cartas em que cada carta possui três atributos: Força, Inteligência e Influência.")
print("Você jogará contra o computador. A cada rodada, você recebe uma carta e escolhe um dos atributos para comparar com a carta do PC.")
print("Quem tiver o maior valor no atributo escolhido vence a rodada.")
print("Se uma das cartas for uma Carta Trunfo, ela vence automaticamente.")
print("Em caso de empate, uma nova rodada de desempate é iniciada.")


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

        print("\n=== CARTA DO PC ===")
        print(f"- Nome: {carta_2['Nome']}\n- Força: {carta_2['Força']}\n- Inteligência: {carta_2['Inteligência']}\n- Influência: {carta_2['Influência']}\n")

        return carta_1, carta_2, vencedor, resultado

    elif carta_2['Trunfo'] is True:
        print(Fore.RED + Style.BRIGHT + "PC ganhou!")
        print("Carta Trunfo")
        vencedor = "PC ganhou!"
        pc += 1

        print("\n=== CARTA DO PC ===")
        print(f"- Nome: {carta_2['Nome']}\n- Força: {carta_2['Força']}\n- Inteligência: {carta_2['Inteligência']}\n- Influência: {carta_2['Influência']}\n")

        return carta_1, carta_2, vencedor, resultado

    if carta_1[resultado] > carta_2[resultado]:
        print(Fore.RED + Style.BRIGHT + "\nJogador ganhou!")
        vencedor = "Jogador ganhou!"
        jogador += 1

    elif carta_1[resultado] == carta_2[resultado]:
        print(Fore.RED + Style.BRIGHT + "\nEmpate!")
        print("\nNova Rodada de Desempate")

        vencedor = "Empate!"
        historico(carta_1, carta_2, vencedor, resultado)

        global rodada
        rodada += 1

        carta_1, carta_2, vencedor, resultado = empate()
        historico(carta_1, carta_2, vencedor, resultado)

        rodada += 1

    else:
        print(Fore.RED + Style.BRIGHT + "\nPC ganhou!")
        vencedor = "PC ganhou!"
        pc += 1

    print("\n=== CARTA DO PC ===")
    print(f"- Nome: {carta_2['Nome']}\n- Força: {carta_2['Força']}\n- Inteligência: {carta_2['Inteligência']}\n- Influência: {carta_2['Influência']}\n")

    return carta_1, carta_2, vencedor, resultado


def comeco_hora(comeco):

    with open(partida, "a", encoding="utf-8") as file:

        file.write(f"O jogo começou no dia {comeco.strftime('%d/%m/%Y')} as {comeco.strftime('%H:%M:%S')} \n\n")


def historico(carta_1, carta_2, vencedor, resultado):

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

        rodadas.write(f"Atributo escolhido {resultado}\n\n")

        rodadas.write(f"RESULTADO DA RODADA {rodada}")
        rodadas.write(f"\n{vencedor}\n\n\n\n")


def resultado_final(final):

    global jogador
    global pc

    with open(partida, "a", encoding="utf-8") as rodadas:
        rodadas.write("Quantidade de rodadas ganham pelo:\n")
        rodadas.write(f"Jogador ganhou {jogador} \n")
        rodadas.write(f"PC ganhou {pc} ")

        if pc > jogador:
            rodadas.write("\nPC ganhou essa partida de Super Trunfo! \n\n\n")
        else:
            rodadas.write("\nJogador ganhou essa partida de Super Trunfo! \n\n\n")

        rodadas.write(f"O jogo terminou no dia {final.strftime('%d/%m/%Y')} as {final.strftime('%H:%M:%S')} ")


def empate():

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
        jogador += 2

        print("\n=== CARTA DO PC ===")
        print(f"- Nome: {carta_2['Nome']}\n- Força: {carta_2['Força']}\n- Inteligência: {carta_2['Inteligência']}\n- Influência: {carta_2['Influência']}\n")

        return carta_1, carta_2, vencedor, resultado

    elif carta_2['Trunfo'] is True:
        print(Fore.RED + Style.BRIGHT + "PC ganhou!")
        print("Carta Trunfo")
        vencedor = "PC ganhou!"
        pc += 2

        print("\n=== CARTA DO PC ===")
        print(f"- Nome: {carta_2['Nome']}\n- Força: {carta_2['Força']}\n- Inteligência: {carta_2['Inteligência']}\n- Influência: {carta_2['Influência']}\n")

        return carta_1, carta_2, vencedor, resultado

    if carta_1[resultado] > carta_2[resultado]:
        print(Fore.RED + Style.BRIGHT + "\nJogador ganhou!")
        vencedor = "Jogador ganhou!"
        jogador += 2

    elif carta_1[resultado] == carta_2[resultado]:
        print(Fore.RED + Style.BRIGHT + "\nEmpate!")
        print("\nNova Rodada")
        vencedor = "Empate!"
        return empate()

    else:
        print(Fore.RED + Style.BRIGHT + "\nPC ganhou!")
        vencedor = "PC ganhou!"
        pc += 2

    print("\n=== CARTA DO PC ===")
    print(f"- Nome: {carta_2['Nome']}\n- Força: {carta_2['Força']}\n- Inteligência: {carta_2['Inteligência']}\n- Influência: {carta_2['Influência']}\n")

    return carta_1, carta_2, vencedor, resultado


def main():

    comeco = datetime.now()
    comeco_hora(comeco)

    while True:

        resultado = jogo()

        if resultado is False:
            continue

        global rodada

        carta_1, carta_2, vencedor, resultado = resultado
        historico(carta_1, carta_2, vencedor, resultado)

        rodada += 1

        novamente = [
            {
                "type": "list",
                "name": "continuar",
                "message": "Deseja jogar mais uma rodada? ",
                "choices": ['Sim', 'Não']
            }
        ]

        decisao = prompt(novamente)["continuar"]

        if decisao == "Não":
            print("Jogatina encerrada")
            final = datetime.now()
            resultado_final(final)
            break


if __name__ == "__main__":
    main()
