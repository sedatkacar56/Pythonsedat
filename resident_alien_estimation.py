from datetime import datetime, date, timedelta
import time

def calculate_resident_alien_date():
    """
    Calculate the date when someone will become a resident alien based on the substantial presence test.
    """
    entry_date_str = input("Enter the date of entry (YYYY/MM/DD): ")
    entry_date = datetime.strptime(entry_date_str, "%Y/%m/%d").date()
    entry_date_year = entry_date.year
    current_date = date.today()
    current_year = current_date.year
    previous_year_1 = current_year - 1
    previous_year_2 = current_year - 2
    future_year_1 = current_year + 1
    future_year_2 = current_year + 2

   
    
    if  entry_date.year == previous_year_2:
        days_previous_year_1 = (date(previous_year_1, 12, 31) - date(previous_year_1, 1, 1)).days + 1
        days_previous_year_2 = (date(previous_year_2, 12, 31) - entry_date).days + 1

        days_total = (current_date - date(current_year, 1, 1)).days + 1 + days_previous_year_1/3 + days_previous_year_2/6
    
        if  days_total >= 183:
            print("You became a resident alien on:", current_date - timedelta(days_total - 183), ".", "You have been", days_total, " days total and", days_previous_year_2/6, " days in 2021 and", days_previous_year_1/3, "in 2022 and", (current_date - date(current_year, 1, 1)).days, "in 2023 in US.")
        else:
            print("You have been present in the US for", days_total, "days since", entry_date, "You will be resident alien", current_date + timedelta(183 - days_total))
    elif  entry_date.year == previous_year_1:
        days_current_year = (date(current_year, 12, 31) - date(current_year, 1, 1)).days + 1
        days_previous_year_1 = (date(previous_year_1, 12, 31) - entry_date).days + 1
        date_future_year_1 =  date(future_year_1, 1, 1) +  timedelta(183 - (days_current_year/3 + days_previous_year_1/6))
        print("You will become a resident alien on:", date_future_year_1, "after staying in US", timedelta(183 - (days_current_year/3 + days_previous_year_1/6)), "more days. You have been present", days_previous_year_1/6, "in US in 2022. You have been present", days_current_year/3, "in US in 2023.")
    elif  entry_date.year == current_year:
        days_future_year_1 = (date(future_year_1, 12, 31) - date(future_year_1, 1, 1)).days + 1
        days_current_year = (date(current_year, 12, 31) - entry_date).days + 1
        date_future_year_2 =  date(future_year_2, 1, 1) +  timedelta(183 - (days_future_year_1/3 + days_current_year/6))
        print("You will become a resident alien on:", date_future_year_2, "after staying in US", timedelta(183 - (days_future_year_1/3 + days_current_year/6)), "more days. You have been present", days_current_year/6, "in US in 2022. You have been present", days_future_year_1/3, "in US in 2023.")
    else:
        print("You are already resident alien")
    
    time.sleep(25)
    #if  days_total >= 183:
        #print("You became a resident alien on:", current_date + timedelta(days=183), days_total, days_previous_year_2/6, days_previous_year_1, (current_date - date(current_year, 1, 1)).days )
    
    
    #else:
        #print("You have been present in the US for", days_total, "days since", entry_date)



calculate_resident_alien_date()
