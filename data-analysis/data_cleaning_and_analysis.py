import pandas as pd
import numpy as np
import os

#Ask the user to input the file path
file_path = input("Enter the full path of the CSV file (e.g. C:\\Users\\ALIENWARE\\Desktop\\2nd Sem\\Stats&Prob\\Assignment_2\\MobilesDataset.csv): ").strip()

#Check if the file exists
if not os.path.exists(file_path):
    print("Error: File not found! Check the file path.")
else:
    #Load the dataset with error handling
    try:
        df = pd.read_csv(file_path, encoding="latin1", on_bad_lines="skip")
        print("\nDataset loaded successfully!")
    except Exception as e:
        print("Error reading the CSV file:", e)
        df = None  #Prevent further errors if loading fails

    if df is not None:
        #Display basic info
        print("\nDataset Info:")
        print(df.info(memory_usage="deep"))

        print("\nFirst 5 Rows:")
        print(df.head())

        #Handle missing values
        before = df.shape[0]
        df = df.dropna()
        print(f"\nRemoved {before - df.shape[0]} rows with missing values.")

        #Basic statistical summary
        print("\nSummary Statistics:")
        print(df.describe())

        #Check and remove duplicate rows
        before = df.shape[0]
        df = df.drop_duplicates()
        print(f"\nRemoved {before - df.shape[0]} duplicate rows.")

        #Insights Section
        print("\n=== INSIGHTS ===")

        #Find correlation with price (if applicable)
        if "price" in df.columns:
            top_corr = df.corr()["price"].dropna().sort_values(ascending=False)
            print("\nTop Correlated Features with Price:")
            print(top_corr)

            #Identify strongest positive & negative correlation
            most_positive_corr = top_corr.index[1] if len(top_corr) > 1 else None
            most_negative_corr = top_corr.index[-1] if len(top_corr) > 1 else None
            
            print(f"\nFeature most positively correlated with price: {most_positive_corr}")
            print(f"Feature most negatively correlated with price: {most_negative_corr}")

        #Identify outliers using IQR method
        print("\nDetecting Outliers...")
        numeric_cols = df.select_dtypes(include=["number"]).columns
        outlier_counts = {}

        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))][col]
            outlier_counts[col] = len(outliers)

        outlier_counts = {k: v for k, v in outlier_counts.items() if v > 0}  # Filter out cols with no outliers
        if outlier_counts:
            print("Columns with outliers detected:")
            for col, count in outlier_counts.items():
                print(f"{col}: {count} outliers")
        else:
            print("No significant outliers detected.")

        #Identify skewness in numerical distributions
        print("\nChecking Data Skewness:")
        skewed_cols = df[numeric_cols].skew().sort_values(ascending=False)
        print(skewed_cols)

        highly_skewed = skewed_cols[abs(skewed_cols) > 1]
        if not highly_skewed.empty:
            print("\nHighly Skewed Columns (>|1| skewness):")
            print(highly_skewed)

        #Find most frequent category for each categorical column
        print("\nMost Frequent Values in Categorical Columns:")
        categorical_cols = df.select_dtypes(include=["object"]).columns

        for col in categorical_cols:
            most_frequent = df[col].mode()[0]
            print(f"{col}: Most frequent value = {most_frequent}")

        #Convert categorical data into numerical format using factorization
        for col in categorical_cols:
            df[col] = pd.factorize(df[col])[0]

        #Compute mean and median for numerical columns
        print("\nMean Values:")
        print(df.mean())

        print("\nMedian Values:")
        print(df.median())

        #Save cleaned dataset in the same directory as the original file
        output_path = os.path.join(os.path.dirname(file_path), "cleaned_data.csv")
        df.to_csv(output_path, index=False)
        print(f"\nCleaned dataset saved at: {output_path}")
