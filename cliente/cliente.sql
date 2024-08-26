CREATE TABLE
    IF NOT EXISTS cliente (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        telefone VARCHAR(20),
        endereco VARCHAR(100)
    );