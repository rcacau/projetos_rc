contador_id_m = 1
contador_id_l = 1


class Livro:
    def __init__(self, titulo:str, autor:str, id: str):
        self.__titulo = titulo
        self.__autor = autor
        self.__id = id
        self.__disponibilidade = True

    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, novo_titulo):
        self._titulo = novo_titulo

    def getAutor(self):
        return self.__autor
    
    def setAutor(self, novo_autor):
        self.__autor = novo_autor

    def getDisponibilidade(self):
        return self.__disponibilidade
    
    def setDisponibilidade(self, status):
        self.__disponibilidade = status

    def getIdL(self):
        return self.__id

    def setIdL(self, novo_id):
        self._titulo = novo_id



class Membro:
    def __init__(self, nome:str, id:str):
        self.__nome = nome
        self.__id = id
        self.historico = []

    def getNome(self):
        return self.__nome
    
    def setNome(self, novo_nome):
        self.__nome = novo_nome

    def getIdM(self):
        return self.__id
    
    def setIdM(self, novo_id):
        self._id = novo_id


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.membros = []

    def addLivro(self):
        global contador_id_l
        titulo = input("Digite o titulo do livro:")
        autor = input("Digite o nome do autor: ")
        livro1 = Livro(titulo, autor, contador_id_l)
        self.livros.append(livro1)
        contador_id_l += 1

    def removerLivro(self):
        livro_remover = input("Digite o titulo do livro que vc deseja remover: ")
        for livro in self.livros:
            if livro.getTitulo() == livro_remover:
                self.livros.remove(livro)
            else:
                print("Livro não encontrado.")

    def addMembro(self):
        global contador_id_m
        nome = input("Digite o nome do membro: ")
        membro1 = Membro(nome, contador_id_m)
        self.membros.append(membro1)
        contador_id_m += 1

    def removerMembro(self):
        membro_remover = input("Digite o nome do membro que vc deseja remover: ")
        for membro in self.membros:
            if membro.getNome() == membro_remover:
                self.livros.remove(membro)
            else:
                print("Livro não encontrado.")

    def pesquisar(self):
        id = input("Digite o ID do livro que vc deseja procurar: ")
        for livro in self.livros:
            if livro.getId() == int(id):
                print("Livro encontrado com sucesso.") 
            else:
                print("Livro nao encontrado.")


    def emprestimo(self):
        id = input("Digite o ID do livro q vc deseja: ")
        for livro in self.livros:
            if livro.getIdL() == int(id):
                if livro.getDisponibilidade() == True:
                    livro.setDisponibilidade(False)
                    id_membro = input("Digite o id do membro: ")
                    for membro in self.membros:
                        if membro.getIdM() == int(id_membro):
                            membro.historico.append(livro)
                            print("Livro emprestado com sucesso.")
                        else:
                            print("Membro não encontrado.")
                else:
                    print("Livro indisponivel.")
            else: 
                print("Livro não encontrado.")


    def devolver(self):
        id_membro = input("Digite o ID do membro: ")
        for membro in self.membros:
            if membro.getIdM() == int(id_membro):
                id = input("Digite o ID do livro q vc deseja devolver: ")
                for livro in self.livros:
                    if livro.getIdL() == int(id):
                        if livro.getDisponibilidade() == False:
                            livro.setDisponibilidade(True)
                            print("Livro devolvido com sucesso.")
                        else:
                            print("O livro ja foi devolvido.")
                    else:
                        print("Livro nao encontrado.")
            else:
                print("Membro nao encontrado.")



biblioteca1 = Biblioteca()

while True:
    menu = int(input("""
    1 - Add livro
    2 - Remover livro
    3 - Add membro
    4 - Remover membro
    5 - Pesquisar livro
    6 - Pegar emprestimo de livro
    7 - Devolver livro
    0 - Sair
    
    Digite aqui: """))

    match menu:
        case 1:
            biblioteca1.addLivro()
        case 2:
            biblioteca1.removerLivro()
        case 3:
            biblioteca1.addMembro()
        case 4:
            biblioteca1.removerMembro()
        case 5:
            biblioteca1.pesquisar()
        case 6:
            biblioteca1.emprestimo()
        case 7:
            biblioteca1.devolver()
        case 0:
            break
        case _:
            print("Opção invalida.  ")