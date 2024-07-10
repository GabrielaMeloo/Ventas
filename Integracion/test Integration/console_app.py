import requests
import sys
from datetime import datetime

BASE_URL = "http://localhost:5000"

def list_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        products = response.json()
        if products:
            for product in products:
                print(f"ID: {product['Id']}, Name: {product['Name']}, Description: {product['Description']}, Price: {product['Price']}, Stock: {product['Stock']}")
        else:
            print("No products found.")
    else:
        print(f"Error: Unable to fetch products. Status code: {response.status_code}")

def get_product(product_id):
    response = requests.get(f"{BASE_URL}/product/{product_id}")
    if response.status_code == 200:
        product = response.json()
        print(f"ID: {product['Id']}, Name: {product['Name']}, Description: {product['Description']}, Price: {product['Price']}, Stock: {product['Stock']}")
    else:
        print(f"Error: Unable to fetch product. Status code: {response.status_code}")

def add_product(name, description, price, stock):
    payload = {
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }
    response = requests.post(f"{BASE_URL}/product", json=payload)
    print(response.json().get('message', 'Error adding product'))

def update_product(product_id, name, description, price, stock):
    payload = {
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }
    response = requests.put(f"{BASE_URL}/product/{product_id}", json=payload)
    print(response.json().get('message', 'Error updating product'))

def delete_product(product_id):
    response = requests.delete(f"{BASE_URL}/product/{product_id}")
    print(response.json().get('message', 'Error deleting product'))

def list_orders():
    response = requests.get(f"{BASE_URL}/orders")
    if response.status_code == 200:
        orders = response.json()
        if orders:
            for order in orders:
                print(f"Order ID: {order['Id']}, Product ID: {order['ProductId']}, Quantity: {order['Quantity']}, Total Price: {order['TotalPrice']}, Date: {order['Date']}")
        else:
            print("No orders found.")
    else:
        print(f"Error: Unable to fetch orders. Status code: {response.status_code}")

def add_order(product_id, quantity, total_price, date):
    payload = {
        "product_id": product_id,
        "quantity": quantity,
        "total_price": total_price,
        "date": date
    }
    response = requests.post(f"{BASE_URL}/order", json=payload)
    print(response.json().get('message', 'Error adding order'))

def update_order(order_id, product_id, quantity, total_price, date):
    payload = {
        "product_id": product_id,
        "quantity": quantity,
        "total_price": total_price,
        "date": date
    }
    response = requests.put(f"{BASE_URL}/order/{order_id}", json=payload)
    print(response.json().get('message', 'Error updating order'))

def delete_order(order_id):
    response = requests.delete(f"{BASE_URL}/order/{order_id}")
    print(response.json().get('message', 'Error deleting order'))

def main():
    print("Welcome to the Core Web Service Console App")
    while True:
        print("\nMenu:")
        print("1. List Products")
        print("2. Get Product by ID")
        print("3. Add Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. List Orders")
        print("7. Add Order")
        print("8. Update Order")
        print("9. Delete Order")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_products()
        elif choice == '2':
            product_id = int(input("Enter Product ID: "))
            get_product(product_id)
        elif choice == '3':
            name = input("Enter Product Name: ")
            description = input("Enter Product Description: ")
            price = float(input("Enter Product Price: "))
            stock = int(input("Enter Product Stock: "))
            add_product(name, description, price, stock)
        elif choice == '4':
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            description = input("Enter Product Description: ")
            price = float(input("Enter Product Price: "))
            stock = int(input("Enter Product Stock: "))
            update_product(product_id, name, description, price, stock)
        elif choice == '5':
            product_id = int(input("Enter Product ID to delete: "))
            delete_product(product_id)
        elif choice == '6':
            list_orders()
        elif choice == '7':
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity: "))
            total_price = float(input("Enter Total Price: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            date = datetime.strptime(date, '%Y-%m-%d').isoformat()
            add_order(product_id, quantity, total_price, date)
        elif choice == '8':
            order_id = int(input("Enter Order ID: "))
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity: "))
            total_price = float(input("Enter Total Price: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            date = datetime.strptime(date, '%Y-%m-%d').isoformat()
            update_order(order_id, product_id, quantity, total_price, date)
        elif choice == '9':
            order_id = int(input("Enter Order ID to delete: "))
            delete_order(order_id)
        elif choice == '0':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
