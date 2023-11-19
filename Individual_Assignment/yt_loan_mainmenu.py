
# This file is the `Main Menu`, you may need to download `yt_loan_function_calculator` to support this sheet.
# After completed download both files, you may straitly run this file.
# This file is the split code in TWO FILES. This file will use `import` to functions.
# Do not copy, I have insert my personal trademark in this file. If you copy, lecturer will knows.


import os
try:
    # Attempt to clear the screen for macOS
    os.system('clear')
except:
    try:
        # Attempt to clear the screen for Windows if the first try fails.
        os.system('cls')
    except:
        # Output an error message if both attempts fail.
        print("Unable to clear the screen.")

# Import yt_loan_function_calculator for loan calculator function.
from yt_loan_function_calculator import LoanCalculator

# Implement the menu system with options for the user to choose.
def selection_menu(loan_calculator):
    print("\nWelcome to YEETENG Housing Loan Eligibility and DSR calculator \U0001F600. ")

    while True:
        print("\nWhat would you like to do? Please choose one of the options below.")
        # Six options for the user to choose.
        # They can choose to: 1.calculate loan  2.display previous calculated loans  3.View current DSR threshold
        #                     4. Set DSR Threshold  5. Delete Previous Loan Calculation  6. Exit the system
        print("1. Calculate New Housing Loan")
        print("2. Display Previous Housing Loan Calculations")
        print("3. View current DSR Threshold")
        print("4. Set/Update a New DSR Threshold")
        print("5. Delete Previous Loan Calculation")
        print("6. Exit the System Calculator")

        choice = input("\nEnter your choice (1/2/3/4/5/6): ")

        # If users choose option 1: Calculate new housing loan
        if choice == "1":
            # User's principal housing loan amount
            principal = loan_calculator.get_float_input("Please enter the total amount of housing loan (RM): ")
            # User's annual interest rate for housing loan, the range of rate is from 1% to 6%.
            rate = loan_calculator.get_float_input("Please enter the estimated annual interest rate (%): ", min_value=1, max_value=6)
            # User's housing loan term in years, the range of years is from 0 to 35 years. Because the minimum and maximum loan tenure is from 5 to 35 years.
            year = loan_calculator.get_float_input("Please enter the loan tenure (in years): ", min_value=5, max_value=35)
            # User's monthly income
            salary = loan_calculator.get_float_input("Please enter your monthly income (RM): ")

            # User's commitments (debt) every month.
            # User's monthly car installment.
            car_loan = loan_calculator.get_float_input("Please enter your monthly car installment (RM): ")
            # User's monthly credit card payment.
            credit_card = loan_calculator.get_float_input("Please enter your monthly credit card payment (RM): ")
            # User's monthly PTPTN payment.
            ptptn = loan_calculator.get_float_input("Please enter your monthly PTPTN payment (RM): ")
            # User's others monthly commitment. Example: Phone bill, TNB, Indah water & etc.
            others_loan = loan_calculator.get_float_input("Please enter your total other monthly commitments (RM): ")

            monthly_debt_commitments = [car_loan, credit_card, ptptn, others_loan]

            loan_calculator.display_loan_details(principal, rate, year, salary, monthly_debt_commitments)

        # If user choose option 2: Display previous loan calculation.
        elif choice == "2":
            loan_calculator.display_previous_loans_calculation()

        # If user choose option 3: View current DSR threshold
        elif choice == "3":
            loan_calculator.view_current_threshold()

        # If user choose option 4: Set new DSR threshold
        elif choice == "4":
            loan_calculator.set_dsr_threshold()

        # If user choose option 5: Delete previous calculation
        elif choice == "5":
            loan_calculator.delete_previous_calculation()

        # If user choose option 6: Exit the system calculator.
        elif choice == "6":
            print("\nThe system will end now \U0001F600.")
            print("Thank you for using YEETENG Housing Loan Eligibility and DSR calculator.\n")
            break
        else:
            # If user input value is invalid, they need to retype.
            print("\nYour option is invalid. Please enter a valid option (1/2/3/4/5/6).")


# This is the entry point of the program. 
# If this script is executed directly (not imported), it will initiate the housing loan calculator selection menu.
if __name__ == "__main__":
    loan_calculator = LoanCalculator()
    selection_menu(loan_calculator)
