from TaxRate import TaxRate
import numpy as np
import pandas as pd
import datatable as dt

taxTable = []
def PrimeTaxTable():
    taxTable.append(TaxRate("Single", 0, 15000, 3.1))
    taxTable.append(TaxRate("Single", 30001, 0, 5.7))
    taxTable.append(TaxRate("Single", 0, 15000, 3.1))



if __name__ == '__main__':
    PrimeTaxTable()

    gName = "Sam Doe"
    gFilingStatus = "Married Jointly"
    gSalary = 35000

    taxRate_df = pd.DataFrame(pd.read_csv("taxrate.csv"))

    taxRate_df = taxRate_df[taxRate_df.FilingStatus == gFilingStatus]
    taxRate_df = taxRate_df.sort_values(by=['FilingStatus', 'Low'])

    taxRateToApply_df = taxRate_df[(taxRate_df.FilingStatus == gFilingStatus) & (taxRate_df.Low <= gSalary) & (taxRate_df.High >= gSalary)]

    #print(taxRateToApply_df)
    taxBraketHigh = taxRateToApply_df['High'].values[0]
    taxBraketTaxRate = taxRateToApply_df['TaxRate'].values[0]

    # print(taxBraketHigh)
    # print(taxBraketTaxRate)
    # print("--------------------------")

    # exit(1)
    taxToPay = 0
    for index, row in taxRate_df.iterrows():
        FilingStatus = row['FilingStatus']
        Low = row['Low']
        High = row['High']
        TaxRate = row['TaxRate']

        if High <= taxBraketHigh:

            taxableSalary = gSalary - High

            taxToPay = taxToPay + (TaxRate * High) / 100


            print(gName, taxableSalary," = " ,FilingStatus, Low, High, TaxRate, " = ", taxToPay)

            #gSalary = gSalary - High

