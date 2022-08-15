
# Calculate net salary of employee from his basic pay

basic_pay = float(input('Enter Basic Salary: '))        # Basic salary Input
HRA = 0.1 * basic_pay                                   # House Rent Allowance
TA = 0.05 * basic_pay                                   # Travel Allowance
net_salary = basic_pay + HRA + TA
PT = 0.02 * net_salary                                  # Professional Tax

net_salary_payable = net_salary - PT                    # Net Salary

print("House Rent Allowance:", HRA)                     # Displaying Outputs
print("Travel Allowance:", TA)
print("Gross Salary:", net_salary)
print("Professional Tax:", PT)
print("Net Salary Payable:", net_salary_payable)
