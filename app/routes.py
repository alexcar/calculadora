from flask import render_template, flash, redirect
from app import app
from app.calcular import CalcularForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    form = CalcularForm()
    if form.validate_on_submit():
        expressao = form.expressao.data
        resultado = 0

        if expressao == '+':
            resultado = form.valor1.data + form.valor2.data
        
        if expressao == '-':
            resultado = form.valor1.data - form.valor2.data

        if expressao == '*':
            resultado = form.valor1.data * form.valor2.data

        if expressao == '/':
            if form.valor2.data == 0:
                flash('Impossível dividir por 0')
                return redirect('/index')

            resultado = form.valor1.data / form.valor2.data
        
        flash('Resultado: {} {} {} = {} '.format(
            form.valor1.data, expressao, form.valor2.data, resultado))
        return redirect('/index')
    return render_template('calcular.html', form=form)
