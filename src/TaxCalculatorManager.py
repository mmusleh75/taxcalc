class TaxCalculatorManager(object):
    def __init__(self):
        pass

    def CalculateTax(self, Salary, TaxRate):
        return (Salary * TaxRate) / 100
