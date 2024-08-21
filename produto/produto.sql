CREATE TABLE Produto (
    id_produto INT PRIMARY KEY,
    nome VARCHAR (100),
    qtnd_disponivel INT,
    preco FLOAT,
    id_categoria INT,
    id_fornecedor INT,
    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor (id_fornecedor),
    FOREIGN KEY (id_categoria) REFERENCES Categoria (id_categoria)

);