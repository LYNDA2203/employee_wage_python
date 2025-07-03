import random

#uc1-- Check Employee is present or Absent
def check_attendance():
    attendance = random.randint(0, 1)#generating the random option for present and absent
    
    #if block for checking the choice of attendence
    if attendance == 1:
        print("Employee is Present") 
    else:
        print("Employee is Absent")
        
#uc2-- Claculate Daily employee Wage    
def calculate_daily_wage():
    wage_per_hour = 20 #calculating as max of 20hours 
    full_day_hour = 8 #for full_time calculating as 8hours
    return wage_per_hour * full_day_hour

#UC3--calculating wages for part time employee    
def calculate_part_time_wage():
    wage_per_hour = 20 #calculating max hours as 20 hours
    part_time_hour = 4 #calculating Part_time as 4hours
    return wage_per_hour * part_time_hour

#UC4-- Getting the working hours of an employee    
def get_work_hours(emp_type):
    return {#returning the value of full_time and part_time values according to the random generated value
        "part_time": 4,
        "full_time": 8
    }.get(emp_type, 0) # if absent-0, part-time-4, full-time-8
    