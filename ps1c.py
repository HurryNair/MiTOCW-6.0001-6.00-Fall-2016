def savings_calculator(annual_salary):
    while True:    
        savings = calculate_savings(portion_saved, 0, annual_salary, r, semi_annual_raise)
        
        if savings < target - 100:
            portion_saved = (portion_saved*2 + portion_saved) /2
            cnt += 1
            continue

        elif savings > target + 100:
            portion_saved = (portion_saved - 0)/2
            cnt += 1
            continue

        else:
            break

    return portion_saved, cnt

def calculate_savings(portion_saved, current_savings, annual_salary, r, semi_annual_raise):
    for m in range(1,36):
        current_savings = current_savings + portion_saved*annual_salary/12 + current_savings*r/12
        if (m%6==0):
            annual_salary = annual_salary + semi_annual_raise*annual_salary
    #print(current_savings)
    return current_savings


def main():
    annual_salary = int(input("Enter your annual salary: "))
    total_cost = 1000000
    semi_annual_raise = 0.07
    portion_down_payment = 0.25
    r = 0.04
    target = total_cost*portion_down_payment
    portion_saved = 0.5
    cnt = 0
    
    if (calculate_savings(0.6, 0, annual_salary, r, semi_annual_raise) != target):
            print("It is not possible to pay the down payment in three years.")
    else:
        print("Best savings rate: ", savings_calculator(annual_salary, total_cost, semi_annual_raise, portion_down_payment, r, target, portion_saved, cnt)[0])
        print("Steps in bisection search: ", savings_calculator(annual_salary, total_cost, semi_annual_raise, portion_down_payment, r, target, portion_saved, cnt)[1])


if __name__ == "__main__":
    main()
