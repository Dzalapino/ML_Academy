from src.data_preprocessing import load_data, BENIGN_PATH, MALWARE_PATH

def main():
    # read the data from .csv files to dataframe
    df_benign = load_data(BENIGN_PATH)
    df_malware = load_data(MALWARE_PATH)
    print(df_benign.head())
    print(df_malware.head())

if __name__ == "__main__":
    main()