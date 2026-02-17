# Bank Transaction Monitoring

This project is a transaction processing system. It takes the previous day's report, a balance report, and a transaction report as CSV files. It processes these files for the current day, validates transactions to identify wrong entries, and generates an updated daily report.

## How to Operate

If you have copy-pasted the code, follow these steps to run the system:

1.  **Organize Files**: Ensure all the Python files (`main.py`, `functions.py`, `classes.py`, `storage.py`) are in the same folder.

2.  **Prepare Input Data**: Create the following CSV files in the same folder:
    *   `balance.csv`: Current account details (Format: `acc_no,name,balance`).
    *   `previous_report.csv`: Statistics from the last run (Format: `total_transaction,total_succsessfull,...`).
    *   `transaction.csv`: Today's transactions to process (Format: `id,type,acc_no,amount,[transfer_to]`).

3.  **Run the Program**:
    Open your terminal or command prompt and run:
    ```bash
    python main.py
    ```

4.  **Check Output**:
    *   The program will display a comparison table between yesterday and today in the console.
    *   A new file `today_report.csv` will be generated.
    *   The `balance.csv` file will be updated with the new account balances.

## Requirements
*   Python 3.x
*   `csv` module (standard in Python)