discountedPrice = int(input("Discounted Price? "))
discount = int(input("Percentage Discount? "))

originalPrice = discountedPrice / (1 - discount/100)
print(f"The original price was £{originalPrice}")