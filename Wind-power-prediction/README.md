[# Wind Speed Prediction using Interpretable Stacking Ensemble Machine Learning Algorithms

![Wind Speed Prediction](https://erepublic.brightspotcdn.com/dims4/default/16d0978/2147483647/strip/true/crop/4670x2435+0+282/resize/840x438!/quality/90/?url=http%3A%2F%2Ferepublic-brightspot.s3.amazonaws.com%2F01%2F8a%2F19eb46354206853cb37788374e41%2Fshutterstock-1454940068-1.jpg)

Forecast wind power output from meteorological features using a stacking ensemble of machine learning algorithms. The project combines multiple learners to deliver accurate and explainable predictions.

## Project Objective
- Develop an accurate model for wind power forecasting.
- Leverage ensemble learning to improve performance over single estimators.
- Explain model behaviour using SHAP feature attributions.

## Repository Structure
| File | Description |
| --- | --- |
| `Total_code_wind.ipynb` | End-to-end workflow for data preparation, model training, and evaluation. |
| `SHAP_Values_wind.ipynb` | Generates SHAP values and plots for interpreting model predictions. |

## Clone and Setup
```bash
git clone https://github.com/Pavankumarmanagoli/Projects.git
cd Projects/Wind-power-prediction
python -m venv .venv && source .venv/bin/activate  # On Windows use .venv\Scripts\activate
pip install numpy pandas scikit-learn catboost shap matplotlib
```

## Usage
1. Launch Jupyter:
   ```bash
   jupyter lab  # or jupyter notebook
   ```
2. Open `Total_code_wind.ipynb` to train and evaluate the stacking model.
3. Run `SHAP_Values_wind.ipynb` to analyse feature importance.

## Evaluation Metrics
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **R-squared (R²)**

## Results
The stacking model achieved **RMSE 0.306**, **MAE 0.228**, and **R² 0.97** on the test set. SHAP analysis shows that `WS10M_MIN` and `WS10M_MAX` are the most influential features in the predictions.

## Conclusion
Stacking ensemble learning, combined with SHAP-based interpretation, provides a robust and transparent approach for wind power forecasting.
