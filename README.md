# datapipeline  with Apache kafka 

This repository contains a sample data pipeline created using Apache kafka, designed to fetch a CSV file and upload it to a MySQL database.

## Prerequisites

Before running the data pipeline, ensure you have the following components set up:

Apache Kafka: Install Apache Kafka and zookeeper on your system or server.

MySQL Database: Set up a MySQL database where you want to upload the data.

Python Libraries: Install the required Python libraries using the following command:

   pip install kafka-python pymysql


## Steps 

1. Prepare Your CSV File
  Place your CSV file (your_file.csv) in the same directory as the scripts.

2. Start Kafka and ZooKeeper
  Start ZooKeeper and Kafka brokers. Navigate to your Kafka installation directory and run the following commands in separate terminal

  bin/zookeeper-server-start.sh config/zookeeper.properties
  bin/kafka-server-start.sh config/server.properties

3. Create a Kafka Topic
   Create a Kafka topic named 'csv-topic' using the following command:
   bin/kafka-topics.sh --create --topic csv-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

4. Run the Kafka Producer
   when running kafka producer it fetch the data from the csv file and store it into the kafka Topic
   python producer.py  ( product script is in the repo)

6. Run the Kafka Consumer
    In another terminal, run the Kafka consumer script to retrieve messages from the Kafka topic and insert data into the MySQL database:

   python consumer.py (consumer script is in the repo)

7. Verify MySQL Database
    Check your MySQL database to ensure that the data from the CSV file has been successfully inserted into the 'products' table.

   ## Note

   Make sure to replace placeholders such as 'your_file.csv', 'localhost:9092', 'your_username', 'your_password', and 'your_database' with actual values in the scripts.


   




