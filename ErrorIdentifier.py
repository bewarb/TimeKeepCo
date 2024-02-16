import csv
import pandas as pd


# The purpose of this method is to extract the two columns from each csv: SPA and Service Code
# and to make a mini dataframe of them to make comparision easier.
def load_csv_into_df(csv_filepath):
    try:
        df = pd.read_csv(csv_filepath)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file '{csv_filepath}' not found.")

def 

def main():
    while True:
        #parse_csv("..","SPA","Service Code")


if __name__ == "__main__":
    main()




