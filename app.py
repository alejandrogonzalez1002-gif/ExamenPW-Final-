from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Página 1: Compra de pintura
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        return render_template('Pagina1.html', nombre=nombre,
                               total=total_sin_descuento,
                               descuento=monto_descuento,
                               total_final=total_con_descuento)
    return render_template('Pagina1.html')

# Página 2: Login simple
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }

    if request.method == 'POST':
        usuario = request.form['username']
        contraseña = request.form['password']

        if usuario in usuarios and usuarios[usuario] == contraseña:
            tipo = "Administrador" if usuario == "juan" else "Usuario"
            mensaje = f"Bienvenido {tipo} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template('Pagina2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)

