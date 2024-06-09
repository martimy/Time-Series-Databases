# Comaprison 

Here is a comparison table that includes terms used by all TSDBs and the corresponding terms used in relational database:


| Relational Database     | InfluxDB             | Prometheus            | Graphite                |
|-------------------------|----------------------|-----------------------|-------------------------|
| Database                | Database             | N/A (single internal database) | N/A (single internal database) |
| Table                   | Measurement          | Metric                | Metric                  |
| Row                     | Point                | Sample                | Datapoint               |
| Column                  | Field/Tag            | Label                 | N/A                     |
| Primary Key             | Measurement name + Tag set + Timestamp | Metric name + Label set + Timestamp | Metric path + Timestamp |
| Index                   | Tag index            | N/A                   | N/A                     |
| Schema                  | Schemaless           | Schemaless            | Schemaless              |
| SQL Query               | InfluxQL/Flux Query  | PromQL                | Graphite Functions      |
| Retention Policy        | Per database         | Global setting        | Per metric              |


