total_sales = int(input("Enter the total sales: "))
total_costs = int(input("Enter the total cost: "))

profit = total_sales - total_costs
ROI = ((total_sales - total_costs) / total_costs) * 100

print(profit)
print(f"{ROI}%")