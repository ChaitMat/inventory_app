from flask import render_template
from . import main
from .forms import Product


@main.route('/')
def index():

    return 'index page'

@main.route('/newproduct')
def newProduct():

    form = Product()

    return render_template('newproduct.html', form = form)




