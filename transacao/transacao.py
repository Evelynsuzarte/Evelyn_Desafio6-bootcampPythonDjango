from datetime import datetime

class Transacao():
    def __init__(self, banco):
        self.banco = banco

    def _connect(self):
        return self.banco
    
    def realizar_transacao(self, id_transacao, quantidade, id_cliente, id_produto):
        conn = self._connect()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT preco FROM produto WHERE id_produto = ?
        ''', (id_produto,))
        
        preco = cursor.fetchone()[0]
        
        valor_total = preco * quantidade
        
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute('''
        INSERT INTO transacao (id_transacao, qtnd_produto, valor_total, data_transacao, id_cliente, id_produto) VALUES (?, ?, ?, ?, ?, ?)
        ''', (id_transacao, quantidade, valor_total, data, id_cliente, id_produto))
        
        cursor.execute('''
        UPDATE produto SET qtnd_disponivel = qtnd_disponivel - ? WHERE id_produto = ?
        ''', (quantidade, id_produto))
        
        conn.commit()