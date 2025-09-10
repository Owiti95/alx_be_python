income = float(input("Enter your monthly income: "))

expenses = float(input("Enter your total monthly expenses"))

monthly_savings = income - expenses

annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)


print(f"Your monthly savings are {monthly_savings}")
print(f"Your annual savings are {annual_savings}")
print(f"Your projected savings are {projected_savings}")