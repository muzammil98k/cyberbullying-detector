import pandas as pd

def load_dataset(path="data/train.csv"):
    try:
        df = pd.read_csv(path)
        print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
        print("Sample rows:")
        print(df.head())
        return df
    except FileNotFoundError:
        print("Dataset not found. Please download and place it in the `data/` folder.")
        return None

if __name__ == "__main__":
    df = load_dataset()
