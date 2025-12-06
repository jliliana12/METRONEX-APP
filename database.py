import sqlite3

DB_NAME = "equipos.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS equipos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            serie TEXT,
            estado TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def create_equipo(nombre, serie, estado):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO equipos(nombre, serie, estado) VALUES (?, ?, ?)",
        (nombre, serie, estado)
    )
    conn.commit()
    return cur.lastrowid

def get_equipo(id_equipo):
    conn = get_db()
    res = conn.execute("SELECT * FROM equipos WHERE id=?", (id_equipo,)).fetchone()
    return dict(res) if res else None

def get_all():
    conn = get_db()
    rows = conn.execute("SELECT * FROM equipos").fetchall()
    return [dict(r) for r in rows]

def update_estado(id_equipo, estado):
    conn = get_db()
    conn.execute("UPDATE equipos SET estado=? WHERE id=?", (estado, id_equipo))
    conn.commit()
