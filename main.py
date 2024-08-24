import sqlite3
import os

def connectar_ao_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

def executar_sql_script(conexao, caminho_sql):
    with open(caminho_sql, 'r') as file:
        sql_script = file.read()
            
    cursor = conexao.cursor()
    cursor.executescript(sql_script)
    conexao.commit()

def insert_tabelas (conexao):
    cursor = conexao.cursor()
    #insert produtos
    #cursor.execute('INSERT INTO alunos (ID,nome, idade, curso) VALUES (1,"Raquel Morais", 19, "Nutrição")')        #continuar


    conexao.commit()

def main():
    # Nome do banco de dados SQLite 
    nome_banco = 'mercado.db'
    
    # Conectando ao banco de dados
    conn = connectar_ao_banco(nome_banco)

    # Diretórios onde estão os scripts SQL  
    produto_sql = 'produto/produto.sql'
    transacao_sql = 'transacao/transacao.sql'
    
    # Executando scripts SQL
    executar_sql_script(conn, produto_sql)
    executar_sql_script(conn, transacao_sql)
    insert_tabelas(conn)


    # Fechando a conexão
    conn.close()

if __name__ == "__main__":
    main()
