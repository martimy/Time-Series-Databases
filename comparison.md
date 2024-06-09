# Comaprison 

Here is a comparison table that includes terms in relational databases and the corresponding term used by each TSDB:


| Relational Database     | InfluxDB v1          | Prometheus            | Graphite                |
|-------------------------|----------------------|-----------------------|-------------------------|
| Database                | Database             | N/A*                  | N/A*                    |
| Table                   | Measurement          | Metric                | Metric                  |
| Row                     | Point                | Sample                | Datapoint               |
| Column                  | Field/Tag            | Label                 | N/A                     |
| Primary Key             | Measurement name + Tag set + Timestamp | Metric name + Label set + Timestamp | Metric path + Timestamp |
| Index                   | Tag index            | N/A                   | N/A                     |
| Schema                  | Schemaless           | Schemaless            | Schemaless              |
| SQL Query               | InfluxQL/Flux Query  | PromQL                | Graphite Functions      |
| Retention Policy        | Per database         | Global setting        | Per metric              |

\* Prometheus and Graphite use single internal database, while InfluxDB supports multiple database

