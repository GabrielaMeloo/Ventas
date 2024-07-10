import mysql.connector

def get_products():
    # Conectar a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ga240409@**",
        database="ventasWeb"
    )
    cursor = conn.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT id, name, description, price, image_url FROM products")
    products = cursor.fetchall()

    # Cerrar la conexión
    cursor.close()
    conn.close()

    return products

# Ejemplo de uso
if __name__ == "__main__":
    products = get_products()
    for product in products:
        print(product)
