'''
Docstring:
A program for experimenting with modifying expenses figures.
'''

from tabulate import tabulate
from colorama import Back, Fore, Style
from user_functions import add_expenses, highest_expense
from income_data import levelPay

print(Fore.BLUE + "--- Welcome to 'Tell Me Your Level, I’ll Give You Your Income!! ---\n\nIn this program, we're here to serve you by analyzing your income and expenses to give you a quick snap snot of what they look like. \n\n" + Style.RESET_ALL)

name = input("What is your name? ")
print("\t\t")
month = input("What month are we preparing this statement for? ")
print("\t\t")


def mvp():
	pay = 0
	#pay starts at 0 before key accesses income of user by the user's level input#

	while True:
		level = int(input("{}, please input your current accounting level from 2 - 20\n".format(name)))

		if level in levelPay.keys():
			pay += levelPay[level]
			break

		else:
			print("{}, please re-check your input. Your level should be between 2 and 20. {} let's try it again".format(name, name))
			continue

		break
		

	while True:
		currency = input ("\nWhat is your country of residence?\nPlease input 'NG' for Nigeria or 'US' for the United States of America\n")

		if currency == "NG":
			pay *= 450

		elif currency == "US":
			pass

		else:
			if currency != "NG" or "US":
				print ("\nPlease re-check your input")
			
			continue							 

		break
					

	print("\n\n{}, here is a list of the available expenses. Please choose accordingly if you want to add an expense. Thank you!".format(name))
	#shows all possible expenses to user#

	print("\n\n--------- Possible Expenses List ----------\nOffice Setup\nFood\nHealth Insurance\nMortgage\nAuto Insurance\nChild care\n")


	while True:
		officeSetup = input("\n{}, do you want to add an Office Setup expense? Please type 'y' or 'n'\n".format(name))

		if officeSetup == "y":
			expense1 = int(input("\n{}, please input how much you spend on this expense (Numbers Only)\n".format(name)))
			pay -= expense1

		elif officeSetup == "n":
			expense1 = 0
			pass
			
		else:
			if officeSetup != 'y' or 'n':
				print("Please input 'y' or 'n'")
				continue

		break


	while True:
		food = input("\n\n{}, do you want to add a Food expense? Please type 'y' or 'n' \n".format(name))
		
		if food == "y":
			expense2 = int(input("\n{} please input how much you spend on this expense (Numbers Only)\n".format(name)))
			pay -= expense2

		elif food == "n":
			expense2 = 0
			pass

		else:
			if food != 'y' or 'n':
				print("Please input 'y' or 'n'")
				continue

		break


	while True:
		healthInsurance = input("\n\n{}, do you want to add a Health Insurance expense? Please type 'y' or 'n'\n".format(name))
		
		if healthInsurance == "y":
			expense3 = int(input("\n{}, please input how much you spend on this expense (Numbers Only)\n".format(name)))
			pay -= expense3

		elif healthInsurance == "n":
			expense3 = 0
			pass
		
		else:
			if healthInsurance != 'y' or 'n':
				print("Please input 'y' or 'n'")
				continue

		break
		

	while True:
		mortgage = input("\n\n{}, do you want to add a Mortgage expense? Please type 'y' or 'n'\n".format(name))
		if mortgage == "y":
			expense4 = int(input("\n{} please input how much you spend on this expense (Numbers Only)\n".format(name)))
			pay -= expense4

		elif mortgage == "n":
			expense4 = 0
			pass

		else:
			if mortgage != 'y' or 'n':
				print("Please input 'y' or 'n'")
				continue

		break


	while True:
		autoInsurance = input("\n\n{}, do you want to add an Auto Insurance expense? Please type 'y' or 'n'\n".format(name))

		if autoInsurance == "y":
			expense5 = int(input("\n{} please input expense how much you spend on this (Numbers Only)\n".format(name)))
			pay -= expense5
		
		elif autoInsurance == "n":
			expense5 = 0
			pass
		
		else:
			if autoInsurance != 'y' or 'n':
				print("Please input 'y' or 'n'")
				continue

		break


	while True:
		childCare = input("\n\n{} do you want to add a Child care expense? Please type 'y' or 'n'\n".format(name))
		if childCare == "y":
			expense6 = int(input("{} please input how much you spend on this expense (Numbers Only)\n".format(name)))
			pay -= expense6

		elif childCare == "n":
			expense6 = 0
			pass

		else:
			if childCare != 'y' or 'n':
				print("Please input 'y' or 'n'")
				continue

		break
		
	total_expenses = add_expenses(expense1, expense2, expense3, expense4, expense5, expense6)

	print("\n{} your approximate ".format(name) + Fore.BLUE + "expenses" + Style.RESET_ALL + " for the month of {} would be {}".format(month,total_expenses))

	print("\n\n")




	if currency == "NG":
		table = [['Gross Pay', levelPay[level] * 450],
		['Office Setup', expense1],
		['Food', expense2],
		['Health Insurance', expense3],
		['Mortgage', expense4],
		['Auto Insurance', expense5], 
		['Child care', expense6]]


		print(tabulate (table, headers = ["Items", "Networth"]))

		print(Back.GREEN + "\n{}, your net income is N".format(name) + str(pay) + Style.RESET_ALL)

		print("\t")

		highest_value = highest_expense(expense1, expense2, expense3, expense4, expense5, expense6)

		while True:
			satisfied = input("\n\nAre you satisfied with your report? Please input 'y' for Yes, or 'n' for No\n")

			if satisfied == "n":		
				if total_expenses >= (0.6 * (levelPay[level] * 450)):
					print("\n{}, your highest expense is N{}. It's advisable you find a way to slash this expense, so that it doesn't go over your gross pay.".format(name,highest_value)) 

				else:
					print ("\n---- Feedback ---- \nI think your expenses are within budget. Keep it up!")

			elif satisfied == "y":
				pass

			else:
				if satisfied != "y" or "n":
					print ("\nPlease input 'y' or 'n'")
				continue

			break


	
	elif currency == "US":
		table = [['Gross Pay', levelPay[level]],
		['Office Setup', expense1],
		['Food', expense2],
		['Health Insurance', expense3],
		['Mortgage', expense4],
		['Auto Insurance', expense5], 
		['Child care', expense6]]


		print(tabulate (table, headers = ["Items", "Networth"]))

		print(Back.GREEN + "\n{}, your net income is $".format(name) + str(pay) + Style.RESET_ALL)

		print("\t")

		highest_value = highest_expense(expense1, expense2, expense3, expense4, expense5, expense6)

		while True:
			satisfied = input("\n\nAre you satisfied with your report? Please input 'y' for Yes, or 'n' for No\n")

			if satisfied == "n":		
				if total_expenses >= 0.6 * levelPay[level]:
					print("\n{}, your highest expense is ${}. It's advisable you find a way to slash this expense, so that it doesn't go over your gross pay.".format(name,highest_value)) 

				else:
					print ("\n---- Feedback ---- \nI think your expenses are within budget. Keep it up!")


			elif satisfied == "y":
				pass

			else:
				if satisfied != "y" or "n":
					print ("\nPlease input 'y' or 'n'")
				continue

			break


	print ("\n\nThank you for using my app!")


print(mvp())
