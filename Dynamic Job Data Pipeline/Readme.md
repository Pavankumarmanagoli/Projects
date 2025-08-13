# Dynamic Job Data Pipeline

A production-ready pipeline for collecting and analyzing job postings for the Irish market. The workflow ingests data from The Muse public API and historical JSON feeds, loads it into Google Cloud storage, cleans and transforms it with Apache Spark and dbt, and orchestrates daily and batch operations through Apache Airflow.

## Objective

Originally built to streamline labour-market research in Ireland, this project automates the collection of live and historical job postings, standardises their schemas, and loads them into BigQuery. The curated dataset enables analysts and engineers to track hiring trends, assess skill demand, and build dashboards without manual data wrangling.

---

## Table of Contents
- [Objective](#objective)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Pipeline Components](#pipeline-components)
  - [Airbyte](#airbyte)
  - [Airflow](#airflow)
  - [Spark](#spark)
- [Project Layout](#project-layout)
- [Technology Stack](#technology-stack)
- [License](#license)

---

## Architecture
1. **Ingestion** – Airbyte and custom HTTP tasks pull job postings from the Muse API and from historical datasets.
2. **Storage** – Raw JSON files are stored in Google Cloud Storage and then loaded into BigQuery.
3. **Transformation** – dbt models and Spark jobs standardise the schema, generate surrogate keys and remove invalid characters.
4. **Orchestration** – Airflow schedules daily incremental loads and historic backfills.
5. **Visualisation** – Processed data can be explored in downstream BI tools such as Looker or Data Studio.

---

## Quick Start
Clone the repository and navigate to this project:

```bash
git clone https://github.com/Pavankumarmanagoli/Projects.git
cd "Projects/Dynamic Job Data Pipeline"
```

Prerequisites:
- Docker and Docker Compose
- Python 3.10+
- Access to a Google Cloud project with BigQuery and Cloud Storage
- A Muse API key stored in the `MUSE_API_KEY` environment variable

### 1. Launch Airbyte
```bash
cd airbyte
tar -xzf abctl-v0.19.0-linux-amd64.tar.gz
./abctl local install     # installs a local Airbyte instance
```

### 2. Start Airflow
```bash
cd ../airflow
docker-compose up -d   # starts the scheduler, webserver and dependencies
```
Use the helper script to run Airflow CLI commands:
```bash
./airflow.sh dags list
```

### 3. Run Spark Jobs
Preprocess local JSON dumps and load historical records into BigQuery:
```bash
cd ../sparkjob
spark-submit preprocessing_script.py
spark-submit process_historic_data.py
```

### 4. Trigger Pipelines
The repository contains two DAGs:
- `Daily_Job_Posting_Data_Management` – pulls new postings each day, loads them into BigQuery and runs dbt transformations.
- `Historic_Job_Posting_Data_Management` – ingests full historical datasets and writes them to BigQuery.

Trigger a DAG from the Airflow UI or via CLI:
```bash
./airflow.sh dags trigger Daily_Job_Posting_Data_Management
```

---

## Pipeline Components
### Airbyte
Manages source connectors and keeps configuration for repeatable ingestion of external APIs and files. The `abctl` CLI is bundled in the `airbyte` directory for local deployment.

### Airflow
DAGs reside under `airflow/dags` and encapsulate extraction, loading to GCS/BigQuery, and downstream dbt transformations. The `docker-compose.yaml` file provides a complete Airflow stack for local testing.

### Spark
The `sparkjob` folder contains lightweight Spark scripts used to clean and append historical datasets before loading them into BigQuery.

---

## Project Layout
```
Readme.md
airbyte/        # Airbyte CLI and configuration
airflow/        # Airflow project: docker-compose, dags and dbt models
sparkjob/       # Spark preprocessing and load scripts
```

---

## Technology Stack
- **Airbyte** – pluggable data ingestion
- **Apache Airflow** – workflow orchestration
- **Apache Spark** – batch processing for large JSON feeds
- **dbt** – SQL-based transformations in BigQuery
- **Google Cloud Storage / BigQuery** – raw and curated data storage
- **Python** – glue code and DAG logic

---

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.