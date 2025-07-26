from flask import Flask, request, render_template, redirect
from datetime import datetime
import json
import os

app = Flask(__name__)
ARCHIVO = 'clientes.json'

# Mostrar el index
@app.route('/')
def index():
    return render_template('index.html')


# Mostrar el formulario
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

# Mostrar el formulario
@app.route('/habitaciones')
def habitaciones():
    return render_template('habitaciones.html')


# Mostrar el formulario
@app.route('/galeria')
def galeria():
    return render_template('galeria.html')


# Guardar los datos recibidos en un archivo JSON
@app.route('/guardar_cliente', methods=['POST'])
def guardar_cliente():
    datos = request.get_json()
    archivo = 'clientes.json'

    # Si el archivo existe, cargar su contenido; si no, usar una lista vacía
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            clientes = json.load(f)
    else:
        clientes = []

    # Agregar nuevo cliente a la lista
    clientes.append(datos)

    # Guardar la lista actualizada en el archivo
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)
        
def guardar_clientes(clientes):
    with open(ARCHIVO, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)


@app.route('/ir_clientes')
def ir_clientes():
    return render_template('buscar_cliente.html')


@app.route('/buscar_cliente', methods=['GET', 'POST'])
def buscar_cliente():
    resultado = None
    mensaje = None

    if request.method == 'POST':
        termino = request.form.get('busqueda').lower()

        if os.path.exists('clientes.json'):
            with open('clientes.json', 'r', encoding='utf-8') as f:
                clientes = json.load(f)

            for c in clientes:
                if termino in c['nombre'].lower() or termino in c['correo'].lower() :
                    resultado = c
                    break

            if not resultado:
                mensaje = "❌ Cliente no encontrado."
        else:
            mensaje = "⚠️ No hay datos registrados aún."

    return render_template('buscar_cliente.html', resultado=resultado, mensaje=mensaje)


@app.route('/buscar_cliente_fecha', methods=['POST'])
def buscar_cliente_fecha():
    resultados = []
    mensaje = None

    fecha_inicio_str = request.form.get('fecha_inicio')
    fecha_fin_str = request.form.get('fecha_fin')

    if not fecha_inicio_str or not fecha_fin_str:
        mensaje = "⚠️ Debes ingresar ambas fechas."
        return render_template('buscar_cliente.html', resultados_fecha=None, mensaje_fecha=mensaje)

    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
        fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d")
    except ValueError:
        mensaje = "⚠️ Formato de fecha inválido."
        return render_template('buscar_cliente.html', resultados_fecha=None, mensaje_fecha=mensaje)

    if os.path.exists('clientes.json'):
        with open('clientes.json', 'r', encoding='utf-8') as f:
            clientes = json.load(f)

        for c in clientes:
            try:
                fecha_ingreso = datetime.strptime(c['fecha_ingreso'], "%Y-%m-%d")
                fecha_salida = datetime.strptime(c['fecha_fin'], "%Y-%m-%d")
                
                # Comprobamos si hay intersección entre rangos
                if fecha_ingreso <= fecha_fin and fecha_salida >= fecha_inicio:
                    resultados.append(c)
            except Exception as e:
                continue

        if not resultados:
            mensaje = "❌ No se encontraron clientes en ese rango de fechas."
    else:
        mensaje = "⚠️ No hay datos registrados aún."

    return render_template('buscar_cliente.html', resultados_fecha=resultados, mensaje_fecha=mensaje)

Usuario_admin = "admin"
Contraseña_admin = "1234"

@app.route('/ir_administracion')
def ir_administracion():
    return render_template('administracion.html')

@app.route('/buscar_admin', methods=['GET', 'POST'])
def buscar_admin():
    resultado = None
    mensaje = None

    if request.method == 'POST':
        Usuario = request.form.get('usuario').lower()
        Contraseña = request.form.get('contraseña').lower()

        if Usuario == Usuario_admin and Contraseña == Contraseña_admin:
            mensaje = "✅ Acceso concedido. Bienvenido al panel de administración." 
            resultado = True 
            return redirect('/ir_clientes')
        
        else:
            mensaje = "❌ Acceso denegado. Usuario o contraseña incorrectos."
            resultado = False
    
    return render_template('administracion.html',resultado=resultado, mensaje=mensaje)


def cargar_cliente():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

@app.route('/eliminar_cliente', methods=['POST'])
def eliminar_cliente():
    correo = request.form['correo']
    clientes = cargar_cliente()
    clientes = [c for c in clientes if c['correo'] != correo]
    guardar_clientes(clientes)
    return redirect('/buscar_cliente')

if __name__ == '__main__':
    app.run(debug=True, port=5005)
    