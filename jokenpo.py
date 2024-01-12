import random

cont1 = 0
cont2 = 0

def checar_vitoria(sorteio, escolha):
    global cont1
    global cont2
    if sorteio == escolha:   
        return "EMPATE"
    elif (escolha == "pedra" and sorteio == "tesoura") or (escolha == "tesoura" and sorteio == "papel") or (escolha == "papel" and sorteio == "pedra"):
        cont1 = cont1 + 1
        return "VITÓRIA"
    else:
        cont2 = cont2 + 1
        return "DERROTA"

opçoes = ["pedra", "papel", "tesoura"]
print("O JOGO COMEÇOU")


while True:
    sorteio = random.choice(opçoes)
    print("---- PLACAR -----")
    print(f"     {cont1} X {cont2}")
    while True:
        escolha = input("escolha: [papel/pedra/tesoura] -> ").lower()
        if escolha in ["pedra", "papel", "tesoura"]:
            break

    print(f"o maquina escolhou {sorteio}")
    resultado = checar_vitoria(sorteio, escolha)
    print(resultado)
    
    while True:
        continuar = input("você deseja jogar novamente: [s / n] -> ").lower()
        print("")
        if continuar in ["s", "n"]:
            break
    if continuar in "n":
        print("---- PLACAR FINAL -----")
        print(f"        {cont1} X {cont2}")
        if cont1 > cont2:
            print("PARABÉNS, VOCÊ GANHOU")
        break
