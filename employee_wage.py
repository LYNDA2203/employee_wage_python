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

#UC5-- Calculating the monthly wages of employee
def calculate_monthly_wage():
    wage_per_hour = 20 #calculating wages as 20 per hour
    working_days = 20 #calculating as per 20 days
    full_day_hours = 8 
    return wage_per_hour * full_day_hours * working_days

#UC6-- Calculating the total wages of employee according to the working hours
def calculate_total_wage():
    wage_per_hour = 20
    total_hours = 0 #initialy assigned as zero
    total_days = 0 #initialy assigned as zero
    max_hours = 100 #max hours taken as 100 hours
    max_days = 20 #maximum days taken as 20

    while total_hours <= max_hours and total_days < max_days:
        hours = 8  # assuming full-time
        total_hours += hours
        total_days += 1

    return total_hours * wage_per_hour 
  
#UC7-- Creating the class[employee_wages ] for  calculating the wages of employee 
class EmployeeWage:
    @staticmethod #connot access class or instance variable but can call the class without object
    def compute_wage(wage_per_hour, total_days, hours_per_day):
        return wage_per_hour * total_days * hours_per_day
    
#UC8-- Creating the class[MultiCompanyWage] for calculating the wages of employee for multiple company
class MultiCompanyWage:
    @staticmethod #connot access class or instance variable but can call the class without object
    def compute_wage(company, wage_per_hour, total_days, hours_per_day):
        total_wage = wage_per_hour * total_days * hours_per_day
        print(f"Total wage for {company}: {total_wage}")
        return total_wage
    