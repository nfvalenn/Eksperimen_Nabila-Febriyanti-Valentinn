import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

def load_data(input_path):
    print(f"Loading data from {input_path}...")
    return pd.read_csv(input_path)

def preprocess_data(df):
    df_clean = df[(df['Age'] >= 18) & (df['Age'] <= 65)].copy()

    drop_cols = ['comments', 'state', 'Timestamp', 'Country']
    df_clean = df_clean.drop(columns=[col for col in drop_cols if col in df_clean.columns], errors='ignore')

    categorical_columns = df_clean.select_dtypes(include=['object', 'category']).columns
    numerical_columns = df_clean.select_dtypes(include=['int64', 'float64']).columns

    df_clean.loc[:, categorical_columns] = df_clean[categorical_columns].fillna('Unknown')

    for col in numerical_columns:
        median = df_clean[col].median()
        df_clean.loc[:, col] = df_clean[col].fillna(median)

    le = LabelEncoder()
    for col in categorical_columns:
        df_clean.loc[:, col] = le.fit_transform(df_clean[col])

    scaler = StandardScaler()
    if 'Age' in df_clean.columns:
        df_clean.loc[:, 'Age'] = scaler.fit_transform(df_clean[['Age']])

    return df_clean

def save_data(df, output_path):
    output_dir = os.path.dirname(output_path)
    if output_dir != '':
        os.makedirs(output_dir, exist_ok=True)

    df.to_csv(output_path, index=False)
    print(f"Preprocessed dataset saved to {output_path}")

if __name__ == "__main__":
    input_file = "survey.csv"
    output_file = "mental_health_cleaned.csv"

    df = load_data(input_file)
    df_clean = preprocess_data(df)
    save_data(df_clean, output_file)
