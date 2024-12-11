from flask import Flask, render_template, request, redirect, url_for, session
from database import Database
from usuario import Usuario

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave secreta segura

db = Database()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mail = request.form['email']
        password = request.form['password']
        usuario = Usuario.iniciar_sesion(db, mail, password)
        if usuario:
            session['usuario'] = usuario
            return redirect(url_for('menu_principal'))
        else:
            return 'Correo electrónico o contraseña incorrectos'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        mail = request.form['email']
        password = request.form['password']
        mensaje = Usuario.registrar_usuario(db, nombre, mail, password)
        if mensaje == "Registro exitoso":
            return redirect(url_for('login'))
        else:
            return mensaje  # Mostrar el mensaje de error en la página
    return render_template('register.html')

@app.route('/menu_principal')
def menu_principal():
    if 'usuario' in session:
        return render_template('menu_principal.html')
    return redirect(url_for('login'))

@app.route('/blackjack')
def blackjack():
    return render_template('blackjack.html')

@app.route('/poker')
def poker():
    return render_template('poker.html')

@app.route('/slotmachine')
def tragaperras():
    return render_template('slotmachine.html')

@app.route('/carrera_buses')
def carrera_buses():
    return render_template('carrera_buses.html')

@app.route('/hipodromo')
def hipodromo():
    return render_template('hipodromo.html')

@app.route('/agregar_saldo', methods=['GET', 'POST'])
def agregar_saldo():
    if 'usuario' in session:
        if request.method == 'POST':
            try:
                monto = float(request.form['monto'])
                if monto > 0:
                    usuario = session['usuario']
                    usuario_actualizado = Usuario.ingresar_dinero(db, usuario, monto)
                    if usuario_actualizado:
                        session['usuario'] = usuario_actualizado
                        return redirect(url_for('menu_principal'))
                    else:
                        return "Error al agregar saldo. Intente nuevamente."
                else:
                    return "Ingrese un monto positivo."
            except ValueError:
                return "Monto no válido. Intente nuevamente."
        return render_template('agregar_saldo.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.crear_tablas()
    app.run(debug=True)
