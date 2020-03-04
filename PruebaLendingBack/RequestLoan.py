class RequestLoan:

    def __init__(self, taxId,soSecNum, amount, loanDecis):
        self.taxId = taxId
        self.soSecNum = soSecNum
        self.amount = amount
        self.loanDecis =loanDecis

requLoanList = [
    {'taxId': '1234', 'soSecNum': 1234, 'amount': 49000, 'loanDecis':'Approved'},
    {'taxId': '5678', 'soSecNum': 5678, 'amount': 50000, 'loanDecis':'Undecided'},
    {'taxId': '9012', 'soSecNum': 9012, 'amount': 51000, 'loanDecis':'Declined'}
]