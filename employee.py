import random

#uc1-- Check Employee is present or Absent
def check_attendance():
    attendance = random.randint(0, 1)#generating the random option for present and absent
    if attendance == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")
        
#uc2-- Claculate Daily employee Wage    
def calculate_daily_wage():
    wage_per_hour = 20 #max of 20hours in a month 
    full_day_hour = 8 #for full_time calculating as 8hours
    return wage_per_hour * full_day_hour