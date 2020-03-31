def month_calculator():
    '''
    Input prompts and this snippet returns estimated time in months for you to save up target amount taking into account
    semi-annual pay raise
    :return:
    '''
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    months = 0
    while current_savings<portion_down_payment*total_cost:
        current_savings = current_savings + portion_saved*annual_salary/12 + current_savings*r/12
        months += 1
        if (months%6==0):
            #Semi-annual raise calculated every sixth month
            annual_salary=annual_salary + semi_annual_raise*annual_salary
        print(months)
    return months

print("Number of months: ", month_calculator())