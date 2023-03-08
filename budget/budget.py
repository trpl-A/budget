
import time
from os import system


# start of typewriter fx ===========================================
def writer(text):
    for a in list(text):
        print(a, end="")
        time.sleep(.045)

# end of function ===========================================



# start of function ===========================================
def monthly_budget():
    salary = int(input("\nenter your monthly net salary: "))
    system("cls")

    # constants
    # =========
    bond = 12000
    electricity = 2000
    water_and_sewage = 700
    wifi_and_data = 1000
    groceries = 1000
    fuel_or_transport = 1200
    # insurance = 
    # school_fees = 
    # security = 
    # medical_aid = 
    # vehicle(s) =

    # ratios
    # ======
    savings_and_investments = salary / 5
    personal = salary / 10
    contingency_cash = salary * (7/100)
    quick_cash = salary * (5/100)
    donations = salary * (3/100)
    family = salary * (5/100)

    ratio_total = savings_and_investments + personal + contingency_cash + quick_cash + donations + family 


    # printing
    # ========
    print("")
    writer(f"With a salary of R{salary} \n")
    writer("=========================== \n")
    time.sleep(.5)

    print(f"savings_and_investments:    R{savings_and_investments}")
    print(f"personal money:             R{personal}")
    print(f"contingency_cash:           R{contingency_cash}")
    print(f"quick_cash:                 R{quick_cash} ")
    print(f"donation money              R{donations}")
    print(f"'family' money              R{family} \n")
    print(f"TOTAL:                      R{ratio_total} \n")


    # adding to text file
    # ===================
    a = open("budgetSheet.txt", "a")
    a.write(f"With a salary of R{salary} \n")
    a.write("=========================== \n" )

    a.write(f"savings_and_investments:    R{savings_and_investments}")
    a.write(f"personal money:             R{personal}")
    a.write(f"contingency_cash:           R{contingency_cash}")
    a.write(f"quick_cash:                 R{quick_cash} ")
    a.write(f"donation money              R{donations}")
    a.write(f"'family' money              R{family} \n")
    a.write(f"TOTAL:                      R{ratio_total} \n\n")

# end of function ============================================
# budget(20000)
# monthly_budget()




# notes =====================
# purchase price for house  R3 million
# bank charges 10% interest
# if 30 year bond:  (8 334 + 840)   / month
# if 20 year bond:  (12 500 + 1250) / month
# if 10 year bond:  (25 000 + 2500) / month

# for the function, assume that monthly cost for bond is 12 000/month

# the interest rate from the bank will vary for a long bond period

