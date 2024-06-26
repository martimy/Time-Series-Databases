# Data Models

Here is summary of each TSDB data models:

### Graphite

Graphite metrics are formatted as follows:

```
metric_path metric_value metric_timestamp
```

- Metric Path: This is a dot-separated hierarchical names.
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


## Comparison with Relational Databases Terms

If you are familiar with relational databases, the following table provides a comparison between concepts and terms used in both types of databases.


| Relational Database     | InfluxDB v1          | Prometheus            | Graphite                |
|-------------------------|----------------------|-----------------------|-------------------------|
| Database                | Database             | N/A*                  | N/A*                    |
| Table                   | Measurement          | Metric                | Metric                  |
| Row                     | Point (measurement + tag set + field set + timestamp) | Sample (value + timestamp) | Datapoint (value + timestamp)              |
| Column                  | Field/Tag            | Label                 | N/A                     |
| Primary Key             | Measurement name + Tag set + Timestamp | Metric name + Label set + Timestamp | Metric path + Timestamp |
| Index                   | Tag index            | N/A                   | N/A                     |
| Schema                  | Schema-less           | Schema-less            | Schema-less              |
| SQL Query               | InfluxQL/Flux Query  | PromQL                | Graphite Functions      |
| Retention Policy        | Per database         | Global setting        | Per metric              |

\* Prometheus and Graphite use single internal database, while InfluxDB supports multiple database

