from flask import render_template, redirect, url_for, request,session
from . import main
from .forms import ProductForm
from .. import db
from ..models import Product,Location
from .tables import ProductsTable


@main.route('/')
def index():

    return 'index page'
    

@main.route('/products')
def viewProducts():

    products = Product.query.all()

    table = ProductsTable(products)

    table.border = True

    return render_template('products.html', table = table)


@main.route('/products/new', methods = ['GET', 'POST'])
def newProduct():

    form = ProductForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            new_product = Product(product_name = form.productName.data)
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('.newProduct'))

    return render_template('newproduct.html', form = form)


@main.route('/products/<int:id>/edit', methods = ['GET', 'POST'])
def editProduct(id):

    product = Product.query.get_or_404(id)

    form = ProductForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            product.product_name = form.productName.data
            db.session.add(product)
            db.session.commit()
            return redirect(url_for('.viewProducts'))

    form.productName.data = product.product_name

    return render_template('editproduct.html', form = form)


@main.route('/products/<int:id>/delete')
def deleteProduct(id):

    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('.viewProducts'))



