import pandas as pd

BENIGN_PATH = 'Data/CSV_benign.csv'
MALWARE_PATH = 'Data/CSV_malware.csv'

def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

def preprocess_data(df):
    # TODO: Implement actual preprocessing
    return df

if __name__ == "__main__":
    # read the data from csv file
    df_benign = load_data(f'../{BENIGN_PATH}')
    df_malware = load_data(f'../{MALWARE_PATH}')

    # preprocess the data
    preprocess_data(df_benign)
    preprocess_data(df_malware)