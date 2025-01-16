def is_leap_year(year):
    """
    Determines whether a given year is a leap year.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def year(y):
    """
    Wrapper function to check if a year is a leap year and print the result.
    """
    if is_leap_year(y):
        print(f"{y} is a leap year.")
    else:
        print(f"{y} is not a leap year.")

# Example usage
year(2000)
year(1900)
year(2024)