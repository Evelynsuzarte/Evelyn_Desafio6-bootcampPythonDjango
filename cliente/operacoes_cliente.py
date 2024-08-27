def excluir_cliente(conn, id_cliente):
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM cliente WHERE id_cliente = ?', (id_cliente,))
        conn.commit()
        print(f"Cliente com id {id_cliente} excluído com sucesso.")
    except Exception as e:
        print(f"Erro ao excluir cliente: {e}")
    finally:
        cursor.close()

