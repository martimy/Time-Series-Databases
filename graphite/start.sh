#!/bin/bash

docker run -d \
    --rm \
    --name graphite \
    -v "$PWD/graphite/conf:/opt/graphite/conf" \
    -v "$PWD/graphite/storage:/opt/graphite/storage" \
    -p 2003-2004:2003-2004 \
    -p 2023-2024:2023-2024 \
    -p 9000:80 \
    graphiteapp/graphite-statsd
