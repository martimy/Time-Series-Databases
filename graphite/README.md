# Graphite


## Install Docker

Pull the official Docker container.

```
$ docker pull graphiteapp/graphite-statsd
```

## Quick Start


1. Run Docker image


```
docker run -d \
    --rm \
    --name graphite \
    -v "$PWD/graphite/conf:/opt/graphite/conf" \
    -v "$PWD/graphite/storage:/opt/graphite/storage" \
    -p 2003-2004:2003-2004 \
    -p 2023-2024:2023-2024 \
    -p 9000:80 \
    graphiteapp/graphite-statsd
```

2. Send data to Graphite

```
$ echo "random_numbers.value 0.5 `date +%s`" | nc localhost 2003
```

3. View the data

Point your Browser to `localhost:9000`. Select `random_numbers` from the left panel.

## Using Python to write data

Run the Python code for a few minutes and watch the chart being populated. Stop the script using `CTRL-C`.

```
$ python3 write_random.py
```


![data](graphite.png)
