from flask import Flask, render_template

app = Flask(__name__)

@app.route('/main')
def main ():
    return render_template('main/main.html')

@app.route('/login')
def login ():
    return render_template('login/login.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios/usuarios.html')

@app.route('/editProductos')
def editProductos():
    return render_template('productos/editProductos.html')

if __name__ == '__main__':
    app.run(debug = True, port = 8000)