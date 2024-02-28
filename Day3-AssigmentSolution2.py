# Input: Total bill amount from the user
total_bill_amount = float(input("Enter the total bill amount: Rs."))

# Check if the total bill amount exceeds Rs.1000
if total_bill_amount > 1000:
    # Calculate the discount
    discount = total_bill_amount * 0.1  # 10% discount
    # Apply the discount
    final_amount = total_bill_amount - discount
    print("A discount of 10% has been applied.")
else:
    # No discount applied
    final_amount = total_bill_amount
    print("No discount applied.")

# Print the final amount
print(f"The final bill amount after discount (if any) is: Rs.{final_amount:.2f}")
print(final_amount)
