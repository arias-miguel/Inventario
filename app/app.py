from flask import Flask, render_template, request, redirect
from forms.forms import *
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/main')
def main ():
    return render_template('main/main.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        formulario = FormularioIngreso()
        return render_template('login/login.html', form = formulario)
    if request.method == 'POST':
        return redirect("/productos")
    

@app.route('/usuarios', methods = ['GET', 'POST'])
def usuarios():
    return render_template('usuarios/usuarios.html')

@app.route('/usuarios/crear/<id>', methods = ['GET', 'POST'])
def usuarioscrear(id):
    if request.method == 'GET':
        formulario = FormularioUsuario()
        return render_template('usuarios/usuarioscrear.html', form = formulario)
    if request.method == 'POST':
        return redirect("/usuarios/")
    return render_template('usuarios/usuarioscrear.html')

@app.route('/usuarios/editar/<id>', methods = ['GET', 'POST'])
def usuarioseditar(id):
    if request.method == 'GET':
        formulario = FormularioUsuario()
        return render_template('usuarios/editarusuario.html', form = formulario)
    if request.method == 'POST':
        return redirect("/usuarios/")
    return render_template('usuarios/editarusuario.html')


@app.route('/productos/editar/<id>', methods = ['GET', 'POST'])
def productoseditar(id):
    if request.method == 'GET':
        formulario = FormularioProducto()
        return render_template('productos/editar-producto.html', form = formulario)
    if request.method == 'POST':
        return redirect("/productos/")
    return render_template('productos/editar-producto.html')

@app.route('/productos/crear/<id>', methods = ['GET', 'POST'])
def productoscrear(id):
    if request.method == 'GET':
        formulario = FormularioProducto()
        return render_template('productos/crear-producto.html.', form = formulario)
    if request.method == 'POST':
        return redirect("/productos/")
    return render_template('productos/crear-producto.html')

@app.route('/productos')
def productos():
    return render_template('productos/productos.html')

@app.route('/proveedores', methods = ['GET', 'POST'])
def proveedores():
    if request.method == 'GET':
        formulario = FormularioProveedor()
        return render_template('proveedores/proveedores.html.', form = formulario)
    if request.method == 'POST':
        return redirect("/productos/")
    return render_template('proveedores/proveedores.html')

@app.route('/proveedores/crear', methods = ['GET', 'POST'])
def proveedorescrear():
    if request.method == 'GET':
        formulario = FormularioProveedor()
        return render_template('proveedores/proveedorescrear.html.', form = formulario)
    if request.method == 'POST':
        return redirect("/productos/")
    return render_template('proveedores/proveedorescrear.html')

@app.route('/proveedores/editar', methods = ['GET', 'POST'])
def proveedoreseditar():
    if request.method == 'GET':
        formulario = FormularioProveedor()
        return render_template('proveedores/proveedoreseditar.html.', form = formulario)
    if request.method == 'POST':
        return redirect("/productos/")
    return render_template('proveedores/proveedoreseditar.html')

@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    return render_template('dashboard/dashboard.html')





if __name__ == '__main__':
    app.run(debug = True, port = 8000)