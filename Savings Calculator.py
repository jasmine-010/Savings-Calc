item = input("What item are you saving for? ")
price = float(input("How much this item cost? ").strip("$"))
current_savings = float(input("How much have you currently saved? ").strip("$"))

if current_savings >= price:
    print("✨ Congrats, you've reached your goal! 😘")
else:
    savings_per_month = float(input("How much do you save each month? ").strip("$"))
    remaining_savings = price - current_savings
    number_of_months_saving = remaining_savings / savings_per_month

print("Welcome to SaveIt!")
print()
print("SaveIt is a savings calculator that helps you save what you have to get what you want.")
print("Here's the breakdkown of everything you need to help achieve your aim.")
print()
print(f"Item: {item}")
print(f"Current Savings: ${current_savings}")
print(f"Savings each month: ${savings_per_month}")
print()
print(f"Here is the remaining amount you need to save: ${remaining_savings:.2f}")
print(f"Now, you just need to keep saving for {number_of_months_saving:.2f} more months. 😁")

