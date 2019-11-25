from flask_table import Table, Col, LinkCol

class ProductsTable(Table):

    id = Col('Id')
    product_name = Col('Product Name')
    edit = LinkCol('Edit','main.editProduct', url_kwargs= dict(id='id'))
    delete = LinkCol('Delete','main.deleteProduct', url_kwargs= dict(id='id'))