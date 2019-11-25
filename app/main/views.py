from flask import render_template, redirect, url_for, request,session
from . import main
from .forms import ProductForm, LocationForm
from .. import db
from ..models import Product,Location
from .tables import ProductsTable, LocationsTable


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
            return redirect(url_for('.viewProducts'))

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

@main.route('/locations')
def viewLocations():

    locations = Location.query.all()

    table = LocationsTable(locations)

    table.border = True

    return render_template('locations.html', table = table)


@main.route('/locations/new', methods = ['GET', 'POST'])
def newLocation():

    form = LocationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            new_location = Location(location_name = form.locationName.data)
            db.session.add(new_location)
            db.session.commit()
            return redirect(url_for('.viewLocations'))

    return render_template('newlocation.html', form = form)


@main.route('/locations/<int:id>/edit', methods = ['GET', 'POST'])
def editLocation(id):

    location = Location.query.get_or_404(id)

    form = LocationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            location.location_name = form.locationName.data
            db.session.add(location)
            db.session.commit()
            return redirect(url_for('.viewLocations'))

    form.locationName.data = location.location_name

    return render_template('editlocation.html', form = form)


@main.route('/locations/<int:id>/delete')
def deleteLocation(id):

    location = Location.query.get_or_404(id)
    db.session.delete(location)
    db.session.commit()
    return redirect(url_for('.viewLocations'))


    



