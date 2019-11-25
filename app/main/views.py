from flask import render_template, redirect, url_for, request,session
from . import main
from .forms import ProductForm
from .. import db
from ..models import Product,Location


@main.route('/')
def index():

    return 'index page'

@main.route('/newproduct', methods = ['GET', 'POST'])
def newProduct():

    form = ProductForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            new_product = Product(product_name = form.productName.data)
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('.newProduct'))

    return render_template('newproduct.html', form = form)




