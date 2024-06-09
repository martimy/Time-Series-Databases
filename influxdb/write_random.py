import random
import time
from influxdb import InfluxDBClient

# Configuration for InfluxDB
host = 'localhost'
port = 8086
dbname = 'mydb'

# Create an InfluxDB client
client = InfluxDBClient(host=host, port=port, database=dbname)

# Function to write random numbers to InfluxDB
def write_random_numbers():
    while True:
        # Generate a random number
        random_number = random.random()

        # Create a JSON body to write to InfluxDB
        json_body = [
            {
                "measurement": "random_numbers",
                "tags": {
                    "host": "server01"
                },
                "fields": {
                    "value": random_number
                }
            }
        ]

        # Write the JSON body to InfluxDB
        client.write_points(json_body)
        print(f"Written: {random_number}")

        # Sleep for a second
        time.sleep(1)

# Run the function to write random numbers to InfluxDB
write_random_numbers()

