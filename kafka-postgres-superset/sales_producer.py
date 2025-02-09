from confluent_kafka import Producer
from faker import Faker
import json
import time
import random

# Kafka configuration
KAFKA_BROKER = "localhost:9092"  # Change as needed
TOPIC = "sales-topic"  # Kafka topic name

# Create a Faker instance
faker = Faker()

# Kafka producer configuration
producer_conf = {
    'bootstrap.servers': KAFKA_BROKER
}

producer = Producer(producer_conf)

def generate_random_user():
    """Generate random user data."""
    return {
        "user_id": random.randint(1000, 9999),
        "username": faker.user_name(),
        "email": faker.email(),
        "full_name": faker.name(),
        "address": faker.address(),
        "phone_number": faker.phone_number()
    }

def delivery_report(err, msg):
    """Callback function for Kafka delivery reports."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

if __name__ == "__main__":
    while True:
        user_data = generate_random_user()
        message = json.dumps(user_data)
        
        # Send message to Kafka
        producer.produce(TOPIC, key=str(user_data["user_id"]), value=message, callback=delivery_report)
        
        producer.flush()  # Ensure the message is sent
        
        time.sleep(1)  # Adjust sleep interval as needed
