import pandas as pd
import argparse

'''
This is the class Transaction Comparator which we have incorporated to display encapuslation principles of OOP

The constructor of this class takes in 4 parameters other than self:

    -file1: The first CSV file the user wants to check
    -file2: The second CSV file the user wants to check
    -column1="SPA": The SPA column
    -column2="Service Code": The Service Code column

The purpose of this class is to compare the data of two CSVs that contain data on transaction history and to
then compile the missing data to later be revealed to a user in the terminal or in a CSV.

Methods in this class:

    -load_csv_into_df(self, csv_filepath): Loads the data of a csv into a dataframe, path given by user
    -compare_columns_data(self): This compares the data of the dfs row by row and collects the missing data in a dictionary
    -save_discrepancies_to_csv(self, discrepancies, save_path): This saves the missing data as a CSV for the user
    
'''
class TransactionComparator:
    # This is the class constructor
    def __init__(self, file1, file2, column1="SPA", column2="Service Code"):
        self.file1 = file1  
        self.file2 = file2 
        self.df1 = self.load_csv_into_df(file1)
        self.df2 = self.load_csv_into_df(file2)
        self.column1 = column1
        self.column2 = column2

    #Loads the data of a csv into a dataframe, path given by user
    def load_csv_into_df(self, csv_filepath):
        try:
            df = pd.read_csv(csv_filepath)
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file '{csv_filepath}' not found.")

    #This compares the data of the dfs row by row and collects the missing data in a dictionary
    def compare_columns_data(self):
        # The dictionary of missing transactions
        discrepancies = {'missing_transactions': []}

        # To make it easier to avoid indexing the worng column I used a set of tuples for each DataFrame based on SPA and Service Code columns
        set_df1 = set(self.df1[[self.column1, self.column2]].itertuples(index=False, name=None))
        
        set_df2 = set(self.df2[[self.column1, self.column2]].itertuples(index=False, name=None))

        # Find missing transactions in df2 that are present in df1
        missing_in_df2 = set_df1 - set_df2
        # Find missing transactions in df1 that are present in df2
        missing_in_df1 = set_df2 - set_df1

        # Process missing transactions for the second file
        for missing in missing_in_df2:
            discrepancies['missing_transactions'].append(f'{self.file2}: {missing}')

        # Process missing transactions for the first file
        for missing in missing_in_df1:
            discrepancies['missing_transactions'].append(f'{self.file1}: {missing}')

        return discrepancies
    
    #This saves the missing data as a CSV for the user
    def save_discrepancies_to_csv(self, discrepancies, save_path):
        # Convert the discrepancies dictionary to a DataFrame
        missing_transactions = pd.DataFrame(discrepancies['missing_transactions'], columns=['Description'])
        # You may want to adjust the column name or structure based on how you want the output CSV to look

        # Save the DataFrame to a CSV file
        missing_transactions.to_csv(save_path, index=False)


# This is the main method
def main():
    # We are using argsparse to handle arguements as well as present information on the program
    try:
        #Purpose
        parser = argparse.ArgumentParser(description="Compare two CSV files containing transaction records.")
        #File 1
        parser.add_argument("file1", help="Path to the first CSV file")
        #File 2
        parser.add_argument("file2", help="Path to the second CSV file")
        
        # This is just an option if other columns wanted to be looked at
        parser.add_argument("--column1", default="SPA", help="Name of the column to use as a key from the first CSV file (default: 'SPA')")
        parser.add_argument("--column2", default="Service Code", help="Name of the column to use as a key from the second CSV file (default: 'Service Code')")
        
        #This is how we state if we want to save the missing data as a csv
        parser.add_argument("-s", "--save", help="Path to save the discrepancies as a CSV file", nargs='?', const="discrepancies.csv", type=str)
        args = parser.parse_args()

        #We create an object from our class using user inputs
        comparator = TransactionComparator(args.file1, args.file2, args.column1, args.column2)
        #Then use the object to call on the method to compare df data and return a dictionary
        discrepancies = comparator.compare_columns_data()

        #Print statements to show data in console
        print("Discrepancies:")
        print("Missing Transactions:")
        for entry in discrepancies['missing_transactions']:
            print(entry)

        #Inform the user what the CSV is saved as if '-s' or '--save' is used
        if args.save:
            comparator.save_discrepancies_to_csv(discrepancies, args.save)
            print(f"Discrepancies saved to {args.save}")

    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Welcome to the Transaction Records Discrepancy Checker!")
    main()
