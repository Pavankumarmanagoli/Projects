# 📊Ireland Job Market Analytics Pipeline

This repository documents a comprehensive **ELT (Extract, Load, Transform)** pipeline for collecting, managing, and analyzing **job posting data** from various sources. The project showcases a fully automated and scalable data workflow that utilizes **Google BigQuery**, **dbt**, **Airflow**, and **Looker** for end-to-end data management and visualization.

---

## 📚 Table of Contents

- [🚀 Project Overview](#-project-overview)
- [🗄️ Data Sources](#️-data-sources)
- [⚙️ Environment Setup](#️-environment-setup)
- [🔄 ELT Process](#-elt-process)
- [💾 Data Warehouse & Transformation](#-data-warehouse--transformation)
- [📈 Data Visualization](#-data-visualization)
- [⏰ Automation with Airflow](#-automation-with-airflow)
- [🎯 Goals & Outcomes](#-goals--outcomes)
- [💡 Tech Stack](#-tech-stack)
- [📄 License](#-license)

---

## 🚀 Project Overview

The primary objective of this project is to design and implement a **cloud-based, fully automated ELT pipeline** for processing and analyzing job postings data. The pipeline extracts data from **APIs** and **static datasets**, loads it into **BigQuery**, transforms it using **dbt**, and visualizes insights using **Looker**.

**✨ Key Features:**
- **Real-time & Historical Job Data Extraction**
- **Automated ELT Pipeline using Airflow**
- **Cloud-based Data Storage & Transformation (BigQuery, dbt)**
- **Interactive Dashboards (Looker)**

---

## 🗄️ Data Sources

The ELT pipeline integrates data from the following sources:

### 📡 **APIs:**
- **The Muse API** — Real-time job postings  
  - API Endpoint: `GET https://www.themuse.com/api/public/jobs`

### 📁 **Static Datasets:**
- **Job Data Feeds** — Historical job postings since 2020  
  - Dataset: [Job Data Overview](https://jobdatafeeds.com/job-data-overview)  
  - Format: **JSON**

### 📊 **Data Collected:**
- Job Titles
- Company Details
- Location
- Job Descriptions
- Posting Dates
- Historical Job Trends

---

## ⚙️ Environment Setup

The environment was designed for scalability, automation, and data integrity.

1. **Google Cloud Platform (GCP)** — Hosted BigQuery and storage buckets.
2. **dbt** — Managed SQL-based data transformations in BigQuery.
3. **Airflow** — Automated data extraction, loading, and transformation jobs.
4. **Looker** — Used for data visualization and dashboarding.

---

## 🔄 ELT Process

The **Extract, Load, Transform (ELT)** pipeline consists of the following stages:

### 🟢 **1. Extract:**
- Data pulled from **The Muse API** and **static datasets**.
- Both real-time and historical job data collected.

### 🟡 **2. Load:**
- Raw data loaded into **Google Cloud Storage (GCS)** buckets.
- Data moved into **BigQuery** as a central repository.

### 🔵 **3. Transform:**
- **dbt** used for data cleaning, standardization, and schema structuring:
  - **Datatype Conversion**
  - **Null Value Imputation**
  - **Unnesting of Array Fields**
  - **Incremental Data Filtering** for daily updates
  - **Union of Multiple Sources** for historical data

---

## 💾 Data Warehouse & Transformation

### **🔷 Google BigQuery:**
- Chosen for its **scalability**, **high-performance querying**, and **cost-efficiency**.
- Integration with GCP services allows seamless data flow.

### **🟡 dbt (Data Build Tool):**
- Modular and reusable SQL-based transformations.
- Supports **version control** using Git.
- Built-in **testing** and **data validation** features.
- Simplifies the transformation logic while leveraging BigQuery's compute power.

---

## 📈 Data Visualization

**Looker** was used for creating interactive dashboards and reports to visualize job market trends.

### 📊 **Dashboards Include:**
- **Top Job Sectors** by location
- **Hiring Trends** over time
- **Salary Analysis** across industries
- **Popular Skills** required by employers

---

## ⏰ Automation with Airflow

**Apache Airflow** was utilized to orchestrate the ELT pipeline.

### 🔄 **Airflow Jobs:**
- **Daily Job Posting Pipeline:**  
  - Incremental extraction of new job postings.
  - Data stored in a **Daily Job Posting** dataset.

- **Historic Job Posting Pipeline:**  
  - Full data extraction for historical analysis.
  - Data stored in a **Historic Job Posting** dataset.

### ⚡ **Airflow Features Implemented:**
- **Task Scheduling** — Automated daily and historic data runs.
- **Error Handling** — Built-in error detection and retry mechanisms.
- **Scalable Workflows** — DAGs optimized for scalability and performance.

---

## 🎯 Goals & Outcomes

### 🎯 **Goals:**
- Build a **fully automated** data pipeline.
- Implement **scalable data transformations** using cloud resources.
- Create **accessible data insights** for end-users.
- Develop a **reusable ELT pipeline** for similar data projects.

### 🏆 **Outcomes:**
- Achieved a **cloud-based, automated ELT pipeline**.
- Enhanced **data accessibility** through Looker dashboards.
- Optimized data transformations using **dbt** and **BigQuery**.
- Built a **robust orchestration system** using Airflow.

---

## 💡 Tech Stack

| 🏗️ **Tool/Framework** | 💡 **Purpose**                     |
|-----------------------|-----------------------------------|
| **Google BigQuery**    | Data warehousing & storage       |
| **dbt**                | Data transformation (SQL-based)  |
| **Apache Airflow**     | Workflow orchestration           |
| **Looker**             | Data visualization & reporting   |
| **Google Cloud Storage** | Raw data storage               |
| **Python**             | Data extraction scripts          |
| **APIs & Static Datasets** | Data sources                  |

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

### 🚀 **Happy Data Engineering!**
