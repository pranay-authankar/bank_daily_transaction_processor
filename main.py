import functions as system
import storage as database

balance_file = "balance.csv"
previous_day_report = "previous_report.csv"
today_report = "today_report.csv"
transaction_file = "transaction.csv"

system.fill_with_prev_day_report(previous_day_report, database.bank)

system.reset_data_for_new_day(database.bank)

system.update_new_accounts(balance_file, database.bank)

system.validate_transactions(transaction_file)

system.update_today_reports(today_report, database.bank)

system.update_balance_file(balance_file, database.bank.accounts)

system.display_compare_reports(previous_day_report, today_report)

system.center_align(" All tasks done successfully ", 40, "-", "\n")
system.center_align(" Ready for next Day ", 40, "-", "\n")
