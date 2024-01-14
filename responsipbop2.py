import mysql.connector

class FashionDatabaseManager:
    def _init_(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS fashion_table (id INT AUTO_INCREMENT PRIMARY KEY, brand_name VARCHAR(255), size VARCHAR(10), stock INT, color VARCHAR(20))"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_data(self, brand_name, size, stock, color):
        query = "INSERT INTO fashion_table (brand_name, size, stock, color) VALUES (%s, %s, %s, %s)"
        values = (brand_name, size, stock, color)
        self.cursor.execute(query, values)
        self.connection.commit()

    def update_data(self, id, new_brand_name, new_size, new_stock, new_color):
        query = "UPDATE fashion_table SET brand_name = %s, size = %s, stock = %s, color = %s WHERE id = %s"
        values = (new_brand_name, new_size, new_stock, new_color, id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_data(self, id):
        query = "DELETE FROM fashion_table WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.connection.commit()

    def select_data(self):
        query = "SELECT * FROM fashion_table"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def print_data(self, data):
        for row in data:
            print(row)

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

# Example of usage
db_manager = FashionDatabaseManager(
    host="localhost",
    user="your_username",
    password="your_password",
    database="Fashion"
)

# Create table (execute this only once)
db_manager.create_table()

# Insert data
db_manager.insert_data("Nike", "M", 20, "Black")
db_manager.insert_data("Adidas", "L", 15, "White")
db_manager.insert_data("Gucci", "S", 10, "Red")
db_manager.insert_data("Zara", "XL", 25, "Blue")
db_manager.insert_data("Chanel", "M", 8, "Pink")

# Update data
db_manager.update_data(1, "Nike", "M", 22, "Green")

# Delete data
db_manager.delete_data(2)

# Select and print data
selected_data = db_manager.select_data()
db_manager.print_data(selected_data)

# Close connection
db_manager.close_connection()