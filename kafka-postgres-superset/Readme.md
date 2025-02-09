# Reffrence :- https://medium.com/@Shamimw/kafka-a-complete-tutorial-part-3-kafka-command-cheat-sheet-40d8e1d9a6c3

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

# ---> Create consumer group

Command:- kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sales-topic --group sales-consumer-group

# ---> Consume Messages from Specific Offset

Command:- kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sales-topic --offset 10 --partition 

# ---> List consumer groups

Command:- kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list

# ---> Describe Consumer group

Command:- kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group sales-consumer-group

# ---> Reset Consumer group offsets to the earliest

Command:- kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group sales-consumer-group --reset-offsets --to-earliest --topic sales-topic --execute