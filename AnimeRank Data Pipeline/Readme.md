# AnimeRank Data Pipeline

This project demonstrates a production-style data pipeline that collects and organizes information on the top ranked anime titles. The pipeline scrapes multiple sources, transforms the raw data, and loads the results into a MySQL database for analysis.

## Table of Contents
- [Overview](#overview)
- [Environment and Architecture](#environment-and-architecture)
- [Web Scraping](#web-scraping)
- [ETL Process](#etl-process)
- [Database Design](#database-design)
- [Tech Stack](#tech-stack)
- [Future Work](#future-work)
- [License](#license)

## Overview
- Deployed a Docker Swarm cluster running Hadoop and Spark.
- Scraped anime information with Scrapy and BeautifulSoup.
- Built a Python-based ETL workflow for cleaning and standardizing data.
- Loaded curated records into MySQL for downstream analytics.

**Key Highlights**
- Distributed architecture capable of scaling across nodes.
- Extraction of 1000+ top anime entries from several websites.
- Database schema optimized for fast analytical queries.

## Environment and Architecture
The pipeline runs on a Hadoop-Spark cluster orchestrated with Docker Swarm across four Ubuntu virtual machines connected via Tailscale VPN.

1. **VPN** – Joined the VMs using Tailscale to enable secure communication.
2. **Cluster Setup** – Initiated Docker Swarm with one master and three worker nodes.
3. **Deployment** – Used `docker-compose` for persistent volumes and network configuration.
4. **Python Environment** – Created a virtual environment on the master node with all dependencies.

## Web Scraping
Data was collected from leading anime resources:

- **MyAnimeList** – Top 1000 anime including titles, genres, rankings, and scores.
- **Anime News Network** – Cover art and promotional images.
- **AniDB** – Episode counts, ratings, and user feedback.

Scraping was accomplished with Scrapy for large-scale crawling and BeautifulSoup for parsing complex HTML elements such as image tags.

## ETL Process
1. **Extract** – Moved raw scrape outputs from the master node into HDFS.
2. **Transform** – Python scripts standardized field formats, resolved missing values, and conformed data to the database schema.
3. **Load** – Inserted cleaned records into MySQL with optimized SQL statements.

## Database Design
MySQL stores the curated datasets for exploration and reporting.

- `anime_info` – Core attributes such as title, rank, and genre.
- `anime_ratings` – Average ratings, reviews, and likes.
- `anime_images` – Links to cover images.
- `anime_episodes` – Episode counts and release information.

Remote access is enabled for both the Docker deployment and local development via MySQL Workbench.

## Tech Stack
| Framework/Tool | Purpose |
| --- | --- |
| Python | ETL scripting |
| Scrapy | Web scraping |
| BeautifulSoup | HTML parsing |
| Hadoop (HDFS) | Distributed storage |
| Apache Spark | Data processing |
| Docker Swarm | Cluster orchestration |
| MySQL | Structured data storage |
| Tailscale VPN | Secure networking |

## Future Work
- Real-time updates through public APIs.
- Interactive dashboards with Power BI or Tableau.
- Basic recommendation model for personalized anime suggestions.
- Authentication layers to harden API and database access.

## License
This project is licensed under the MIT License.