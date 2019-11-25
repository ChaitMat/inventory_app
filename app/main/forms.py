from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):

    productName = StringField('Name of the product', validators = [DataRequired()])
    submit = SubmitField('Submit')


class LocationForm(FlaskForm):

    locationName = StringField('Name of the location', validators = [DataRequired()])
    submit = SubmitField('Submit')