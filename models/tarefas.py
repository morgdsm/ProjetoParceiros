import sqlite3
from datetime import datetime

# Função para conectar ao banco
def conectar_db():
    return sqlite3.connect('data/banco.db')


# Adicionar nova tarefa
def adicionar_tarefa(descricao, status, prazo, parceiro_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tarefas (descricao, status, prazo, parceiro_id)
        VALUES (?, ?, ?, ?)
    """, (descricao, status, prazo, parceiro_id))
    conn.commit()
    conn.close()


# Listar todas as tarefas
def listar_tarefas():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.id, t.descricao, t.status, t.prazo, p.nome
        FROM tarefas t
        JOIN parceiros p ON t.parceiro_id = p.id
        ORDER BY t.prazo ASC
    """)
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas


# Atualizar o status de uma tarefa
def atualizar_status_tarefa(tarefa_id, novo_status):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tarefas SET status = ?
        WHERE id = ?
    """, (novo_status, tarefa_id))
    conn.commit()
    conn.close()


# Deletar uma tarefa
def deletar_tarefa(tarefa_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    conn.commit()
    conn.close()


# Gerar dados para o dashboard
def contar_tarefas_por_status():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT status, COUNT(*) FROM tarefas
        GROUP BY status
    """)
    resultado = cursor.fetchall()
    conn.close()
    return resultado
