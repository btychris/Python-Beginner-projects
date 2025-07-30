starRating = int(input("Enter a star rating between 0 and 5? "))

while starRating < 0 or starRating > 5:
    try:
        print("Invalid Star rating - Try Again!")
        starRating = int(input("Enter a star rating between 0 and 5? "))
    except ValueError:
        continue

print("Thank you!")