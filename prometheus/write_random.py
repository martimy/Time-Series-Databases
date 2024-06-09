import random
import time
from prometheus_client import start_http_server, Gauge

# Create a metric to track the random numbers
random_number_gauge = Gauge('random_number', 'A random number')

# Function to generate random numbers and update the gauge
def generate_random_numbers():
    while True:
        # Generate a random number
        random_number = random.random()

        # Update the Prometheus gauge with the new random number
        random_number_gauge.set(random_number)
        print(f"Updated random number to {random_number}")

        # Sleep for a second
        time.sleep(1)

if __name__ == '__main__':
    # Start up the server to expose the metrics
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")

    # Generate random numbers indefinitely
    generate_random_numbers()

