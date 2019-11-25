from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):

    productName = StringField('Name of the product', validators = [DataRequired()])
    submit = SubmitField('Submit')