import pandas as pd
import argparse


class TransactionComparator:
    def __init__(self, file1, file2, column1="SPA", column2="Service Code"):
        self.df1 = self.load_csv_into_df(file1)
        self.df2 = self.load_csv_into_df(file2)
        self.column1 = column1
        self.column2 = column2

    def load_csv_into_df(self, csv_filepath):
        try:
            df = pd.read_csv(csv_filepath)
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file '{csv_filepath}' not found.")

    def compare_columns_data(self):
        discrepancies = {'missing_transactions': [], 'unmatched_transactions': []}

        for index, row in self.df1.iterrows():
            df1_spa_value = row[self.column1]
            df1_service_code_value = row[self.column2]

            # IF a row in df2 has had the same row in DF1 then it is regarded as a matching row and ignored.
            matching_row = self.df2[(self.df2["SPA"] == df1_spa_value) & (self.df2["Service Code"] == df1_service_code_value)]

            # IF it is empty then it is added to the missing transactions
            if matching_row.empty:
                discrepancies['missing_transactions'].append(row)
            else:
                for col in self.df1.columns:
                    # OR if the the
                    if row[col] != matching_row.iloc[0][col]:
                        discrepancies['unmatched_transactions'].append((row, matching_row.iloc[0]))
                        break

        for index, row in self.df2.iterrows():
            df2_spa_value = row[self.column1]
            df2_service_code_value = row[self.column2]
            matching_row = self.df1[(self.df1["SPA"] == df2_spa_value) & (self.df1["Service Code"] == df2_service_code_value)]
            if matching_row.empty:
                discrepancies['missing_transactions'].append(row)

        return discrepancies


def main():
    try:
        parser = argparse.ArgumentParser(description="Compare two CSV files containing transaction records.")
        parser.add_argument("file1", help="Path to the first CSV file")
        parser.add_argument("file2", help="Path to the second CSV file")
        parser.add_argument("--column1", default="SPA", help="Name of the column to use as a key from the first CSV file (default: 'SPA')")
        parser.add_argument("--column2", default="Service Code", help="Name of the column to use as a key from the second CSV file (default: 'Service Code')")
        args = parser.parse_args()

        comparator = TransactionComparator(args.file1, args.file2, args.column1, args.column2)
        discrepancies = comparator.compare_columns_data()

        print("Discrepancies:")
        print("Missing Transactions:")
        for entry in discrepancies['missing_transactions']:
            print(entry)
        print("\nUnmatched Transactions:")
        for entry in discrepancies['unmatched_transactions']:
            print(f"Entry from df1: {entry[0]}")
            print(f"Entry from df2: {entry[1]}")
            print("------")

    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("Welcome to the Transaction Records Discrepancy Checker!")
    main()
