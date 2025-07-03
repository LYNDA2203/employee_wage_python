import employee_wage

if __name__ == "__main__":
    #uc1--> check Attendence
    print("Welcome to Employee Wage Computation Program")
    employee_wage.check_attendance()
   
    #uc2-- Calculate Daily employee Wage 
    print("Daily Wage:", employee_wage.calculate_daily_wage()) 
    
    #UC3--calculating wages for part time employee    
    print("Part-time Wage:", employee_wage.calculate_part_time_wage())
    
    #UC4-- Getting the working hours of an employee 
    import random
    emp_type = random.choice(["absent", "part_time", "full_time"])# step1: return the options 
    hours = employee_wage.get_work_hours(emp_type)# step2: calls the function and returns values from the function
    print(f"Employee Type: {emp_type}")# returns the employee type[full-time or part_time]
    print("Wage:", hours * 20)# calculate wages according to the hours of employee works
   
  #UC5-- Calculating the monthly wages of employee
    print("Monthly Wage:", employee_wage.calculate_monthly_wage())
    
  #UC6-- Calculating the total wages of employee according to the working hours
    print("Total Wage:", employee_wage.calculate_total_wage())
    
  