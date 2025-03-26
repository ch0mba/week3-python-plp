#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# #The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# #If the discount is 20% or higher, apply the discount; otherwise, return the original price.



def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount only if it's 20% or more
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price  # Return original price if discount is less than 20%

# Example usage:
print(calculate_discount(100, 25))  # Output: 75.0 (25% discount applied)
print(calculate_discount(100, 10))  # Output: 100 (No discount applied)



def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount if 20% or more
        return price - (price * (discount_percent / 100))
    else:
        return "Discount does not apply"  # Return message if discount is too low

# Get user input
price = int(input("Enter item price: "))
discount_percent = int(input("Enter discount: "))

# Call the function and print the result
print(calculate_discount(price, discount_percent))

#