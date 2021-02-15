# Sparkify's Data Pipelines with Apache Airflow
## Improving a Music-Streaming Apps ETL Pipeline by Enhanced Automation and Monitoring




## Project and Airflow Overview
Sparkify, a **fake** music-streaming application, was pleased with my prior worked and decided to improve it data warehouse ETL pipeline. Given the company's goal of having transparent monitoring, dynamic operations and ability to easily backfill, management and I decided to use Apache Airflow.

Airflow coordinates movements among data storage and processing tools. The software is **not** data processing framework. Nothing is stored in memory.

Airflow's core components:
1) Scheduler - Orchestrates the execution of jobs on a trigger or schedule.
2) Work Queue - Used by the schedule to deliver tasks that need to be run to the workers.
3) Worker Processes - The tasks are defined in the Directed Acyclic Graph (DAG). When the worker completes a task, it will reference the queue to process more work until no further work remains.
4) Database - Stores the workflow's metadata, e.g. credentials, connections, history, and configuration.
5) Web Interface - A control dashboard for users and maintainers.



Management and I selected the following objectives of the upgraded data pipeline:
1) Dynamic and built from reusable tasks
2) Transparent monitoring
3) 
Custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data for a music streaming app called Sparkiy.
