from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Product

class ProductForm(FlaskForm):

    productName = StringField('Name of the product', validators = [DataRequired()])
    submit = SubmitField('Submit')


class LocationForm(FlaskForm):

    locationName = StringField('Name of the location', validators = [DataRequired()])
    submit = SubmitField('Submit')


class AddProductForm(FlaskForm):

    selectproduct = QuerySelectField(query_factory=lambda: Product.query.all())
    qty = IntegerField('Quantity', [NumberRange(min=1)])
    submit = SubmitField('Submit')