
# This file is the back-end calculator functions to support `Main Menu`.
# Please do download this file to support `yt_loan_mainmenu`.
# Do not run this file. 
# Do not copy, I have insert my personal trademark in this file. If you copy, lecturer will knows.


class LoanCalculator:
    def __init__(self):
        # List to store calculations
        self.loan_calculations = []
        # The original(default) DSR threshold is 70%
        self.dsr_threshold = 70

    # Function for the float input to limit at certain range. Limit the range from minimum value to maximum value.
    def get_float_input(self, prompt, min_value=None, max_value=None):
        while True:
            try:
                value = float(input(prompt))
                if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                    return value
                else:
                    print(f"Your input is invalid. The input value must only be between {min_value} and {max_value}.")
            except ValueError:
                print("Your input is invalid. Please enter a numerical value only.")


    # Function to calculate the monthly housing installment (loan).
    def calculate_monthly_housing_instalment(self, principal, rate, year):
        r = (rate / 100) / 12
        n = year * 12
        monthly_payment = (r * principal * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
        return monthly_payment


    # Function to calculate the total amount payable over the term of loan.
    def calculate_total_payment(self, monthly_payment, year):
        return monthly_payment * year * 12


    # Function to calculate Debt Service Ratio (DSR)
    def calculate_dsr(self, salary, monthly_debt_commitments):
        dsr = (sum(monthly_debt_commitments) / salary) * 100
        return dsr


    # Let user to display the current DSR threshold.
    def view_current_threshold(self):
        print(f"Current DSR Threshold: {self.dsr_threshold}%")


    # Function for users to set a new DSR threshold. (BM)
    def set_dsr_threshold(self):
        new_threshold = self.get_float_input("Please enter your new DSR threshold (%): ", min_value=0, max_value=100)
        self.dsr_threshold = new_threshold
        print(f"Your DSR threshold updated to {self.dsr_threshold}%")


    # Display(print) the loan detials to users.
    def display_loan_details(self, principal, rate, year, salary, monthly_debt_commitments):
        monthly_payment = self.calculate_monthly_housing_instalment(principal, rate, year)
        total_payment = self.calculate_total_payment(monthly_payment, year)
        dsr = self.calculate_dsr(salary, monthly_debt_commitments)

        # Display the housing loan detials
        # The '\n' means print new line for string.
        print("\nLoan Details:")
        print(f"Principal Loan Amount: RM {principal:.2f}")
        print(f"Annual Interest Rate: {rate:.2f}%")
        print(f"Loan Term: {year} years")
        print(f"Monthly Income: RM {salary:.2f}")

        # Display the different types of user's monthly debt.
        print("Monthly Debt Commitments:")
        for index, commitment in enumerate(["House Loan", "Car Loan", "Credit Card", "PTPTN"]):
            print(f"  - {commitment}: RM {monthly_debt_commitments[index]:.2f}")
        print(f"\nMonthly Instalment: RM {monthly_payment:.2f}")
        print(f"Total Amount Payable: RM {total_payment:.2f}")
        print(f"Debt Service Ratio (DSR): {dsr:.2f}")

        # Assume the threshold for DSR is 70%. 
        # If user's DSR is smaller than 70%, then eligible. 
        if dsr <= self.dsr_threshold:
            print("\nCongratulations! You are eligible for the housing loan.")
        else:
            # If not, then not eligible.
            print(f"\nSorry, you are not eligible for the housing loan based on your Debt Service Ratio (DSR > {self.dsr_threshold}%).")

        # Append the details of the current housing loan calculation to the list of loan calculations.
        self.loan_calculations.append({
            "Principal": principal,
            "Annual Interest Rate": rate,
            "Loan Term in years": year,
            "Monthly Salary": salary,
            "Monthly Debt Commitments": monthly_debt_commitments,
            "Monthly Housing Instalment": monthly_payment,
            "Total Amount Payable": total_payment,
            "DSR": dsr
        })


    # Functions to display previous loan calculation.
    def display_previous_loans_calculation(self):

        # If the user's didn't have any previous loan calculation.
        if not self.loan_calculations:
            print("\nNo previous loan calculations.")
        else:
            # If the user's have previous loan calculation
            print("\nPrevious Loan Calculations:")
            # To iterate through each housing loan calculation in the list and display the details
            for index, loan in enumerate(self.loan_calculations, start=1):
                # Print the header for each loan calculation with its index. Example : "Housing Loan Calculation 1"
                print(f"\nHousing Loan Calculation {index}:")
                for key, value in loan.items():
                    if key == "Monthly Debt Commitments":
                        print(f"{key}:")
                        for i, commitment in enumerate(["House Loan", "Car Loan", "Credit Card", "PTPTN"]):
                            print(f"  - {commitment}: RM {value[i]:.2f}")
                    else:
                        print(f"{key}: {value:.2f}")


    # Functions for users to delete previous loan calculations. (BM)
    def delete_previous_calculation(self):

        # If no previous calculations to delete. 
        if not self.loan_calculations:
            print("\nNo previous loan calculations to delete.")
            return

        # Display the list of previous loan calculations.
        self.display_previous_loans_calculation()
        # Teach the user to enter the index of the calculation to delete
        index_to_delete = self.get_float_input("\nEnter the index of the calculation to delete (1/2/3): ")

        # Validate the user input and delete the specified calculation (BM).
        if 1 <= index_to_delete <= len(self.loan_calculations):
            deleted_calculation = self.loan_calculations.pop(int(index_to_delete) - 1)
            print(f"\nCalculation {index_to_delete} deleted successfully: ")
            print("\nDeleted Calculation Details:")

            # To display details of the deleted loan calculation
            for key, value in deleted_calculation.items():
                if key == "Monthly Debt Commitments":
                    print(f"{key}:")

                    # To display details of each monthly debt commitment.
                    for i, commitment in enumerate(["House Loan", "Car Loan", "Credit Card", "PTPTN"]):
                        print(f"  - {commitment}: RM {value[i]:.2f}")
                else:
                    print(f"{key}: {value:.2f}")
        else:
            print(" Your input is invalid. No calculation deleted.")
