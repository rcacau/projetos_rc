alunos = {}

while True:
    opc = input("vc deseja add um alunos, remover um aluno, visualisar os alunos, atualizar um aluno ou fechar o sistema? [A, R, V, U, S]: ").lower()
    if opc in "a":
        ad = { input("digite a matricula do aluno: "): input("digite o nome do aluno: ")}
        alunos.update(ad)
    elif opc in "r":
        matricula = input("digite a matricula do aluno: ")
        alunos.pop(matricula)
    elif opc in "v":
        for i in alunos:
            print(alunos[i],i)
    elif opc in "u":
        matricula = input("digite a matricula do aluno: ")
        novoNome = input("digite o nome atualizado: ")
        alunos[matricula] = novoNome
    elif opc in "s":
        break   