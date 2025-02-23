# 🎉 Data Engineering Project: AnimeRank Data & ETL Pipeline

This repository documents a comprehensive **Data Engineering Project** focused on building a distributed environment to **scrape anime data**, perform **ETL operations**, and store the structured data in a **MySQL database**. The primary goal is to gather, process, and organize information about the **top-ranked anime** from multiple sources for data analysis.

---

## 📚 Table of Contents
- [🚀 Project Overview](#-project-overview)
- [⚙️ Environment Setup](#️-environment-setup)
- [🕸️ Web Scraping](#️-web-scraping)
- [🛠️ ETL Process](#️-etl-process)
- [💾 Database Design](#-database-design)
- [📈 Future Enhancements](#-future-enhancements)
- [💡 Tech Stack](#-tech-stack)
- [📄 License](#-license)

---

## 🚀 Project Overview

This project involves:
- Setting up a **Hadoop-Spark Cluster** using Docker Swarm.
- Scraping anime data from multiple sources using **Scrapy** and **BeautifulSoup**.
- Building an end-to-end **ETL pipeline** for data cleaning and transformation.
- Storing the processed data in a **MySQL database** for querying and analysis.

**✨ Key Features:**
- Scalable Distributed System using Hadoop & Spark
- Extraction of 1000+ top anime records from multiple sources
- Structured data storage optimized for analytics

---

## ⚙️ Environment Setup

To build a scalable and fault-tolerant environment, a **Hadoop-Spark cluster** was set up using **Docker Swarm** across multiple **Ubuntu Virtual Machines (VMs)** connected via **Tailscale VPN**.

### ✅ **Steps Taken:**
1. **VPN Setup:** Connected 4 Ubuntu VMs via **Tailscale VPN** for secure communication.
2. **Docker Swarm Initialization:**  
   - One VM as **Master Node**  
   - Three VMs as **Worker Nodes**
3. **Container Orchestration:**  
   - Created a **Docker Compose** file for cluster deployment, persistent storage, and container networking.
4. **Cluster Deployment:**  
   - Installed a **Hadoop-Spark** cluster on the Swarm using the Docker Compose file.
5. **Python Environment:**  
   - Set up a **Python Virtual Environment** on the master node with required dependencies.

---

## 🕸️ Web Scraping

The project utilized **Scrapy** and **BeautifulSoup** for efficient and accurate web scraping from popular anime websites.

### 📋 **Sources & Data Collected:**
1. **[MyAnimeList](https://myanimelist.net/topanime.php?limit=0)**  
   - Extracted top **1000 anime** and captured ~26 features (title, genre, rank, score, etc.).

2. **[Anime News Network](https://www.animenewsnetwork.com/encyclopedia/ratings-anime.php?top50=best_bayesian&n=500)**  
   - Scraped **anime images** and cover arts.

3. **[AniDB](https://anidb.net/anime/)**  
   - Collected data on episodes, average ratings, user reviews, and the number of users who liked each anime.

### 🛠️ **Scraping Tools Used:**
- [Scrapy](https://scrapy.org/) — for efficient large-scale scraping.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) — for handling complex HTML structures (e.g., image extraction).

---

## 🛠️ ETL Process

The **Extract, Transform, Load (ETL)** pipeline was designed to process and clean the scraped data before storing it in a **MySQL database**.

### 📈 **ETL Workflow:**
1. **Extraction:**  
   - Transferred raw scraped data from the master node to **Hadoop Distributed File System (HDFS)**.

2. **Transformation:**  
   - Developed a **Python script** to:
     - Load data from **HDFS**
     - Clean and standardize data formats
     - Handle missing values and duplicates
     - Align data with the **database schema**

3. **Loading:**  
   - Inserted the cleaned data into the **MySQL database** using optimized SQL queries.

---

## 💾 Database Design

The **MySQL database** was configured to store structured anime data for further analysis.

### 🗄️ **Database Setup:**
1. Installed **MySQL** on an Ubuntu VM.
2. Configured system files to allow **remote access** for querying and ETL operations.
3. Created two distinct user accounts:
   - **Docker Master-Node Deployment**  
   - **Local Access via MySQL Workbench**

### 🗃️ **Key Tables:**
- **`anime_info`** – Basic anime details (title, rank, genre, etc.)
- **`anime_ratings`** – Average ratings, user reviews, likes
- **`anime_images`** – URLs to anime cover images
- **`anime_episodes`** – Episode count, release dates, etc.

---

## 📈 Future Enhancements

- **🔄 Real-Time Data Updates:** Implement APIs for continuous data refresh.
- **📊 Data Visualization:** Use **Power BI**/**Tableau** for visual analytics.
- **💡 Recommendation System:** Build a basic ML model for anime recommendations.
- **🛡️ Enhanced Security:** Set up authentication for API and database layers.

---

## 💡 Tech Stack

| 🏗️ **Framework/Tool** | 💡 **Purpose**                         |
|-----------------------|---------------------------------------|
| **Python**            | Data wrangling, ETL scripting        |
| **Scrapy**            | Web scraping                         |
| **BeautifulSoup**     | HTML parsing for complex data        |
| **Hadoop (HDFS)**     | Distributed data storage             |
| **Apache Spark**      | Data processing and transformation   |
| **Docker Swarm**      | Cluster orchestration                |
| **MySQL**             | Structured data storage              |
| **Tailscale VPN**     | Secure VM networking                 |

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

### 🚀 **Happy Data Engineering!**

Feel free to contribute to this project by submitting pull requests or raising issues. For any queries, reach out via [GitHub Issues](https://github.com/).

