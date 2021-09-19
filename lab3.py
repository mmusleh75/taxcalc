import pandas as pd

SingleBracket1 = 15000
SingleBracket2 = 30000

MarriedJointlyBracket1 = 30000
MarriedJointlyBracket2 = 60000

MarriedSeparatelyBracket1 = 15000
MarriedSeparatelyBracket2 = 30000

HeadofHouseholdBracket1 = 15000
HeadofHouseholdBracket2 = 30000

def GeneralTaxCalculator(gSalary):

    Tax = 0
    OriginalSalary = gSalary
    TaxPercentage=0

    if gSalary <= SingleBracket1:
        Tax = (gSalary * 3.1) / 100
        TaxPercentage = 3.1
    elif (gSalary > SingleBracket1) & (gSalary <= SingleBracket2):
        gSalary = gSalary - SingleBracket1
        Tax = (SingleBracket1 * 3.1) / 100
        Tax = Tax + (gSalary * 5.25) / 100
        TaxPercentage = 5.25
    else:
        gSalary = gSalary - SingleBracket1 - SingleBracket2
        Tax = (SingleBracket1 * 3.1) / 100
        Tax = Tax + (SingleBracket2 * 5.25) / 100
        Tax = Tax + (gSalary * 5.7) / 100
        TaxPercentage = 5.7

    return Tax, OriginalSalary - Tax, TaxPercentage

def MarriedJointlyTaxCalculator(gSalary):

    Tax = 0
    OriginalSalary = gSalary

    if gSalary <= MarriedJointlyBracket1:
        Tax = (gSalary * 3.1) / 100
        TaxPercentage = 3.1
    elif (gSalary > MarriedJointlyBracket1) & (gSalary <= MarriedJointlyBracket2):
        gSalary = gSalary - MarriedJointlyBracket1
        Tax = (MarriedJointlyBracket1 * 3.1) / 100
        Tax = Tax + (gSalary * 5.25) / 100
        TaxPercentage = 5.25
    else:
        gSalary = gSalary - MarriedJointlyBracket1 - MarriedJointlyBracket2
        Tax = (MarriedJointlyBracket1 * 3.1) / 100
        Tax = Tax + (MarriedJointlyBracket2 * 5.25) / 100
        Tax = Tax + (gSalary * 5.7) / 100
        TaxPercentage = 5.7

    return Tax, OriginalSalary - Tax, TaxPercentage

def CalculateTax(gFile):
    people_df = pd.DataFrame(pd.read_csv(gFile))

    GeneralTax_df = people_df[(people_df.FilingStatus == "Single") | (people_df.FilingStatus == "Married Separately") | (people_df.FilingStatus == "Head of Household")]
    MJTax_df = people_df[(people_df.FilingStatus == "Married Jointly")]

    # Calculating Single tax
    for index, row in GeneralTax_df.iterrows():
        Name = row['Name']
        FilingStatus = row['FilingStatus']
        Salary = row['Salary']

        Tax = GeneralTaxCalculator(Salary)

        print(Name, ",", FilingStatus, ",", Salary, ",", Tax[0], ",", Tax[1], ",", Tax[2],"%")

    # Calculating Married Jointly tax
    for index, row in MJTax_df.iterrows():
        Name = row['Name']
        FilingStatus = row['FilingStatus']
        Salary = row['Salary']

        Tax = MarriedJointlyTaxCalculator(Salary)

        print(Name, ",", FilingStatus, ",", Salary, ",", Tax[0], ",", Tax[1], ",", Tax[2],"%")

if __name__ == '__main__':

    CalculateTax("data/people.csv")
