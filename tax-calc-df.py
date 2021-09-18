#from TaxRate import TaxRate
#import numpy as np
import pandas as pd
# import datatable as dt

SingleBracket1 = 15000
SingleBracket2 = 30000

MarriedJointlyBracket1 = 30000
MarriedJointlyBracket2 = 60000

MarriedSeparatelyBracket1 = 15000
MarriedSeparatelyBracket2 = 30000

HeadofHouseholdBracket1 = 15000
HeadofHouseholdBracket2 = 30000

def SingleTaxCalculator(gSalary):

    Tax = 0
    OriginalSalary = gSalary

    if gSalary <= SingleBracket1:
        Tax = (gSalary * 3.1) / 100
    elif (gSalary > SingleBracket1) & (gSalary <= SingleBracket2):
        gSalary = gSalary - SingleBracket1
        Tax = (SingleBracket1 * 3.1) / 100
        Tax = Tax + (gSalary * 5.25) / 100
    else:
        gSalary = gSalary - SingleBracket1 - SingleBracket2
        Tax = (SingleBracket1 * 3.1) / 100
        Tax = Tax + (SingleBracket2 * 5.25) / 100
        Tax = Tax + (gSalary * 5.7) / 100

    return Tax, OriginalSalary - Tax

    return Tax, OriginalSalary - Tax

def MarriedJointlyTaxCalculator(gSalary):

    Tax = 0
    OriginalSalary = gSalary

    if gSalary <= MarriedJointlyBracket1:
        Tax = (gSalary * 3.1) / 100
    elif (gSalary > MarriedJointlyBracket1) & (gSalary <= MarriedJointlyBracket2):
        gSalary = gSalary - MarriedJointlyBracket1
        Tax = (MarriedJointlyBracket1 * 3.1) / 100
        Tax = Tax + (gSalary * 5.25) / 100
    else:
        gSalary = gSalary - MarriedJointlyBracket1 - MarriedJointlyBracket2
        Tax = (MarriedJointlyBracket1 * 3.1) / 100
        Tax = Tax + (MarriedJointlyBracket2 * 5.25) / 100
        Tax = Tax + (gSalary * 5.7) / 100

    return Tax, OriginalSalary - Tax

def MarriedSeparatelyTaxCalculator(gSalary):
    Tax = 0
    OriginalSalary = gSalary

    if gSalary <= MarriedSeparatelyBracket1:
        Tax = (gSalary * 3.1) / 100
    elif (gSalary > MarriedSeparatelyBracket1) & (gSalary <= MarriedSeparatelyBracket2):
        gSalary = gSalary - MarriedSeparatelyBracket1
        Tax = (MarriedSeparatelyBracket1 * 3.1) / 100
        Tax = Tax + (gSalary * 5.25) / 100
    else:
        # TODO 3
        gSalary = gSalary - MarriedSeparatelyBracket1 - MarriedSeparatelyBracket2
        Tax = (MarriedSeparatelyBracket1 * 3.1) / 100
        Tax = Tax + (MarriedSeparatelyBracket2 * 5.25) / 100
        Tax = Tax + (gSalary * 5.7) / 100
    return Tax, OriginalSalary - Tax

def HeadOfHouseholdTaxCalculator(gSalary):
    Tax = 0
    OriginalSalary = gSalary

    if gSalary <= HeadofHouseholdBracket1:
        Tax = (gSalary * 3.1) / 100
    elif (gSalary > HeadofHouseholdBracket1) & (gSalary <= HeadofHouseholdBracket2):
        gSalary = gSalary - HeadofHouseholdBracket1
        Tax = (HeadofHouseholdBracket1 * 3.1) / 100
        Tax = Tax + (gSalary * 5.25) / 100
    else:
        gSalary = gSalary - HeadofHouseholdBracket1 - HeadofHouseholdBracket2
        Tax = (HeadofHouseholdBracket1 * 3.1) / 100
        Tax = Tax + (HeadofHouseholdBracket2 * 5.25) / 100
        Tax = Tax + (gSalary * 5.7) / 100
    return Tax, OriginalSalary - Tax

def CalculateTax(gFile):
    people_df = pd.DataFrame(pd.read_csv(gFile))

#    taxRate_df = taxRate_df[taxRate_df.FilingStatus == gFilingStatus]
#    taxRate_df = taxRate_df.sort_values(by=['FilingStatus', 'Low'])

    # breaking people file into 4 groups based on the filing status
    singleTax_df = people_df[(people_df.FilingStatus == "Single")]
    MJTax_df = people_df[(people_df.FilingStatus == "Married Jointly")]
    MSTax_df = people_df[(people_df.FilingStatus == "Married Separately")]
    HeadTax_df = people_df[(people_df.FilingStatus == "Head of Household")]

    # Calculating Single tax
    for index, row in singleTax_df.iterrows():
        Name = row['Name']
        FilingStatus = row['FilingStatus']
        Salary = row['Salary']

        Tax = SingleTaxCalculator(Salary)

        print(Name, ",", FilingStatus, ",", Salary, ",", Tax[0], ",", Tax[1])

    # Calculating Married Jointly tax
    for index, row in MJTax_df.iterrows():
        Name = row['Name']
        FilingStatus = row['FilingStatus']
        Salary = row['Salary']

        Tax = MarriedJointlyTaxCalculator(Salary)

        print(Name, ",", FilingStatus, ",", Salary, ",", Tax[0], ",", Tax[1])
    # Calculating Married Separately tax
    for index, row in MSTax_df.iterrows():
        Name = row['Name']
        FilingStatus = row['FilingStatus']
        Salary = row['Salary']

        Tax = MarriedSeparatelyTaxCalculator(Salary)

        print(Name, ",", FilingStatus, ",", Salary, ",", Tax[0], ",", Tax[1])
    # Calculating Head of Household tax
    for index, row in HeadTax_df.iterrows():
        Name = row['Name']
        FilingStatus = row['FilingStatus']
        Salary = row['Salary']

        Tax = HeadOfHouseholdTaxCalculator(Salary)

        print(Name, ",", FilingStatus, ",", Salary, ",", Tax[0], ",", Tax[1])
if __name__ == '__main__':

    CalculateTax("data/people.csv")
    exit(1)

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

    # Assignment is to complete the TODO's
    # TODO
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
