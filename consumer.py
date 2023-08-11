from kafka import KafkaConsumer
import pymysql
import json
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Kafka consumer configuration
consumer = KafkaConsumer('data', enable_auto_commit=True)

# MySQL database connection
db = pymysql.connect(host='localhost', user='root', password='Shyam@123', database='test')
cursor = db.cursor()

# Create table if it doesn't exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Category VARCHAR(255),
    Price DECIMAL(10, 2),
    StockQuantity INT
);
'''
cursor.execute(create_table_query)
db.commit()

# Iterate through Kafka messages
for message in consumer:
    try:
        json_data = json.loads(message.value.decode())
        logging.debug("Received JSON data: %s", json_data)  # Updated logging statement

        query = f"INSERT INTO products (ProductID, ProductName, Category, Price, StockQuantity) VALUES (%s, %s, %s, %s, %s)"
        values = (
            json_data["ProductID"],
            json_data["ProductName"],
            json_data["Category"],
            json_data["Price"],
            json_data["StockQuantity"]
        )
        cursor.execute(query, values)
        db.commit()

        logging.debug("Inserted into MySQL successfully")
    except Exception as e:
        logging.error(f"Error processing message: {e}")

cursor.close()
db.close()
