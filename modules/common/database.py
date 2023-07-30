import sqlite3


class Database:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    def test_connection(self):
        self.cursor.execute("SELECT sqlite_version();")
        result = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {result[0][0]}")

    def get_all_users(self):
        self.cursor.execute("SELECT name, address, city FROM customers")
        result = self.cursor.fetchall()
        return result

    def get_user_address_by_name(self, name):
        self.cursor.execute(
            f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        )
        result = self.cursor.fetchall()
        return result

    def update_product_qnt_by_id(self, product_id, qnt):
        self.cursor.execute(
            f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        )
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        self.cursor.execute(f"SELECT quantity FROM products WHERE id = {product_id}")
        result = self.cursor.fetchall()
        if len(result) != 0:
            return result[0][0]
        else:
            return None

    def insert_product(self, product_id, name, description, qnt):
        self.cursor.execute(
            f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        )
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        self.cursor.execute(f"DELETE FROM products WHERE id = {product_id}")
        self.connection.commit()

    def get_detailed_orders(self):
        self.cursor.execute(
            "SELECT orders.id, customers.name, products.name, products.description, \
            orders.order_date FROM orders JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        )
        result = self.cursor.fetchall()
        return result
