import bcrypt
import sqlite3
import re

class Usuario:
    def __init__(self, nombre, mail, password, saldo=100):
        self.nombre = nombre
        self.mail = mail
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.saldo = saldo

    @staticmethod
    def validar_mail(mail):
        return re.match(r"[^@]+@[^@]+\.[^@]+", mail)

    @staticmethod
    def validar_password(password):
        return len(password) >= 8

    @classmethod
    def registrar_usuario(cls, db, nombre, mail, password):
        if not cls.validar_mail(mail):
            return "Correo electrónico no válido"
        if not cls.validar_password(password):
            return "La contraseña debe tener al menos 8 caracteres"
        
        conn = db.conectar_bd()
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            cursor.execute("INSERT INTO Usuarios (nombre, mail, password) VALUES (?, ?, ?)", (nombre, mail, hashed_password))
            conn.commit()
            return "Registro exitoso"
        except sqlite3.IntegrityError:
            return "El correo electrónico ya está registrado"

    @classmethod
    def iniciar_sesion(cls, db, mail, password):
        if not cls.validar_mail(mail):
            return None
        
        conn = db.conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE mail = ?", (mail,))
        usuario = cursor.fetchone()
        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario[3]):
            return usuario
        return None

    @staticmethod
    def ingresar_dinero(db, usuario, monto):
        if monto > 0:
            conn = db.conectar_bd()
            cursor = conn.cursor()
            cursor.execute("UPDATE Usuarios SET saldo = saldo + ? WHERE id_usuario = ?", (monto, usuario[0]))
            conn.commit()
            usuario = (usuario[0], usuario[1], usuario[2], usuario[3], usuario[4] + monto, usuario[5])
            return usuario
        return None