from flask_table import Table, Col, LinkCol

class ProductsTable(Table):

    id = Col('Id')
    product_name = Col('Product Name')
    edit = LinkCol('Edit','main.editProduct', url_kwargs= dict(id='id'))
    delete = LinkCol('Delete','main.deleteProduct', url_kwargs= dict(id='id'))

class LocationsTable(Table):

    id = Col('Id')
    location_name = Col('Location Name')
    edit = LinkCol('Edit','main.editLocation', url_kwargs= dict(id='id'))
    delete = LinkCol('Delete','main.deleteLocation', url_kwargs= dict(id='id'))
    addproduct = LinkCol('Add Product','main.addProduct', url_kwargs= dict(id='id'))

class ProductsMovementTable(Table):

    id = Col('Id')
    timestamp = Col('Time Stamp')
    from_location = Col('From')
    to_location = Col('To')
    product_id = Col('Product moved')
    qty = Col('Quantity')
    # edit = LinkCol('Edit','main.editProduct', url_kwargs= dict(id='id'))
    # delete = LinkCol('Delete','main.deleteProduct', url_kwargs= dict(id='id'))