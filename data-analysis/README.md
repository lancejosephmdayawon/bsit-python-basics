# Mobile Dataset Analysis Tool

## Overview

A Python-based data analysis tool designed to clean, analyze, and extract insights from mobile phone datasets. This script provides comprehensive statistical analysis, correlation studies, outlier detection, and data quality assessment for smartphone specifications and pricing data.

## Features

### 1. **Interactive File Loading**

- User-friendly file path input system
- File existence validation
- Error handling for file reading issues
- Support for various CSV encodings (latin1)

### 2. **Data Cleaning Pipeline**

- **Missing Value Handling**: Automatically detects and removes rows with null values
- **Duplicate Removal**: Identifies and eliminates duplicate entries
- **Data Type Conversion**: Converts categorical variables to numerical format for analysis
- **Quality Reports**: Provides before/after statistics for data cleaning operations

### 3. **Statistical Analysis**

- **Descriptive Statistics**: Mean, median, standard deviation, min/max values
- **Distribution Analysis**: Skewness detection for understanding data distribution patterns
- **Correlation Analysis**: Identifies relationships between features and price
- **Frequency Analysis**: Finds most common values in categorical columns

### 4. **Outlier Detection**

- Implements **IQR (Interquartile Range) method** for robust outlier detection
- Identifies outliers in all numerical columns
- Provides detailed count of outliers per feature

### 5. **Feature Correlation**

- Calculates correlation coefficients with price columns
- Identifies strongest positive and negative correlations
- Helps understand which features most impact pricing

### 6. **Automated Output**

- Saves cleaned dataset to the same directory as source file
- Preserves original data while creating cleaned version
- Names output file consistently as `cleaned_data.csv`

## Requirements

```
pandas>=1.3.0
numpy>=1.21.0
```

Install dependencies using:

```bash
pip install pandas numpy
```

## Usage

### Basic Execution

```bash
python mobile_analysis.py
```

### Input Format

When prompted, enter the full path to your CSV file. Look at the example below:

```
Enter the full path of the CSV file: C:\Users\LanceJosephDayawon\Desktop\MobilesDataset.csv
```

### Expected Dataset Structure

The script is optimized for mobile phone datasets with columns such as:

- Company Name
- Model Name
- Mobile Weight
- RAM
- Front Camera
- Back Camera
- Processor
- Battery Capacity
- Screen Size
- Launched Price (various regions)
- Launched Year

## Output Examples

### Console Output

```
Dataset loaded successfully!

Dataset Info:
<class 'pandas.core.frame.DataFrame'>
...

Removed 15 rows with missing values.
Removed 3 duplicate rows.

=== INSIGHTS ===

Top Correlated Features with Price:
price                    1.000000
battery_capacity         0.682341
ram                      0.654123
screen_size              0.543210
...

Feature most positively correlated with price: battery_capacity
Feature most negatively correlated with price: launched_year

Detecting Outliers...
Columns with outliers detected:
price: 23 outliers
battery_capacity: 12 outliers

Highly Skewed Columns (>|1| skewness):
price              2.341
battery_capacity   1.456
```

### File Output

- **cleaned_data.csv**: Processed dataset with missing values removed, duplicates eliminated, and categorical variables encoded

## Technical Implementation

### Data Cleaning Process

1. **Load CSV** with error handling and encoding support
2. **Remove null values** across all columns
3. **Eliminate duplicates** based on all columns
4. **Encode categorical variables** using pandas factorization

### Statistical Methods

- **IQR Method**: `Q1 - 1.5*IQR` to `Q3 + 1.5*IQR` for outlier boundaries
- **Pearson Correlation**: Default correlation method for linear relationships
- **Skewness Calculation**: Using pandas `.skew()` method with threshold of |1|

### Encoding Strategy

Categorical columns are converted using `pd.factorize()`:

- Assigns unique integer to each category
- Maintains consistency across the dataset
- Enables numerical operations on categorical data

## Key Insights Generated

1. **Price Correlation Analysis**

   - Identifies which features (RAM, battery, camera) most impact price
   - Reveals both positive and negative correlations

2. **Data Quality Metrics**

   - Quantifies missing data
   - Reports duplicate entries
   - Assesses overall dataset cleanliness

3. **Distribution Patterns**

   - Detects skewed features that may need transformation
   - Identifies outlier-prone columns

4. **Categorical Patterns**
   - Most popular brands, processors, or configurations
   - Market trends based on frequency analysis

## Limitations & Considerations

- **Data Loss**: `dropna()` removes entire rows with any missing value (aggressive approach)
- **Encoding**: Factorization creates ordinal relationships that may not reflect true categorical nature
- **No Visualization**: Currently text-based output only
- **Single Price Column**: Assumes one "price" column; multiple regional prices require modification

## Use Cases

- **Data Science Portfolio**: Demonstrates data cleaning and EDA skills
- **Market Research**: Analyze mobile phone pricing strategies
- **Consumer Analysis**: Understand feature-price relationships
- **Quality Assurance**: Validate dataset completeness and consistency
- **Academic Projects**: Statistical analysis and data preprocessing

## Author Notes

This script demonstrates fundamental data science skills including:

- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- Statistical analysis and interpretation
- Error handling and user interaction
- File I/O operations

Designed as a reusable template for CSV-based analysis projects with minimal modifications needed for different datasets.

## License

This project is available for educational and portfolio purposes.

---

Author
Lance Joseph Dayawon
lancejosepmdayawon@gmail.com
