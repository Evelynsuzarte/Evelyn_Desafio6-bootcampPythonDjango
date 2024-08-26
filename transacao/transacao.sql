CREATE TABLE IF NOT EXISTS transacao (
    id_transacao INT PRIMARY KEY,
    qtnd_produto INT, 
    valor_total FLOAT,
    data_transacao DATE,
    id_cliente INT,
    id_produto INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente),
    FOREIGN KEY (id_produto) REFERENCES Produto (id_produto)
);