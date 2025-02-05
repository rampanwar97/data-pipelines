from confluent_kafka import Producer
import json
import random
import time
from datetime import datetime

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'sales-producer'
}

# Create Producer instance
producer = Producer(conf)

# Kafka topic
topic = 'sales-topic'

def delivery_report(err, msg):
    """
    Callback function to check if the message was successfully delivered.
    """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def generate_sales_data():
    """
    Generate random sales data.
    """
    products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera']
    customers = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

    return {
        'sale_id': random.randint(1000, 9999),  # Random sale ID
        'product': random.choice(products),     # Random product
        'quantity': random.randint(1, 10),      # Random quantity
        'price': round(random.uniform(10, 1000), 2),  # Random price
        'customer': random.choice(customers),   # Random customer
        'timestamp': datetime.now().isoformat() # Current timestamp
    }

def produce_sales_data():
    """
    Produce sales data to the Kafka topic.
    """
    try:
        while True:
            # Generate random sales data
            sales_data = generate_sales_data()

            # Convert sales data to JSON string
            sales_data_json = json.dumps(sales_data)

            # Produce message to Kafka topic
            producer.produce(topic, key=str(sales_data['sale_id']), value=sales_data_json, callback=delivery_report)

            # Wait for any outstanding messages to be delivered
            producer.poll(0)

            # Print the generated sales data
            print(f"Produced: {sales_data}")

            # Wait for 2 seconds before producing the next message
            time.sleep(2)
    except KeyboardInterrupt:
        print("Producer stopped.")
    finally:
        # Wait for all messages to be delivered
        producer.flush()

if __name__ == '__main__':
    produce_sales_data()