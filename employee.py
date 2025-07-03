import random

#uc1-- Check Employee is present or Absent
def check_attendance():
    attendance = random.randint(0, 1)#generating the random option for present and absent
    if attendance == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")