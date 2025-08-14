 Wind Energy Analysis and Forecasting with Deep Learning

## Project Objective

This project analyzes wind turbine sensor data and forecasts future power output using a Long Short-Term Memory (LSTM) neural network. Accurate power predictions help wind farm operators plan energy production and improve grid reliability.

## Dataset

The `dataset/T1.csv` file contains historical measurements from a single turbine, including wind speed, wind direction, ambient conditions, and actual power generation. These features are used to train and evaluate the forecasting model.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Pavankumarmanagoli/Projects.git
cd Projects/"Wind Energy Analysis and Forecast using Deep Learning"
```

### Install Dependencies

This project requires Python 3.8+ and the following libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow
```

### Run the Notebook

Launch Jupyter Notebook and open the analysis notebook:

```bash
jupyter notebook "Wind Energy Analysis and Prediction using LSTM .ipynb"
```

Run all cells to reproduce the exploratory analysis, train the LSTM model, and generate power forecasts.

## Key Visualizations

### Correlation Heatmap
![download (1)](https://user-images.githubusercontent.com/48255425/86516148-d5f25d80-be3b-11ea-9bdc-d414a3d29b73.png)
The heatmap shows relationships between features. Wind direction has little correlation with turbine power.

### Wind Direction vs. Wind Speed (Windrose)
![download (14)](https://user-images.githubusercontent.com/48255425/86516118-a9d6dc80-be3b-11ea-802d-bc78664d5ec8.png)

### Kernel Density Estimate
![download (15)](https://user-images.githubusercontent.com/48255425/86516193-1ce05300-be3c-11ea-837d-8554dcd01672.png)
Univariate and bivariate KDE plots describe the distribution of features.

### Date/Time vs. Wind Power
![__results___22_0](https://user-images.githubusercontent.com/48255425/86529697-74300300-bed0-11ea-82ee-81074baaf28a.png)

## Results

![__results___48_0](https://user-images.githubusercontent.com/48255425/86529699-75f9c680-bed0-11ea-86c6-cb59d6e531ad.png)

The trained LSTM model achieves approximately 96% forecasting accuracy. Increasing the number of training epochs may further improve performance.

## Project Structure

- `dataset/T1.csv` – raw turbine data.
- `Wind Energy Analysis and Prediction using LSTM .ipynb` – exploratory analysis and model training notebook.
- `_config.yml` – configuration for GitHub Pages (if used).
- `README.md` – project documentation.

## Contributing

Contributions and suggestions are welcome. Feel free to fork the repository, open issues, or submit pull requests to improve the analysis or extend the model.
