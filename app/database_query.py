from app import db


def get_products(): 
    result = db.engine.execute('SELECT * FROM Product') 
    products = [dict(row) for row in result] 
    return products
    

products=get_products()

for product in products:
    print(product['price'])

