import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load and process metadata
def load_and_process_metadata(file_path):
    # Load CSV into DataFrame with headers
    metadata_raw = pd.read_csv('/content/Metadata.csv', header=None, names=['RawData'])


    # Extract date, time, description, value from raw data
    metadata_processed = extract_metadata(metadata_raw)

    # Convert 'Value' to numerical and filter valid entries
    metadata_processed = convert_and_filter(metadata_processed)

    # Categorize descriptions into meaningful categories
    metadata_processed['Category'] = metadata_processed['Description'].apply(categorize_description)

    return metadata_processed

# Function to extract date, time, description, value
def extract_metadata(metadata_raw):
    dates, times, descriptions, values = [], [], [], []
    current_date, current_time = None, None

    for row in metadata_raw['RawData']:
        if len(row.split('.')) == 3 and row.count('.') == 2:
            current_date = row.strip()
        elif len(row.split(':')) == 3 and row.count(':') == 2:
            current_time = row.strip()
        else:
            parts = row.split()
            if len(parts) >= 3:
                description = ' '.join(parts[:-2])
                value = parts[-2] + ' ' + parts[-1]
                dates.append(current_date)
                times.append(current_time)
                descriptions.append(description)
                values.append(value)

    structured_data = pd.DataFrame({
        'Date': dates,
        'Time': times,
        'Description': descriptions,
        'Value': values
    })

    return structured_data

# Function to convert 'Value' to numerical and filter valid entries
def convert_and_filter(metadata_processed):
    metadata_processed['NumericalValue'] = metadata_processed['Value'].str.extract(r'([-+]?\d*\.\d+|\d+)', expand=False).astype(float)
    metadata_processed.dropna(subset=['NumericalValue'], inplace=True)
    metadata_processed = metadata_processed[metadata_processed['Date'].str.match(r'\d{2}\.\d{2}\.\d{4}') & 
                                            metadata_processed['Time'].str.match(r'\d{2}:\d{2}:\d{2}')]
    metadata_processed['DateTime'] = pd.to_datetime(metadata_processed['Date'] + ' ' + metadata_processed['Time'], format='%d.%m.%Y %H:%M:%S')
    metadata_processed.set_index('DateTime', inplace=True)

    return metadata_processed

# Function to categorize description into predefined categories
def categorize_description(desc):
    categories = {
        'Druck': 'Pressure', 'Pressure': 'Pressure',
        'Temperatur': 'Temperature', 'Temperature': 'Temperature',
        'Geschwindigkeit': 'Speed', 'Speed': 'Speed',
        'Leistung': 'Power', 'Power': 'Power',
        'Kraft': 'Force', 'Force': 'Force',
        'Strom': 'Current', 'Current': 'Current',
        'Drehmoment': 'Torque', 'Torque': 'Torque',
        'Durchmesser': 'Diameter', 'Diameter': 'Diameter'
    }
    for key in categories:
        if key in desc:
            return categories[key]
    return 'Other'

# Function to plot boxplot for each category
def plot_boxplot(metadata_processed):
    plt.figure(figsize=(15, 10))
    sns.boxplot(x='Category', y='NumericalValue', data=metadata_processed)
    plt.title('Box Plot of Numerical Values by Category')
    plt.xlabel('Category')
    plt.ylabel('Numerical Value')
    plt.xticks(rotation=45)
    plt.show()

# Main execution
if __name__ == '__main__':
    file_path = '/content/Metadata.csv'
    structured_metadata = load_and_process_metadata(file_path)
    plot_boxplot(structured_metadata)
