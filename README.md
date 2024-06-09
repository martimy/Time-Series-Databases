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

The three TSDBs differ significantly in their data models, which impacts their use cases, performance, and features. Here is a [summary of their data models](models.md).

