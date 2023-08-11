from kafka import KafkaProducer
import csv
import json
import time

# Kafka producer configuration
producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'data'

# CSV file path
csv_file_path = 'products.csv'

def send_data_to_kafka(data_dict):
    data_json = json.dumps(data_dict)
    producer.send(topic, value=data_json.encode('utf-8'))

while True:
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        processed_rows = set()  # Keep track of processed rows

        for row in csv_reader:
            row_id = int(row[0])
            if row_id not in processed_rows:
                data_dict = {
                    "ProductID": row_id,
                    "ProductName": row[1],
                    "Category": row[2],
                    "Price": float(row[3]),
                    "StockQuantity": int(row[4])
                }
                send_data_to_kafka(data_dict)
                processed_rows.add(row_id)

    time.sleep(5)  # Wait for 5 seconds before checking for new data
