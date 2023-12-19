def main(year):
    """
    Check if a given year is leap year. 
    Args:
     - year (int)
    Returns:
     - boolean: True if it's a leap year, False otherwise
    """

    if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is leap year.")
        return True 
    else:
        print(f"{year} is not leap year.")
        return False 
    
if __name__ == "__main__":
    main(2004)
    main(2007)