import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Mysql102030",
    "database": "locadora"
}

def consultar_banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    lista_de_filmes = cursor.fetchall()
    cursor.close()
    conexao.close()
    return lista_de_filmes

def bulir_banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()
    cursor.close()
    conexao.close()




while True:
    menu = int(input("""
    escolha uma opção 
    1 - Add novo filme
    2 - Ver todos os filmes
    3 - Editar filme
    4 - Deletar filme 
    0 - Sair
"""))
    
    match menu:
        case 1:
            titulo_flime = input("Digite o nome do filme: ")
            genero_flime = input("Digite o genero do filme: ")
            ano_flime = input("Digite o ano do fime: ")
            bulir_banco(f"INSERT INTO filmes (titulo, genero, ano_lanc) VALUES ('{titulo_flime}', '{genero_flime}', {ano_flime})")
        case 2:
            print(consultar_banco("SELECT * FROM filmes"))
        case 3:
            id_filme = int(input("Digite o id do filme que vc deseja alterar: "))
            novo_titulo_flime = input("Digite o nome novo do filme: ")
            novo_genero_flime = input("Digite o genero novo do filme: ")
            novo_ano_flime = input("Digite o ano novo do fime: ")
            query = f"""
            UPDATE filmes SET titulo = '{novo_titulo_flime}', genero = '{novo_genero_flime}', ano_lanc = {novo_ano_flime} WHERE id = {id_filme} 
            """
            bulir_banco(query)
        case 4:
            id_filme = int(input("Digite o id do filme que vc deseja deletar: "))
            query = f"DELETE FROM filmes WHERE id = {id_filme}"
            bulir_banco(query)
        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção invalida")