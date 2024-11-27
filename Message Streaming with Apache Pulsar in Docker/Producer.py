import pulsar

# Create a Pulsar client by connecting to the Pulsar broker
client = pulsar.Client('pulsar://localhost:6650')

# Create a producer on a topic named 'my-topic'
producer = client.create_producer('my-topic')

# Send a message to the topic
producer.send(('Hello World').encode('utf-8'))

print("Message sent")

# Close the Pulsar client
client.close()
