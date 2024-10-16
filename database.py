import sqlite3

def connect_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn, cursor

def close_db(conn):
    conn.close()
    
# Adicionar uma nova tarefa ao banco de dados
def add_task(title, description):
    conn, cursor = connect_db()
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, 'Pendente')", (title, description))
    conn.commit()
    close_db(conn)

# Obter todas as tarefas
def get_tasks():
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    close_db(conn)
    return tasks

# Atualizar o status de uma tarefa para 'Concluída'
def complete_task(task_id):
    conn, cursor = connect_db()
    cursor.execute("UPDATE tasks SET status = 'Concluída' WHERE id = ?", (task_id,))
    conn.commit()
    close_db(conn)

# Editar uma tarefa existente
def edit_task(task_id, title, description):
    conn, cursor = connect_db()
    cursor.execute("UPDATE tasks SET title = ?, description = ? WHERE id = ?", (title, description, task_id))
    conn.commit()
    close_db(conn)

# Excluir uma tarefa
def delete_task(task_id):
    conn, cursor = connect_db()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    close_db(conn)
