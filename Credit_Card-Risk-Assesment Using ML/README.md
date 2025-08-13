# Credit Card Risk Assessment Using Machine Learning

This repository demonstrates an end‑to‑end machine learning workflow for estimating the probability that a credit card client will default on their payment. The project highlights how data‑driven techniques can support credit risk evaluation and assist financial institutions in making informed lending decisions.

## Project Structure
- `Credit Card Risk Assessment.ipynb` – Jupyter Notebook containing the full analysis and model training pipeline.
- `Credit_default_dataset.csv` – dataset of historical credit card customers and default behavior.

## Dataset
The dataset includes more than 30,000 anonymized credit card clients with attributes such as payment history, bill statements, credit limits and demographic details. It originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients).

## Installation
Clone the repository and install the required packages:

```bash
git clone https://github.com/Pavankumarmanagoli/Projects.git
cd "Projects/Credit_Card-Risk-Assesment Using ML"
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Usage
Launch Jupyter Notebook and open the analysis:

```bash
jupyter notebook "Credit Card Risk Assessment.ipynb"
```

Run the notebook cells sequentially to reproduce the preprocessing, modeling and evaluation steps.

## Methodology
1. **Data preprocessing** – handle missing values and outliers, encode categorical variables and scale features.
2. **Exploratory data analysis** – visualize distributions and trends associated with default risk.
3. **Model development** – train classification algorithms (e.g., Logistic Regression, Random Forest) and evaluate with accuracy, precision, recall, F1‑score and AUC‑ROC.
4. **Risk scoring** – assign a probability of default to each customer and highlight the factors that most influence risk.

## Insights
- Customers with high credit utilization and frequently late payments show a higher probability of default.
- Payment history, bill amounts and recent payments are among the strongest predictors of risk.

## Contributing
Contributions, issues and feature requests are welcome. Feel free to fork the repository and open a pull request.

## Acknowledgments
Dataset: “Default of Credit Card Clients,” UCI Machine Learning Repository.