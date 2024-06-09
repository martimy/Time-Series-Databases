# Time Series Databases

A time series database is a specialized database that efficiently stores and retrieves time-stamped data. The data stored is known as time series data due to is time-based nature, where each datapoint is associated with a timestamp that indicates when it was recorded. TSDBs offer several advantages over traditional databases and other storage solutions when it comes to handling time series data.

There are several open source TSDBs available in the market today. These TSDBs are constantly evolving and improving, and each has its own strengths and weaknesses. Choosing the right one depends on the specific use case, data requirements and the organization's infrastructure. 

This repository provides instructions on how to use three popular TSDBs using Docker images and minimal configuration. A Python script is included to generate random data.

- [Graphite](https://graphiteapp.org/)
- [InfluxDB](https://www.influxdata.com/)
- [Prometheus](https://prometheus.io/)

## Usage

Clone this repository

```
$ git clone https://github.com/martimy/Time-Series-Databases
```

Change to the directory of each TSDB and follow the instructions provided.


## Data Model Comparison

The three TSDBs differ significantly in their data models, which impacts their use cases, performance, and features. The following a summary of their data models:

### Graphite

Graphite metrics are formatted as follows:

```
metric_path metric_value metric_timestamp
```

- Metric Path: This is a sot-separated hierarchical names.
- Value: Numeric data point.
- Timestamp: Each data point is associated with a timestamp.

**Example:**

```
servers.room1.cpu.load 0.5 1622543199
```


### InfluxDB

InfluxDB v1 data model includes the following items:

- Measurements: Similar to tables in relational databases. Each measurement contains time series data.
- Tags: Key-value pairs that are indexed for efficient querying. Tags are used for metadata and for filtering data.
- Fields: Key-value pairs that store actual data points. Fields are not indexed, which makes them faster to write but slower to query compared to tags.
- Timestamp: Each data point is associated with a timestamp.

**Example:**

Here is an example showing temperature and humidity of two rooms in a house. In this example, the measurement='home', tags='room', fields='temp, hum', and the timestamp is Unix timestamp in second precision.


```
home,room=LivingRoom temp=21.1,hum=35.9 1641024000
home,room=Kitchen temp=21.0,hum=35.9 1641024000
home,room=LivingRoom temp=21.4,hum=35.9 1641027600
home,room=Kitchen temp=23.0,hum=36.2 1641027600
```

### Prometheus

Prometheus data model includes the following items:

```
<metric name>{<label name>=<label value>, ...}
```

- Metric Name: Identifies the particular time series.
- Labels: Key-value pairs that distinguish different dimensions of a metric. Labels are used for filtering and aggregation.
- Value: Numeric data point.
- Timestamp: Each data point is associated with a millisecond-precision timestamp

Unlike the other two TSDBs, Prometheus uses pull model to get data from targets.

**Example**

A time series with the metric name http_requests_total and the labels method="GET" and handler="/api" could be written like this:

```
http_requests_total{method="GET", handler="/api"} 1027 1622543199
```


