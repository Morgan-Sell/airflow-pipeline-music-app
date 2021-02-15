# Sparkify's Data Pipeline with Apache Airflow
## Improving a Music-Streaming Apps ETL Pipeline by Enhancing Automation and Monitoring

<img src="https://github.com/Morgan-Sell/airflow-pipeline-music-app/blob/main/img/guitar_laptop.jpg" width="850" height="275">


## Project and Airflow Overview
Sparkify, a **fake** music-streaming application, was pleased with my prior worked and contracted me to further the sophistication of its data warehouse ETL pipeline. Given the company's goals of having transparent monitoring, dynamic operations, and the ability to easily backfill, management and I decided to use Apache Airflow.

The project's objective is to extract raw JSON files of songs played by users and Sparkify's music library then transform the data into the appropriate facts and dimensions tables then load the tables into AWS Redshift, which is used by the data analytics/science department. 

Airflow coordinates movements among data storage and processing tools. The software is **not** a data processing framework. Nothing is stored in memory.

### Airflow's Core Components:
1) Scheduler - Orchestrates the execution of jobs on a trigger or schedule.
2) Work Queue - Used by the scheduler to deliver tasks that need to be run to the workers.
3) Worker Processes - The tasks are defined in the Directed Acyclic Graph (DAG). When the worker completes a task, it will reference the queue to process more work until no further work remains.
4) Database - Stores the workflow's metadata, e.g. credentials, connections, history, and configuration.
5) Web Interface - A control dashboard for users and maintainers.

An Airflow DAG is comprised of operators that define the atomic steps of work. In this project, I developed custom operators that perform frequently used procedures and allow for multiple use cases. One example is the `LoadDimensionOperator`. 

Each operator performs one definite task, e.g. load data from S3 to redshift. This both allows for parallelization, which decreases the required time to complete the procedure, and simplifies debugging/monitoring. Well-defined operators improve transparency and provide more information when resolving bugs.


### Sparkify's DAG Diagram
<img src="https://github.com/Morgan-Sell/airflow-pipeline-music-app/blob/main/img/dag_graph.png" width="750" height="180">

The diagram above visualizes the DAG's workflow. Each rectangle represents an operator/task. The arrows demonstrate dependencies. Meanwhile, the `Create_tables` operator functions independently.

The diagram also shows multi-purpose operators that are dynamic and work in parallel. In addition to performing ETL, the DAG coordinates a data quality check. The `Run_data_quality_checks` ensures that NULL values do not exist for any of the Redshift tables' primary keys, e.g. `artist_id` and `song_id`.

## Credit
This project was completed as part of Udacity's Data Engineering nanodegree program.

## Packages
- Airflow
