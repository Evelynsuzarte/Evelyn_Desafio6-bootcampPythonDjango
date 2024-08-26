
class Relatorios:
    def __init__(self, banco):
        self.banco = banco

    def _connect(self):
        return self.banco._connect()

    """LISTAR PRODUTOS EM ESTOQUE"""
    def listar_produtos_em_estoque(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM produto WHERE quantidade_disponivel > 0
        ''')
        
        return cursor.fetchall()

    def listar_produtos_em_estoque(self):
        produtos = self.banco.listar_produtos_em_estoque()
        for produto in produtos:
            print(produto)

    """VENDAS POR CLIENTE"""
    def listar_vendas_cliente(self, id_cliente):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT * FROM transacao WHERE id_cliente = ?
        ''', (id_cliente,))
        
        return cursor.fetchall()

    def listar_vendas_cliente(self, id_cliente):
        vendas_cliente = self.banco.listar_vendas_cliente(id_cliente)
        for venda in vendas_cliente:
            print(venda)

    """LISTAR TOTAL DE VENDAS POR CATEGORIA"""
    def listar_total_vendas_categoria(self):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT c.nome, t.valor_total FROM transacao t 
        INNER JOIN produto p ON t.id_produto = p.id_produto
        INNER JOIN  categoria c ON p.id_categoria = c.id_categoria
        ORDER BY t.valor_total DESC 
        ''')
        
        return cursor.fetchall()

    def listar_total_vendas_categoria(self):
        categorias = self.banco.listar_total_vendas_categoria()
        for categoria in categorias:
            print(categoria)

    """PRODUTOS MAIS VENDIDOS"""
    def listar_produtos_mais_vendidos(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT p.nome, SUM(t.valor_total) FROM transacao t 
        INNER JOIN produto p ON t.id_produto = p.id_produto 
        ORDER BY t.valor_total DESC''')

        return cursor.fetchall()

    def listar_produtos_mais_vendidos(self):
        produtos = self.banco.listar_produtos_mais_vendidos()
        for produto in produtos:
            print(produto)
    