from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

# Vai extender do FlaskForm e será um formulário
class CadastroForm(FlaskForm):
    usuario = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='E-mail:', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Senha:', validators=[Length(min=6 ), DataRequired()])
    senha2 = PasswordField(label='Confirmação de senha:', validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Cadastrar')
    