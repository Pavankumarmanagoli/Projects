import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic', 'my-subscription')
msg = consumer.receive()
print("Received message: '%s'" % msg.data().decode('utf-8'))
consumer.acknowledge(msg)
client.close()