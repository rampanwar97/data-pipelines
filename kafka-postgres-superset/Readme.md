# ---> Create kafka-topics

Command:- kafka-topics.sh --create --topic sales-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

# ---> List All Topics

Command:- kafka-topics.sh --list --bootstrap-server localhost:9092

# ---> Describe a Topic

Command:- kafka-topics.sh --describe --topic sales-topic --bootstrap-server localhost:9092

# ---> Delete a Topic

Command:- kafka-topics.sh --delete --topic sales-topic --bootstrap-server localhost:9092

# ---> Alter a Topic (e.g., Increase Partitions)

Command:- kafka-topics.sh --alter --topic sales-topic --partitions 5 --bootstrap-server localhost:9092

# ---> Produce messages to a Topic

Command:- kafka-console-producer.sh --broker-list localhost:9092 --topic sales-topic

# ---> Consume messages from Topic

Command:- kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sales-topic --from-beginning