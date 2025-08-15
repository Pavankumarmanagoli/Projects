# Walmart Sales Analytics Pipeline with Azure Databricks

In this project, data is extracted in batches using **Azure Data Factory** and transformed with **Apache Spark** in **Azure Databricks**. The transformed data is stored in **Azure Synapse Analytics** in a columnar format. Finally, a dashboard is created using  Power BI. As a result of this project, fresh food has become the top category, supporting the decision to promote these items in more visible locations and on the website or application. The most popular fresh food is MorningStar Farms Veggie Burgers, with customers picking up a total of 184 units daily. With this information, the company is able to contact MorningStar Farms to order more products and discuss pricing options. For more information about the data source, see [here](https://www.kaggle.com/datasets/thedevastator/product-prices-and-sizes-from-walmart-grocery).

## Project Overview

This repository demonstrates an end-to-end analytics pipeline for Walmart sales data:

- Data ingestion with **Azure Data Factory**
- Data transformation with **Apache Spark** on **Azure Databricks**
- Storage and querying in **Azure Synapse Analytics**
- Interactive dashboards built with **Looker Studio** or **Power BI**

![0](/images/0.png)

## Tech Stack

- Azure Data Factory
- Azure Databricks (Apache Spark)
- Azure Data Lake Storage Gen2
- Azure Synapse Analytics
- Looker Studio / Power BI

## Getting Started

Clone the repository and navigate to this project directory:

```bash
git clone https://github.com/Pavankumarmanagoli/Projects.git
cd "Projects/Walmart Sales Analytics Pipeline with Azure Databricks"
```

The `Wallmart.ipynb` notebook contains the Spark transformations executed in Azure Databricks. Follow the steps in the [Contents](#contents) section to provision resources and run the pipeline.

## Contents
[Create Storage Account](sections/01-storage-accounts.md).<br>
- [Azure Blob Storage](sections/01-storage-accounts.md#Create-Azure-Blob-Storage).<br>
- [Azure Data Lake Storage Gen2](sections/01-storage-accounts.md#Create-Azure-Data-Lake-Storage-Gen2).<br>

[Create Azure Data Factory](sections/02-azure-data-factory.md#Create-Azure-Data-Factory).<br>
- [Create Linked Services](sections/02-azure-data-factory.md#Create-Linked-Services).<br>
  - [Source Linked Services](sections/02-azure-data-factory.md#Source-Linked-Services).<br>
  - [Sink Linked Services](sections/02-azure-data-factory.md#Sink-Linked-Services).<br>
  - [Databricks Linked Services](sections/02-azure-data-factory.md#Databricks-Linked-Services).<br>

- [Create Dataset](sections/02-azure-data-factory.md#Create-Dataset).<br>
  - [Dataset of Azure Blob Storage](sections/02-azure-data-factory.md#Dataset-of-Azure-Blob-Storage).<br>
  - [Dataset of Azure Data Lake Storage Gen2](sections/02-azure-data-factory.md#Dataset-of-Azure-Data-Lake-Storage-Gen2).<br>
- [Extract data using Azure Data Factory](sections/02-azure-data-factory.md#Extract-data-using-Azure-Data-Factory).<br>

[Create Azure Databricks Services](sections/03-azure-databricks.md#Create-Azure-Databricks-Services).<br>
- [Create Cluster](sections/03-azure-databricks.md#Create-Cluster).<br>
- [Mounting Data Lake Storage](sections/03-azure-databricks.md#Mounting-Data-Lake-Storage).<br>
- [Using Databricks to transform data](sections/03-azure-databricks.md#Using-Databricks-to-transform-data).<br>
- [Run Databricks Notebook using Azure Data Factory](sections/03-azure-databricks.md#Run-Databricks-Notebook-using-Azure-Data-Factory).<br>

[Create Synapse Analytics workspace](sections/04-synapse-analytics.md#Create-Synapse-Analytics-workspace).<br>
- [Create Lake database](sections/04-synapse-analytics.md#Create-Lake-database).<br>
- [Create Table from data lake](sections/04-synapse-analytics.md#Create-Table-from-data-lake).<br>
- [Query data on Azure Synapse Analytics](sections/04-synapse-analytics.md#Query-data-on-Azure-Synapse-Analytics).<br>

[Import Azure Synapse Analytics (SQL DW) Data into the Power BI](sections/05-power-bi.md#).<br>
- [Connect to a data source in Power BI](sections/05-power-bi.md#Connect-to-a-data-source-in-Power-BI).<br>
- [Creating Data visualizations](sections/05-power-bi.md#Creating-Data-visualizations).<br>
