from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CheckMaterial(FlaskForm):
    material = StringField('Material',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Verificar')


class CheckLocal(FlaskForm):
    material_descartado = StringField('Material',
                        validators=[DataRequired(), Length(min=2, max=20)])
    coordenadas_x = FloatField('Latitude (em float)', validators=[DataRequired()])
    coordenadas_y = FloatField('Longitude (em float)', validators=[DataRequired()])
    submit = SubmitField('Procurar')