import random
import time
import socket

# Configuration for Graphite
graphite_host = 'localhost'
graphite_port = 2003

# Function to send data to Graphite
def send_to_graphite(metric, value, timestamp=None):
    if timestamp is None:
        timestamp = int(time.time())
    message = f"{metric} {value} {timestamp}\n"
    # Create a socket connection to Graphite
    sock = socket.socket()
    sock.connect((graphite_host, graphite_port))
    sock.sendall(message.encode('utf-8'))
    sock.close()

# Function to write random numbers to Graphite
def write_random_numbers():
    while True:
        # Generate a random number
        random_number = random.random()

        # Define the metric name
        metric = "random_numbers.value"

        # Send the data to Graphite
        send_to_graphite(metric, random_number)
        print(f"Written: {random_number}")

        # Sleep for a second
        time.sleep(1)

# Run the function to write random numbers to Graphite
write_random_numbers()
