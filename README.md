# TimeKeepCo

The prompt that this project is built upon:

```
Highlight your skills using the customer persona and prompt					
Instructions: Utilizing the persona below, follow the instructions, document your steps, and present your work to the hiring manager.					
Your customer is the (fictional) Chief Financial Officer of a company called "Time Keep CO." The organization is a watch and watch parts company dsitributed globally. They are hiring you as an independent contractor to work on the following tasks:      	

Transaction Records: Time Keep Co has two files that need to be scanned for errors and rectifying. These files list many customer transactions along with a Service Code and what is called a "SPA" for each transaction. The two files and their records of each transaction should match, but they do not. Each individual transaction can be identified by its unique combination of Service Code and SPA. Time Keep Co needs you to identify any discrepancies between the two files and report them back to be corrected.		

Task Description:
Ship Keep Co has two files that need to be scanned for errors and rectifying. These files list many customer transactions which are identified by a Service Code and what is called a "SPA" for each transaction. The two files should match, but the do not. Each individual transaction can be identified by its unique combination of Service Code and SPA (corresponding columns will be found in each file). Ship Keep Co needs you to identify any discrepancies between the transaction records in the two files and report them back to be corrected. 		

Write a script to help read the files and check that the data of each transaction matches in both files. Your script should input each CSV file and use the combination of SPA and Service Code in each row as a key to match each transaction between the two files. Your script should identify discrepancies that may be present in coresponding transactions as well as identify any transactions that appear in one file and not in the other. In the output of your script, try to make it clear to a user what type of discrepancy is present (missing transaction or un-matched data in matching transactions)					

```

## Documentation of the Process:

### Understanding the prompt more:

- **Each individual transaction can be identified by its unique combination of Service Code and SPA.**
- **Service Code and what is called a "SPA" for each transaction. The two files should match, but the do not.**
- **identify discrepancies that may be present in coresponding transactions**
- **identify any transactions that appear in one file and not in the other**

Interesting relationship is neither file is considered the "master" file, so we need to make a generalized system that can check both CSVs for discrepancies at the same time.

Diagram:

Class : TransactionComparator, which we have incorporated to display encapuslation principles of OOP

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

To run this program just with default arugments use:

```
$ .\TransactionComparator.py [file1] [file1] 
```

To run it and save the terminal to a CSV:

```
$ .\TransactionComparator.py [file1] [file1] -s
```

For help:

```
$ .\TransactionComparator.py -h
```