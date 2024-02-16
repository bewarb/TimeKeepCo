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