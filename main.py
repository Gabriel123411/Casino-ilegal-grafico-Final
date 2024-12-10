from database import Database
from usuario import Usuario

def conectar_bd():
    db = Database()
    return db.conectar_bd()

def registrar_usuario(nombre, mail, password):
    db = Database()
    return Usuario.registrar_usuario(db, nombre, mail, password)

def iniciar_sesion(mail, password):
    db = Database()
    return Usuario.iniciar_sesion(db, mail, password)

def ingresar_dinero(usuario, monto):
    db = Database()
    return Usuario.ingresar_dinero(db, usuario, monto)

# Puedes mantener las funciones comentadas para menús si planeas usarlas en el futuro
# def menu_login():
#     while True:
#         print("1. Iniciar sesión")
#         print("2. Registrarse")
#         opcion = input("Seleccione una opción: ")
#         if opcion == '1':
#             usuario = iniciar_sesion()
#             if usuario:
#                 return usuario
#         elif opcion == '2':
#             registrar_usuario()
#         else:
#             print("Opción no válida. Intente nuevamente.")

# def menu_principal(usuario):
#     while True:
#         print(f"\nSaldo actual: ${usuario[4]}")
#         print("1. Ingresar dinero")
#         print("2. Elegir juego")
#         print("3. Salir")
#         opcion = input("Seleccione una opción: ")
#         if opcion == '1':
#             usuario = ingresar_dinero(usuario)
#         elif opcion == '2':
#             elegir_juego(usuario)
#         elif opcion == '3':
#             print("Gracias por jugar. ¡Hasta luego!")
#             break
#         else:
#             print("Opción no válida. Intente nuevamente.")

# def elegir_juego(usuario):
#     print("Seleccione un juego:")
#     print("1. Blackjack")
#     print("2. Poker")
#     print("3. Tragaperras")
#     print("4. Hipodromo")
#     print("5. Carrera de Buses")
#     opcion = input("Seleccione una opción: ")
#     if opcion == '1':
#         juego = Blackjack()
#     elif opcion == '2':
#         juego = Poker()
#     elif opcion == '3':
#         juego = Tragaperras()
#     elif opcion == '4':
#         juego = Hipodromo()
#     elif opcion == '5':
#         juego = CarreraBuses()
#     else:
#         print("Opción no válida. Intente nuevamente.")
#         return
#     usuario = juego.jugar(usuario)

if __name__ == "__main__":
    db = Database()
    db.crear_tablas()  # Crea las tablas al inicio
    # usuario = menu_login()
    # if usuario:
    #     menu_principal(usuario)