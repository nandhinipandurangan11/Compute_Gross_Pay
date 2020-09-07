# CIS40: Summer 2020: Chapter 8 Exercise 1:Nandhini Pandurangan
# This program computes the gross pay of the user given hours and hourly rate
# Input validation is done through a while loop and try + except
# This program is similar to Chapter 5 Exercise 3 but it implements
# Object Oriented Programming

import random


class Pay:
    def __init__(self, obj_name):
        """
        Constructor
        :param: obj_name
        :return None
        """

        # "constants" defining the max hours and additional rate
        self.MAX_HOURS = 40
        self.ADDITIONAL_RATE = 1.5

        self.obj_name = obj_name
        print("The object", self.obj_name, "has been created!\n")

    def get_input(self):
        """
        Retrieves user input

        :param: None
        :returns: name of user's company, the hours worked, pay rate
        """
        # initializing variables before the while loop
        flag = True
        hours = 0
        original_hours = 0
        rate = 0.0

        company = input("Enter your company name: ")

        # input validation
        while flag:
            try:
                hours = int(input("Please enter the hours you have worked: ").strip())
                if hours < 0:
                    print("\nError: hours worked cannot be negative\n")
                    continue

                original_hours = hours
                rate = float(input("Please enter your hourly rate: ").strip())
                if rate <= 0:
                    print("\nError: hourly rate must be a positive number\n")
                    continue

                flag = False

            except:
                print("\n--------Please enter valid numerical values for hours and/or rate--------\n")

        return company, hours, rate

    def calculate_gross_pay(self, hours, rate):
        """
         Performs all the calculations

        :param: hours, rate
        :return: pay
        """
        total_extra_rate = 0.0
        additional_hours = 0

        # evaluating the input:
        if hours > self.MAX_HOURS:
            additional_hours = hours % self.MAX_HOURS
            hours = hours - additional_hours
            total_extra_rate = rate * self.ADDITIONAL_RATE

        # calculating the gross pay and the document number
        pay = (hours * rate) + (additional_hours * total_extra_rate)

        return pay

    def output_results(self, company, original_hours, rate, pay):
        """
         Outputs the results

        :param company, original_hours, rate, pay
        :return: None
        """
        # outputting the results
        print("\nReport for: ", self.obj_name)
        print("Company:", company)
        print("Hours:", round(original_hours, 2))
        print("Rate:", round(rate, 2))
        print("********************************")
        print("Your document number is:", random.randint(1000, 2000))
        print("Your", company, "gross pay is", round(pay, 2), "dollars")

    def main(self):
        """
        Calls the appropriate functions

        :param: None
        :returns: None
        """
        company, hours, rate = self.get_input()
        original_hours = hours
        pay = self.calculate_gross_pay(hours, rate)
        self.output_results(company, original_hours, rate, pay)


# creating a Pay object and calling the Pay method main()
p = Pay("Jimmy Fallon")
p.main()

"""
Output1: 

The object Jimmy Fallon has been created!

Enter your company name: Google
Please enter the hours you have worked: 45
Please enter your hourly rate: 10

Report for:  Jimmy Fallon
Company: Google
Hours: 45
Rate: 10.0
********************************
Your document number is: 1862
Your Google gross pay is 475.0 dollars
--------------------------------------------------

Output2:

The object Jimmy Fallon has been created!

Enter your company name: Apple
Please enter the hours you have worked: forty

--------Please enter valid numerical values for hours and/or rate--------

Please enter the hours you have worked: 40
Please enter your hourly rate: twenty

--------Please enter valid numerical values for hours and/or rate--------

Please enter the hours you have worked: 40
Please enter your hourly rate: 20

Report for:  Jimmy Fallon
Company: Apple
Hours: 40
Rate: 20.0
********************************
Your document number is: 1302
Your Apple gross pay is 800.0 dollars
"""