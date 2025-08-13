# Data Pipeline for Optimizing Bike-Sharing Systems

## Project Objective
Enhance the operational efficiency of urban bike‑sharing programs by ingesting real‑time data from the NextBike API and translating it into actionable insights for better bike distribution and resource planning.

## Problem Statement
Bike-sharing networks lose revenue and frustrate customers when bikes and docks are unevenly distributed. Our real-time data pipeline detects imbalances as they happen and delivers actionable insights, enabling operators to rebalance efficiently, improve service, and cut costs.



## Architecture
1. **NextBike API** – fetch live station and bike data.
2. **Google Cloud Storage** – stage raw JSON dumps for durability.
3. **BigQuery** – transform and store cleaned data for analytics.
4. **Tableau** – visualize availability, demand trends, and station health.

## Data Pipeline
- **Extract:** `cloudDE.py` polls the NextBike API every minute and uploads the raw JSON to a GCS bucket.
- **Transform & Load:** `bigquerypipe.py` creates the BigQuery table if needed and streams structured data into it.
- **Visualize:** Tableau connects directly to BigQuery for live dashboards.

## Getting Started
### Prerequisites
- Python 3.10+
- Google Cloud project with BigQuery and Cloud Storage enabled
- Service account key with appropriate permissions

### Clone and Install
```bash
git clone https://github.com/Pavankumarmanagoli/Projects.git
cd "Projects/Data Pipeline Project for Optimizing Bike-Sharing Systems"
python3 -m venv .venv && source .venv/bin/activate
pip install google-cloud-bigquery google-cloud-storage requests schedule
```

### Configure Credentials
```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service_account_key.json
```

### Run the Pipeline
1. **Ingest to Cloud Storage**
   ```bash
   python cloudDE.py
   ```
2. **Load into BigQuery**
   ```bash
   python bigquerypipe.py
   ```

## Visualizations
Interactive dashboards built in Tableau highlight:
- real-time bike availability
- station usage maps
- demand trends and peak hours

## Tech Stack
NextBike API · Python · Google Cloud Storage · Google BigQuery · Tableau

## Future Work
- Integrate weather and event data for improved demand forecasting.
- Extend analytics to additional cities and mobility modes.

## License
Released under the MIT License.