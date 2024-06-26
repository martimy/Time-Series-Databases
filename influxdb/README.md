# InfluxDB

InfluxDB is available in two versions and there is a third version to be available shortly. InfluxDB v2 uses the query language, Flux, which has not been successful in the market. So this example will focus on using InfluxDB v1 and the query langauge, InfluxQL, which is expected to be used in furture developments. 

Here are some of the key terms used by InfluxDB v1:
 
- database: refers to a structured set of data that is optimized for time series data. A database consists of measurements.
- measurement: this is where InfluxDB stores time series data points. 
- point: is a single data entry in a measurement, consisting of a timestamp, fields, and tags. 
- field: Fields hold the actual data values. 
- tag: tags are indexed metadata.
- series: represents a unique set of tag and field values within a measurement. 


## Docker Installtion

```
docker pull influxdb:1.8
```

## Quick Start

1. Create InfluxDB directories

```
$ mkdir data config
```
 
2. Run Docker image

```
docker run \
    --rm -d \
    --name influxdb \
    -p 8086:8086 \
    -v "$PWD/data:/var/lib/influxdb2" \
    -v "$PWD/config:/etc/influxdb2" \
    influxdb:1.8
```

2. Create a database

```
$ curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE mydb"
```

3. Write some data:

```
$ curl -i -XPOST 'http://localhost:8086/write?db=mydb' \
--data-binary 'cpu_load_short,host=server01 value=0.64 1434055562000000000'
```

4. Query data usng InfluxQL:

```
$ curl -G 'http://localhost:8086/query?pretty=true' \
--data-urlencode "db=mydb" --data-urlencode "q=SELECT \"value\" FROM \"cpu_load_short\" WHERE \"host\"='server01'"
```

## Using Python to Write Data

You can use Python to write data to InfluxDB using the `influxdb` module. Run the following script for few minutes the stop the program using `CTRL-C`.

```
$ python3 write_random.py
```

Retrieve all random numbers written by the Python code in csv format:

```
curl -G 'http://localhost:8086/query?pretty=true' \
--data-urlencode "db=mydb" \
--data-urlencode "q=SELECT \"value\" FROM \"random_numbers\" WHERE \"host\"='server01'" \
--header "Accept: application/csv" -o output.csv
```

## using influx

You can use `influx` utility to setup InfluxDB databases and perform other tasks:

The example below shows the database hase two measurements. 

```
$ docker exec -it influxdb influx
Connected to http://localhost:8086 version 1.8.10
InfluxDB shell version: 1.8.10
> use mydb
> show series
key
---
cpu_load_short,host=server01
random_numbers,host=server01
> show measurements
name: measurements
name
----
cpu_load_short
random_numbers
> select * from random_numbers
name: random_numbers
time                host     value
----                ----     -----
1717896870326431266 server01 0.6956190233951661
1717896871343055593 server01 0.837187805972766
1717896872352179116 server01 0.6671158236674488

> quit
```

[For more information](https://docs.influxdata.com/influxdb/v1/guides/write_data/)

