import sqlite3
import re


class Database:
    def __init__(self, db_name='casino.db'):
        self.db_name = db_name

    def conectar_bd(self):
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            print(f"No ha sido posible conectarse con la base de datos: {e}")

    def crear_tablas(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Usuarios(
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    mail TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    saldo INTEGER NOT NULL DEFAULT 100,
                    fecha_registro TEXT DEFAULT CURRENT_TIMESTAMP)
                """)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Juegos(
                    id_juego INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_juego TEXT NOT NULL,
                    tipo_juego TEXT NOT NULL,
                    descripcion TEXT)
                """)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Historial_Juegos(
                    id_historial INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER,
                    id_juego INTEGER,
                    fecha_juego TEXT DEFAULT CURRENT_TIMESTAMP,
                    resultado TEXT,
                    apuesta REAL,
                    ganancia_perdida REAL,
                    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
                    FOREIGN KEY (id_juego) REFERENCES Juegos(id_juego))
                """)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Apuestas(
                    id_apuesta INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER,
                    id_juego INTEGER,
                    monto_apuesta REAL,
                    fecha_apuesta TEXT DEFAULT CURRENT_TIMESTAMP,
                    estado_apuesta TEXT,
                    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
                    FOREIGN KEY (id_juego) REFERENCES Juegos(id_juego))
                """)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Transacciones(
                    id_transaccion INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER,
                    tipo_transaccion TEXT,
                    monto REAL,
                    fecha_transaccion TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario))
                """)
                conn.commit()
                return "Las tablas fueron creadas exitosamente"
        except sqlite3.Error as e:
            return f"Error al crear tablas: {e}"