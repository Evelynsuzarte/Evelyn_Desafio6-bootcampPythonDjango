CREATE TABLE IF NOT EXISTS produto (
    id_produto INT PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR (100),
    qtnd_disponivel INT,
    preco FLOAT,
    id_categoria INT,
    id_fornecedor INT,
    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor (id_fornecedor),
    FOREIGN KEY (id_categoria) REFERENCES Categoria (id_categoria)

);