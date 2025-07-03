import employee_wage

if __name__ == "__main__":
    #uc1--> check Attendence
    print("Welcome to Employee Wage Computation Program")
    employee_wage.check_attendance()
   
    #uc2-- Calculate Daily employee Wage 
    print("Daily Wage:", employee_wage.calculate_daily_wage()) 
    
    #UC3--calculating wages for part time employee    
    print("Part-time Wage:", employee_wage.calculate_part_time_wage())
    
   