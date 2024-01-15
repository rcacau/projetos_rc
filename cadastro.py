import random 


def checar(nome):
    cont = 0
    for i in nome:
        if i.lower() in "qwertyuiopasdfghjklçzxcvbnm":
            cont += 1
    if len(nome) == cont:
        return nome
    else:
        return "erro, digite apenas letras no nome."


clientes = []

print("Se você desejar sair digite 'sair' no campo 'nome'")
cont = 0

while True:
    try:
        nome = str(input("Digite o nome: ")).upper().strip()
        resultado = checar(nome)
        if resultado == nome:
            if nome == "SAIR":
                break
            cpf = int(input("Digite o CPF (apenas números): "))
            valor = float(input("Digite o valor da compra: "))

            candidato = {
                "nome" : nome,
                "cpf" : cpf,
                "valor" : valor
            }
            clientes.append(candidato)
            print("Cliente Registrado!")
        else:
            print(resultado)

    except:
        print("Você preencheu um tipo de dado errado, tente novamente!")
        print("OBS: Digite apenas números no CPF e no Valor")
        continue           


campeão = random.choice(clientes)

print(f"""Parabéns {campeão["nome"]}, cpf: {campeão["cpf"]} você foi o sorteado por ter feito uma compra no valor de {campeão["valor"]}""")
