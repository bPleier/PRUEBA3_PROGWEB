#PRUEBA N°3 PROGRAMACIÓN WEB
#DILAN GATICA MOYA

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/ejercicio_1', methods=['GET', 'POST'])
def ejercicio_1():
    if request.method == 'POST':
        nota_1 = int(request.form['nota_1'])
        nota_2 = int(request.form['nota_2'])
        nota_3 = int(request.form['nota_3'])
        promedio = (nota_1 + nota_2 + nota_3) / 3
        asistencia = int(request.form['asistencia'])
        if asistencia >= 70 and promedio >= 40:
            return render_template('ejercicio_1.html', promedio=promedio, ramo='APROBADO', nota_1=nota_1, nota_2=nota_2, nota_3=nota_3, asistencia=asistencia)
        else:
            return render_template('ejercicio_1.html', promedio=promedio, ramo='REPROBADO', nota_1=nota_1, nota_2=nota_2, nota_3=nota_3, asistencia=asistencia)
    return render_template('ejercicio_1.html')

@app.route('/ejercicio_2', methods=['GET','POST'])
def ejercicio_2():
    if request.method == 'POST':
        nombre_1 = (request.form['nombre_1'])
        nombre_2 = (request.form['nombre_2'])
        nombre_3 = (request.form['nombre_3'])
        if len(nombre_1) > len(nombre_2) and len(nombre_1) > len(nombre_3):
            return render_template('ejercicio_2.html', nombre_1=nombre_1, nombre_2=nombre_2, nombre_3=nombre_3,
                                   resultado=f'El nombre con mayor cantidad de carácteres es: {nombre_1}',
                                   cantidad=f'El nombre tiene: {len(nombre_1)} carácteres.')
        elif len(nombre_2) > len(nombre_1) and len(nombre_2) > len(nombre_3):
            return render_template('ejercicio_2.html', nombre_1=nombre_1, nombre_2=nombre_2, nombre_3=nombre_3,
                                   resultado=f'El nombre con mayor cantidad de carácteres es: {nombre_2}',
                                   cantidad=f'El nombre tiene: {len(nombre_2)} carácteres.')
        elif len(nombre_3) > len(nombre_1) and len(nombre_3) > len(nombre_2):
            return render_template('ejercicio_2.html', nombre_1=nombre_1, nombre_2=nombre_2, nombre_3=nombre_3,
                                   resultado=f'El nombre con mayor cantidad de carácteres es: {nombre_3}',
                                   cantidad=f'El nombre tiene: {len(nombre_3)} carácteres.')
    return render_template('ejercicio_2.html')


if __name__ == '__main__':
    app.run(debug=True)

