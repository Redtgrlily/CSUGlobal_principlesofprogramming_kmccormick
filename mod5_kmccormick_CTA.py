##Part 1: Rainfall Calculator
def rainfall_calculator():
    total_rainfall = 0.0
    total_months = 0
    
    while True:
        try:
            years = int(input("Enter the number of years: "))
            if years <= 0:
                print("Please enter a positive number of years.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    for year in range(1, years + 1):
        print(f"\n --- Year {year} ---")
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"Enter rainfall (in inches) for month {month}: "))
                    if rainfall < 0:
                        print("Rainfall cannot be negative. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a numberic value.")
            total_rainfall += rainfall
            total_months += 1
            
    average_rainfall = total_rainfall / total_months
    
    print("\nRainfall Report")
    print(f"Total months: {total_months}")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    
def book_club_points():
    try:
        books_purchased = int(input("Enter the number of books purchased this month: "))
        if books_purchased < 0:
            print("Number of books cannot be negative.")
            return
        if books_purchased >= 8:
            points = 60
        elif books_purchased >= 6:
            points = 30
        elif books_purchased >= 4:
            points = 15
        elif books_purchased >= 2:
            points = 5
        else:
            points = 0
        print(f"Points awarded: {points}")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        
def main():
    print("Part 1: Rainfall Calculator\n")
    rainfall_calculator()
    
    print("\nPart 2: Book Club Points\n")
    book_club_points()
    
if __name__ == "__main__":
    main()