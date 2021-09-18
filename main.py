#from TaxRate import TaxRate
#import numpy as np
#import pandas as pd
# import datatable as dt

SingleBracket1 = 15000
SingleBracket2 = 30000

MarriedJointlyBracket1 = 30000
MarriedJointlyBracket2 = 60000

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
        # TODO 1
        Tax = 0

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
        # TODO 2
        Tax = 0

    return Tax, OriginalSalary - Tax

def MarriedSeparatelyTaxCalculator(gSalary):
    # TODO 3
    return 0, 0

def HeadOfHouseholdTaxCalculator(gSalary):
    # TODO 4
    return 0, 0

if __name__ == '__main__':

    vName = "Steve Doe"
    vSalary = 100000

    Tax = SingleTaxCalculator(vSalary)
    # Tax[0] is the tax to be paid
    # Tax[1] is the take home
    print(vName, ",", vSalary, ",", Tax[0], ",", Tax[1])

    Tax = MarriedJointlyTaxCalculator(vSalary)
    print(vName, ",", vSalary, ",", Tax[0], ",", Tax[1])

    # Assignment is to complete the TODO's
    # 1. Complete the code for Single and Married Jointly for the 3rd tax braket
    # 2. Update code for these two functions
    Tax = MarriedSeparatelyTaxCalculator(vSalary)
    print(vName, ",", vSalary, ",", Tax[0], ",", Tax[1])

    Tax = HeadOfHouseholdTaxCalculator(vSalary)
    print(vName, ",", vSalary, ",", Tax[0], ",", Tax[1])
