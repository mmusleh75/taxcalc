#from TaxRate import TaxRate
#import numpy as np
#import pandas as pd
# import datatable as dt

SingleBraket1 = 15000
SingleBraket2 = 30000

MarriedJointlyBraket1 = 30000
MarriedJointlyBraket2 = 60000

def SingleTaxCalculator(gSalary):

    Tax = 0
    OriginalSalary = gSalary

    if gSalary <= SingleBraket1:
        Tax = (gSalary * 3.1) / 100
    elif (gSalary > SingleBraket1) & (gSalary <= SingleBraket2):
        gSalary = gSalary - SingleBraket1
        Tax = (SingleBraket1 * 3.1) / 100
        Tax = Tax + (gSalary * 5.25) / 100
    else:
        gSalary = gSalary - SingleBraket1 - SingleBraket2
        Tax = (SingleBraket1 * 3.1) / 100
        Tax = Tax + (SingleBraket2 * 5.25) / 100
        Tax = Tax + (gSalary * 5.7) / 100

    return Tax, OriginalSalary - Tax

def MarriedJointlyTaxCalculator(gSalary):

    Tax = 0
    OriginalSalary = gSalary

    if gSalary <= MarriedJointlyBraket1:
        Tax = (gSalary * 3.1) / 100
    elif (gSalary > MarriedJointlyBraket1) & (gSalary <= MarriedJointlyBraket2):
        gSalary = gSalary - MarriedJointlyBraket1
        Tax = (MarriedJointlyBraket1 * 3.1) / 100
        Tax = Tax + (gSalary * 5.25) / 100
    else:
        gSalary = gSalary - MarriedJointlyBraket1 - MarriedJointlyBraket2
        Tax = (MarriedJointlyBraket1 * 3.1) / 100
        Tax = Tax + (MarriedJointlyBraket2 * 5.25) / 100
        Tax = Tax + (gSalary * 5.7) / 100

    return Tax, OriginalSalary - Tax

if __name__ == '__main__':

    gName = "Steve Doe"
    gSalary = 100000

    SingleTax = SingleTaxCalculator(gSalary)

    # SingleTax[0] is the tax to be paid
    # SingleTax[1] is the take home
    print(gName, ",", gSalary, ",", SingleTax[0], ",", SingleTax[1])

    print("------------------------------------")

    MarriedJointlyTax = MarriedJointlyTaxCalculator(gSalary)

    # MarriedJointlyTax[0] is the tax to be paid
    # MarriedJointlyTax[1] is the take home
    print(gName, ",", gSalary, ",", MarriedJointlyTax[0], ",", MarriedJointlyTax[1])

    print("------------------------------------")

    # Write code to cover "Married Separately" and "Head of Household"





'''
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

'''
