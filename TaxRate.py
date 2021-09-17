class TaxRate:
    def __init__(self, FilingStatus, FromSalary, ToSalary, Tax):
        self.FilingStatus = FilingStatus
        self.FromSalary = FromSalary
        self.ToSalary = ToSalary
        self.Tax = Tax

    def getFilingStatus(self):
        return self.FilingStatus

    def getFromSalary(self):
        return self.FromSalary

    def getToSalary(self):
        return self.ToSalary

    def getTax(self):
        return self.Tax
