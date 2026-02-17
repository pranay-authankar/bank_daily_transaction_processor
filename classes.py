class Bank:
    def __init__(self):

        self.total_transaction = 0
        self.total_succsessfull = 0
        self.total_fail = 0
        self.no_of_deposits = 0
        self.total_deposits = 0
        self.no_of_withdrawls = 0
        self.total_withdrawls = 0
        self.net_amount = 0
        self.today_change = self.total_deposits - self.total_withdrawls
        self.accounts = {}
    
    def update_success_record(self, type, amount):

        self.total_transaction += 1
        self.total_succsessfull += 1
        
        match type:
            case "deposit":
                self.no_of_deposits += 1
                self.total_deposits += amount
                self.net_amount += amount
                
            
            case "withdraw":
                self.no_of_withdrawls += 1
                self.total_withdrawls += amount
                self.net_amount -= amount
                

            case "transfer":
                self.no_of_deposits += 1
                self.no_of_withdrawls += 1
        
        self.today_change = self.total_deposits - self.total_withdrawls

    def update_fail_record(self):
        self.total_transaction += 1
        self.total_fail += 1

    def display(self):
        print(f"Total Transactions : {self.total_transaction}\nSuccesfull : {self.total_succsessfull}\nFail : {self.total_fail}")
    
    def __str__(self):
            f"{self.total_transaction},{self.total_succsessfull},{self.total_fail},\
            {self.no_of_deposits},{self.total_deposits},{self.no_of_withdrawls},\
            {self.total_withdrawls},{self.net_amount},{self.today_change}"
    
class BankAccount:
    def __init__(self, acc_no, name, initial_bal):

        self.acc_no = acc_no
        self.name = name
        self.__balance = initial_bal


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError
    
    def transfer(self, bank, transfer_acc, amount):
        if transfer_acc in bank.accounts:
            bank.accounts[self.acc_no].withdraw(amount)
            bank.accounts[transfer_acc].deposit(amount)
        else:
            raise ValueError
    
    def __str__(self):
        return f"{self.acc_no},{self.name},{self.__balance}"

class Transaction:
    def __init__(self, id, status, type, source, amount, transfered = None,):
        self.transac_id = id
        self.type = type
        self.source_acc_no = source
        self.amount = amount
        self.transfered_acc_no = transfered
        self.status = status
    
    def __str__(self):
        return f"Status : {self.status}\n\nID - {self.transac_id}\nType : {self.type}\n\
            Account number (self) : {self.source_acc_no}\n\
            Amount : {self.amount}\n\
            Account Number (transfered) : {self.transfered_acc_no}\n-----\n"
    

    