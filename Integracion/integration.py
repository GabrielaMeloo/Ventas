from flask import Flask, request, jsonify
from flask_cors import CORS
import zeep
import logging
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Deshabilitar advertencias de verificación SSL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

app = Flask(__name__)
CORS(app)

wsdl = 'https://localhost:44303/CoreWebService.asmx?wsdl'

# Configurar el logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Verificar conexión al servicio web
try:
    response = requests.get(wsdl.replace('?wsdl', ''), verify=False)
    response.raise_for_status()
    logger.info("Successfully connected to the service")
except requests.exceptions.RequestException as e:
    logger.error(f"Error connecting to the service: {e}")
    raise

# Inicializar el cliente SOAP
try:
    session = requests.Session()
    session.verify = False
    client = zeep.Client(wsdl=wsdl, transport=zeep.transports.Transport(session=session))
except Exception as e:
    logger.error(f"Error initializing SOAP client: {e}")
    raise

# Productos
@app.route('/products', methods=['GET'])
def get_products():
    try:
        response = client.service.GetProducts()
        products = zeep.helpers.serialize_object(response)
        return jsonify(products)
    except Exception as e:
        logger.error(f"Error in get_products: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    try:
        response = client.service.GetProduct(id)
        product = zeep.helpers.serialize_object(response)
        return jsonify(product)
    except Exception as e:
        logger.error(f"Error in get_product: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    description = data['description']
    price = data['price']
    stock = data['stock']
    try:
        client.service.PostProducts(name, description, price, stock)
        return jsonify({'message': 'Product added successfully'})
    except Exception as e:
        logger.error(f"Error in add_product: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    name = data['name']
    description = data['description']
    price = data['price']
    stock = data['stock']
    try:
        client.service.PutProduct(id, name, description, price, stock)
        return jsonify({'message': 'Product updated successfully'})
    except Exception as e:
        logger.error(f"Error in update_product: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        client.service.DeleteProduct(id)
        return jsonify({'message': 'Product deleted successfully'})
    except Exception as e:
        logger.error(f"Error in delete_product: {e}")
        return jsonify({'error': str(e)}), 500

# Pedidos
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        response = client.service.GetOrders()
        orders = zeep.helpers.serialize_object(response)
        logger.info(f"Orders retrieved: {orders}")  # Imprimir la respuesta para depuración
        return jsonify(orders)
    except Exception as e:
        logger.error(f"Error in get_orders: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/order', methods=['POST'])
def add_order():
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']
    total_price = data['total_price']
    date = data['date']
    try:
        client.service.PostOrder(product_id, quantity, total_price, date)
        return jsonify({'message': 'Order added successfully'})
    except Exception as e:
        logger.error(f"Error in add_order: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/order/<int:id>', methods=['PUT'])
def update_order(id):
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']
    total_price = data['total_price']
    date = data['date']
    try:
        client.service.PutOrder(id, product_id, quantity, total_price, date)
        return jsonify({'message': 'Order updated successfully'})
    except Exception as e:
        logger.error(f"Error in update_order: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/order/<int:id>', methods=['DELETE'])
def delete_order(id):
    try:
        client.service.DeleteOrder(id)
        return jsonify({'message': 'Order deleted successfully'})
    except Exception as e:
        logger.error(f"Error in delete_order: {e}")
        return jsonify({'error': str(e)}), 500

# Pagos
@app.route('/payment/<int:id>', methods=['GET'])
def get_payment(id):
    try:
        response = client.service.GetPayment(id)
        payment = zeep.helpers.serialize_object(response)
        return jsonify(payment)
    except Exception as e:
        logger.error(f"Error in get_payment: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/payment', methods=['POST'])
def add_payment():
    data = request.get_json()
    order_id = data['order_id']
    amount = data['amount']
    date = data['date']
    status = data['status']
    try:
        client.service.PostPayment(order_id, amount, date, status)
        return jsonify({'message': 'Payment added successfully'})
    except Exception as e:
        logger.error(f"Error in add_payment: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/payment/<int:id>', methods=['DELETE'])
def delete_payment(id):
    try:
        client.service.DeletePayment(id)
        return jsonify({'message': 'Payment deleted successfully'})
    except Exception as e:
        logger.error(f"Error in delete_payment: {e}")
        return jsonify({'error': str(e)}), 500

# Inventario
@app.route('/inventory', methods=['GET'])
def get_inventory():
    try:
        response = client.service.GetInventory()
        inventory = zeep.helpers.serialize_object(response)
        return jsonify(inventory)
    except Exception as e:
        logger.error(f"Error in get_inventory: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']
    try:
        client.service.PostInventoryItem(product_id, quantity)
        return jsonify({'message': 'Inventory item added successfully'})
    except Exception as e:
        logger.error(f"Error in add_inventory_item: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/inventory/<int:id>', methods=['PUT'])
def update_inventory_item(id):
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']
    try:
        client.service.PutIventoryItem(id, product_id, quantity)
        return jsonify({'message': 'Inventory item updated successfully'})
    except Exception as e:
        logger.error(f"Error in update_inventory_item: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/inventory/<int:id>', methods=['DELETE'])
def delete_inventory_item(id):
    try:
        client.service.DeleteIventoryItem(id)
        return jsonify({'message': 'Inventory item deleted successfully'})
    except Exception as e:
        logger.error(f"Error in delete_inventory_item: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
