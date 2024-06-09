#!/bin/bash

docker run \
    --rm -d \
    --name influxdb \
    -p 8086:8086 \
    -v "$PWD/data:/var/lib/influxdb2" \
    -v "$PWD/config:/etc/influxdb2" \
    influxdb:1.8
