#from TaxRate import TaxRate
#import numpy as np
#import pandas as pd
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

if __name__ == '__main__':

    vName = "Steve Doe"
    vSalary = 50000

    Tax = SingleTaxCalculator(vSalary)
    # Tax[0] is the tax to be paid
    # Tax[1] is the take home
    print(vName, ", Single ,", vSalary, ",", Tax[0], ",", Tax[1])

    Tax = MarriedJointlyTaxCalculator(vSalary)
    print(vName, ", Married Jointly ,", vSalary, ",", Tax[0], ",", Tax[1])

    # Assignment is to complete the TODO's
    # 1. Complete the code for Single and Married Jointly for the 3rd tax braket
    # 2. Update code for these two functions
    Tax = MarriedSeparatelyTaxCalculator(vSalary)
    print(vName, ", Married Separately ,", vSalary, ",", Tax[0], ",", Tax[1])

    Tax = HeadOfHouseholdTaxCalculator(vSalary)
    print(vName, ", Head Of Household ,", vSalary, ",", Tax[0], ",", Tax[1])
