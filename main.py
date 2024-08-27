import sqlite3
from relatorios.relatorios import Relatorios as rel
from transacao.transacao import Transacao
from cliente.operacoes_cliente import excluir_cliente

def conectar_ao_banco(nome_banco):
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
    #insert categorias
    cursor.execute('INSERT OR IGNORE INTO categoria (id_categoria, nome) VALUES (1, "Perifericos")')
    cursor.execute('INSERT OR IGNORE INTO categoria (id_categoria, nome) VALUES (2, "Eletronicos")')
    cursor.execute('INSERT OR IGNORE INTO categoria (id_categoria, nome) VALUES (3, "Cabos e Adaptadores")')
    cursor.execute('INSERT OR IGNORE INTO categoria (id_categoria, nome) VALUES (4, "Armazenamento")')
    
    #insert fornecedores
    cursor.execute('INSERT OR IGNORE INTO fornecedor (id_fornecedor, nome) VALUES (1, "Razer")')
    cursor.execute('INSERT OR IGNORE INTO fornecedor (id_fornecedor, nome) VALUES (2, "Logitech")')
    cursor.execute('INSERT OR IGNORE INTO fornecedor (id_fornecedor, nome) VALUES (3, "Samsung")')
    cursor.execute('INSERT OR IGNORE INTO fornecedor (id_fornecedor, nome) VALUES (4, "Dell")')
    cursor.execute('INSERT OR IGNORE INTO fornecedor (id_fornecedor, nome) VALUES (5, "HP")')
    
    #insert produtos
    cursor.execute('INSERT OR IGNORE INTO produto (id_produto, nome, qtnd_disponivel, preco, id_categoria, id_fornecedor) VALUES (1,"Teclado Gamer", 20, 120.10, 1, 1)')
    cursor.execute('INSERT OR IGNORE INTO produto (id_produto, nome, qtnd_disponivel, preco, id_categoria, id_fornecedor) VALUES (2,"Mouse Gamer", 30, 80.50, 1, 2)')
    cursor.execute('INSERT OR IGNORE INTO produto (id_produto, nome, qtnd_disponivel, preco, id_categoria, id_fornecedor) VALUES (3,"Monitor", 30, 800.50, 2, 1)')
    cursor.execute('INSERT OR IGNORE INTO produto (id_produto, nome, qtnd_disponivel, preco, id_categoria, id_fornecedor) VALUES (4,"HD Externo", 40, 300.00, 4, 3)')
    cursor.execute('INSERT OR IGNORE INTO produto (id_produto, nome, qtnd_disponivel, preco, id_categoria, id_fornecedor) VALUES (5,"SSD", 50, 400.00, 4, 4)')
    cursor.execute('INSERT OR IGNORE INTO produto (id_produto, nome, qtnd_disponivel, preco, id_categoria, id_fornecedor) VALUES (6,"Cabo HDMI", 60, 20.00, 3, 5)')
    cursor.execute('INSERT OR IGNORE INTO produto (id_produto, nome, qtnd_disponivel, preco, id_categoria, id_fornecedor) VALUES (7,"Adaptador USB", 70, 10.00, 3, 5)')
    cursor.execute('INSERT OR IGNORE INTO produto (id_produto, nome, qtnd_disponivel, preco, id_categoria, id_fornecedor) VALUES (8,"Pen Drive", 80, 30.00, 4, 4)')
    
    #insert clientes
    cursor.execute('INSERT OR IGNORE INTO cliente (id_cliente, nome, telefone, endereco) VALUES (1, "João", "47997505577","Rua das Flores, 123")')
    cursor.execute('INSERT OR IGNORE INTO cliente (id_cliente, nome, telefone,endereco) VALUES (2, "Maria", "47997505577","Rua das Árvores, 321")')
    cursor.execute('INSERT OR IGNORE INTO cliente (id_cliente, nome, telefone,endereco) VALUES (3, "Fernanda", "47997505588","Rua das Plantas, 864")')
    cursor.execute('INSERT OR IGNORE INTO cliente (id_cliente, nome, telefone,endereco) VALUES (4, "Cláudia", "47997505599","Rua das Pedras, 522")')
    cursor.execute('INSERT OR IGNORE INTO cliente (id_cliente, nome, telefone,endereco) VALUES (5, "Lucas", "47997505500","Avenida Santos, 117")')
                          
    conexao.commit()

def main():
    # Nome do banco de dados SQLite 
    nome_banco = 'mercado.db'
    
    # Conectando ao banco de dados
    conn = conectar_ao_banco(nome_banco)

    # Diretórios onde estão os scripts SQL  
    categoria_sql = 'categoria/categoria.sql'
    fornecedor_sql = 'fornecedor/fornecedor.sql'
    cliente_sql = 'cliente/cliente.sql'
    produto_sql = 'produto/produto.sql'
    transacao_sql = 'transacao/transacao.sql'

    # Executando scripts SQL
    executar_sql_script(conn, categoria_sql)
    executar_sql_script(conn, fornecedor_sql)
    executar_sql_script(conn, cliente_sql)
    executar_sql_script(conn, produto_sql)
    executar_sql_script(conn, transacao_sql)
    insert_tabelas(conn)
    
    transacao =  Transacao(conn)
    """Realizar transação: Ordem dos parâmetros: id_transacao, quantidade, id_cliente, id_produto"""
    # transacao.realizar_transacao(6, 2, 4, 8)
    
    relatorios = rel(conn)
    print("- - - PRODUTOS EM ESTOQUE - - -")
    relatorios.listar_produtos_em_estoque()
    print()
    
    print("- - - VENDAS POR CLIENTE - - -")
    for cliente in conn.execute('SELECT id_cliente, nome FROM cliente'):
        print(f'Cliente: {cliente[1]}')
        relatorios.listar_vendas_cliente(cliente[0])       
    print()
    
    print("- - - VENDAS POR CATEGORIA - - -")
    relatorios.listar_total_vendas_categoria()
    print()
    
    print("- - - PRODUTOS MAIS VENDIDOS - - -")
    relatorios.listar_produtos_mais_vendidos()
    print()
    
    print("- - - EXLCUIR CLIENTE - - -")
    #excluindo cliente
    excluir_cliente(conn, 3)

    # Fechando a conexão
    conn.close()

if __name__ == "__main__":
    main()
