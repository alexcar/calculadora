from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

EXPRESSAO = [('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')]

class CalcularForm(FlaskForm):
    valor1 = IntegerField('Valor1')
    expressao = SelectField(u'expressao', choices=EXPRESSAO)
    valor2 = IntegerField('Valor2')
    submit = SubmitField('Enviar')