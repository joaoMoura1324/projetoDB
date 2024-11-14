import sqlite3

# Conexão com a base de dados 'biblioteca.db'
conexao = sqlite3.connect('biblioteca.db')

# Criação de um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar a tabela para armazenar livros
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER NOT NULL
)
''')


# Função para inserir um novo livro
def inserir_livro(titulo, autor, ano_publicacao):
    cursor.execute('''
    INSERT INTO livros (titulo, autor, ano_publicacao)
    VALUES (?, ?, ?)
    ''', (titulo, autor, ano_publicacao))
    conexao.commit()


# Função para atualizar as informações de um livro
def atualizar_livro(id_livro, novo_titulo=None, novo_autor=None, novo_ano_publicacao=None):
    if novo_titulo:
        cursor.execute('''
        UPDATE livros
        SET titulo = ?
        WHERE id = ?
        ''', (novo_titulo, id_livro))

    if novo_autor:
        cursor.execute('''
        UPDATE livros
        SET autor = ?
        WHERE id = ?
        ''', (novo_autor, id_livro))

    if novo_ano_publicacao:
        cursor.execute('''
        UPDATE livros
        SET ano_publicacao = ?
        WHERE id = ?
        ''', (novo_ano_publicacao, id_livro))

    conexao.commit()


# Função para consultar todos os livros
def consultar_livros():
    cursor.execute('SELECT * FROM livros')
    return cursor.fetchall()


# Inserir alguns livros na tabela
inserir_livro('1984', 'George Orwell', 1949)
inserir_livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)

# Atualizar um livro
atualizar_livro(1, novo_titulo='1984 (Edição Atualizada)')

# Consultar todos os livros
livros = consultar_livros()
for livro in livros:
    print(f'ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano de Publicação: {livro[3]}')

# Fechar a conexão com a base de dados
conexao.close()