import sqlite3

# Função para conectar ao banco
def conectar_db():
    return sqlite3.connect('data/banco.db')


# Adicionar novo parceiro
def adicionar_parceiro(nome, email, telefone):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO parceiros (nome, email, telefone)
        VALUES (?, ?, ?)
    """, (nome, email, telefone))
    conn.commit()
    conn.close()


# Listar todos os parceiros
def listar_parceiros():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nome, email, telefone
        FROM parceiros
        ORDER BY nome
    """)
    parceiros = cursor.fetchall()
    conn.close()
    return parceiros


# Editar parceiro
def editar_parceiro(parceiro_id, nome, email, telefone):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE parceiros
        SET nome = ?, email = ?, telefone = ?
        WHERE id = ?
    """, (nome, email, telefone, parceiro_id))
    conn.commit()
    conn.close()


# Deletar parceiro
def deletar_parceiro(parceiro_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM parceiros WHERE id = ?", (parceiro_id,))
    conn.commit()
    conn.close()
