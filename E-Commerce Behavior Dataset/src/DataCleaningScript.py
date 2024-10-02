import pandas as pd 
import os 

RAW_DATA_PATH = 'E-Commerce Behavior Dataset/data/raw/2019-Oct.csv'
CLEANED_DATA_PATH = 'E-Commerce Behavior Dataset/data/cleaned/cleaned_data.csv'


def load_raw_data():
    return pd.read_csv(RAW_DATA_PATH)

def clean_data(df):

    #Dropping Duplicate Rows
    df.drop_duplicates(inplace=True)

    #Dropping all the null values
    df = df.dropna().copy()

    #Convert event_time column into datetime
    df['event_time'] = pd.to_datetime(df['event_time'], utc=True, errors='coerce')

    return df


def save_cleaned_data(df):
    os.makedirs(os.path.dirname(CLEANED_DATA_PATH), exist_ok=True)
    df.to_csv(CLEANED_DATA_PATH, index=False)


if __name__ == '__main__':
    raw_data = load_raw_data()
    cleaned_data = clean_data(raw_data)
    save_cleaned_data(cleaned_data)


    print("Data has been cleaned and saved!")