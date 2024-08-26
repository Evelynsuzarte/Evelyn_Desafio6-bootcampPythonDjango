class Relatorios:
    def __init__(self, banco):
        self.banco = banco

    def _connect(self):
        return self.banco

    """LISTAR PRODUTOS EM ESTOQUE"""
    def listar_produtos_em_estoque(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM produto WHERE qtnd_disponivel > 0
        ''')
        
        produtos = cursor.fetchall()
        for produto in produtos:
            print(produto)

    """VENDAS POR CLIENTE"""
    def listar_vendas_cliente(self, id_cliente):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM transacao WHERE id_cliente = ?
        ''', (id_cliente,))
        
        vendas_cliente = cursor.fetchall()
        for venda in vendas_cliente:
            print(venda)

    """LISTAR TOTAL DE VENDAS POR CATEGORIA"""
    def listar_total_vendas_categoria(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT c.nome, SUM(t.valor_total) AS total_vendas 
        FROM transacao t 
        INNER JOIN produto p ON t.id_produto = p.id_produto
        INNER JOIN categoria c ON p.id_categoria = c.id_categoria
        GROUP BY c.nome
        ORDER BY total_vendas DESC
        ''')
        
        categorias = cursor.fetchall()
        for categoria in categorias:
            print(categoria)

    """PRODUTOS MAIS VENDIDOS""" 
    def listar_produtos_mais_vendidos(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT p.nome, SUM(t.valor_total) AS total_vendas 
        FROM transacao t 
        INNER JOIN produto p ON t.id_produto = p.id_produto 
        GROUP BY p.nome
        ORDER BY total_vendas DESC
        ''')
        
        produtos = cursor.fetchall()
        for produto in produtos:
            print(produto)
