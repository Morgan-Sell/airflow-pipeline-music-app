# Sparkify's Data Pipelines with Apache Airflow
## Improving a Music-Streaming Apps ETL Pipeline by Enhanced Automation and Monitoring

<img src="https://github.com/Morgan-Sell/airflow-pipeline-music-app/blob/main/img/guitar_laptop.jpg" width="800" height="250">


## Project and Airflow Overview
Sparkify, a **fake** music-streaming application, was pleased with my prior worked and decided to improve it data warehouse ETL pipeline. Given the company's goal of having transparent monitoring, dynamic operations and ability to easily backfill, management and I decided to use Apache Airflow.

Airflow coordinates movements among data storage and processing tools. The software is **not** data processing framework. Nothing is stored in memory.

Airflow's core components:
1) Scheduler - Orchestrates the execution of jobs on a trigger or schedule.
2) Work Queue - Used by the schedule to deliver tasks that need to be run to the workers.
3) Worker Processes - The tasks are defined in the Directed Acyclic Graph (DAG). When the worker completes a task, it will reference the queue to process more work until no further work remains.
4) Database - Stores the workflow's metadata, e.g. credentials, connections, history, and configuration.
5) Web Interface - A control dashboard for users and maintainers.

An Airflow DAG is comprised of operators that define the atomic steps of work. In this project, I developed custom operators that perform frequently used operations and allow for multiple use cases. One example is the LoadDimensionOperator. Each operator should on perform one, e.g. load data from S3 to redshift. This both allows for parrallelization, which decreases the required time to complete the operation, and simpflies debugging/monitoring. Well-defined operators improve transparency and provide more information when looking for a bug.

### Sparkify's DAG Diagram
<img src="https://github.com/Morgan-Sell/airflow-pipeline-music-app/blob/main/img/airflow_operators_diagram.png" width="800" height="250">
