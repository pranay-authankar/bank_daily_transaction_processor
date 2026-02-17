import csv
import classes as C
import storage

def center_align(text, size, fill, ends):
    print(f"{text}".center(size, fill), end = ends)

def format_table(data_set, size):

    for x in range(0, len(data_set)):
        center_align("=", size, "=", "|")
    print()
    
    center_align(" ", size, " ", "|")
    center_align("Yesterday", size, " ", "|")
    center_align("Today", size, " ", "|")
    print()

    for x in range(0, len(data_set)):
        center_align("=", size, "=", "|")
    print()

    i = 0
    while (i < len(data_set[0])):
        for element in data_set:
            center_align(element[i], size, " ", "|")
        i += 1
        print()

        for x in range(0, len(data_set)):
            center_align("=", size, "=", "|")
        print()

def validate_transactions(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        reader.__next__()

        for transact in reader:
            try:
                if transact[0] not in storage.transactions_dict:
                    t_id = transact[0]
                else:
                    raise ValueError

                if transact[1] in storage.transaction_type:
                    t_type = transact[1].strip().casefold()
                else:
                    raise ValueError
                
                if transact[2] in storage.bank.accounts:
                    t_source = transact[2]
                else:
                    raise ValueError
                
                t_amount = int(transact[3])
                
                match t_type:
                    case "deposit" : storage.bank.accounts[t_source].deposit(t_amount)
                    case "withdraw": storage.bank.accounts[t_source].withdraw(t_amount)
                    case "transfer":
                        t_transfer = transact[4].strip()
                        if t_source != t_transfer:
                            storage.bank.accounts[t_source].transfer(storage.bank, t_transfer, t_amount)
                        else:
                            raise ValueError


            except (ValueError, TypeError, IndexError):
                storage.bank.update_fail_record()
                t_status = "Fail"

            else:
                t_status = "Success"
                
                storage.bank.update_success_record(t_type, t_amount)

            finally:
                if t_type == "transfer":
                    storage.transactions_dict[t_id] = C.Transaction(t_id, t_status, t_type, t_source, t_amount, t_transfer)
                else:
                    storage.transactions_dict[t_id] = C.Transaction(t_id, t_status, t_type, t_source, t_amount)

def fill_with_prev_day_report(prev_filename, bank):

    with open(prev_filename) as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            bank.total_transaction = float(row[0])
            bank.total_succsessfull = float(row[1])
            bank.total_fail = float(row[2])
            bank.no_of_deposits = float(row[3])
            bank.total_deposits = float(row[4])
            bank.no_of_withdrawls = float(row[5])
            bank.total_withdrawls =  float(row[6])
            bank.net_amount = float(row[7])
            bank.today_change = float(row[8])

def reset_data_for_new_day(bank):
    bank.total_transaction = 0
    bank.total_succsessfull = 0
    bank.total_fail = 0
    bank.no_of_deposits = 0
    bank.total_deposits = 0
    bank.no_of_withdrawls = 0
    bank.total_withdrawls = 0

def update_new_accounts(balance_filename, bank):
    with open(balance_filename) as f:
        reader = csv.reader(f)
        reader.__next__()

        for account in reader:
            try:
                acc_id = account[0].strip()
                acc_name = account[1].strip()
                acc_balanace = int(account[2])

                if acc_balanace < 0:
                    raise ValueError

                if acc_id not in storage.bank.accounts:
                    storage.bank.accounts[acc_id] = C.BankAccount(acc_id, acc_name, acc_balanace)
                else:
                    raise ValueError
                
            except (ValueError, IndexError, TypeError):
                C.Bank.update_fail_record(bank)
            else:
                C.Bank.update_success_record(bank, "deposit", acc_balanace)     

def update_balance_file(balance_filename, bank_accounts_dict):

    with open(balance_filename, "w", newline = "") as f:
        writer = csv.writer(f)

        writer.writerow(["acc_no","name","balance"])
        for account in bank_accounts_dict:
            row = str(bank_accounts_dict[account]).split(",")
            writer.writerow(row)
        
def update_today_reports(today_filename, bank):
    
    with open(today_filename, "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(["total_transaction,total_succsessfull,total_fail,no_of_deposits,total_deposits,no_of_withdrawls,total_withdrawls,net_amount,today_change"])
        b = bank
        writer.writerow([b.total_transaction, b.total_succsessfull, b.total_fail, b.no_of_deposits,b.total_deposits, b.no_of_withdrawls, b.total_withdrawls, b.net_amount, b.today_change])

def report_csv_to_list(filename):

    data_list = []
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader)
            
            for row in reader:
                for data in row:
                    data_list.append(float(data))
            
    except (FileNotFoundError, ValueError, TypeError):
        return []
    
    else:
        return data_list

def display_compare_reports(prev_report, today_report):

    prev_data = report_csv_to_list(prev_report)
    today_data = report_csv_to_list(today_report)

    heading = ["Total Transactions", "Succesfull Transacts", "Failed Transacts", "Total no. of Deposits", "Total Deposits", "Total no. of withdrawls", "Total Withdraw", "Net Amount", "Change in a day"]

    matrix = [heading, prev_data, today_data]
    
    format_table(matrix, 30)



    
