#!/bin/bash

# These two options are mutually exclusive:
#    --net host \
#    -p 9090:9090 \
# Select the latter to expose port 9090 to the host if the container is connected to another network (default)

#Note: for data to be persistent prometheus-data is created in /var/lib/docker/volumes/prometheus-data

docker run -d \
    --rm \
    --net host \
    --name prometheus \
    -v "$PWD/prometheus.yaml:/etc/prometheus/prometheus.yml" \
    -v prometheus-data:/prometheus \
    prom/prometheus

