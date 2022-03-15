import gspread
from google.oauth2.service_account import Credentials
import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hybrid-laptops')

#checkout = SHEET.worksheet('checkout')
#macpro = SHEET.worksheet('macpro')

laptop_list='1 2 3 4 5'

def input_details():
    """ 
    Function that requests user data
    """
    print('GODDARD LITTLEFAIR \n')
    print('Hybrid laptops Check-out System \n')
    print(' \n')
    global checkout_list
    checkout_list = []
    while True:
        employee_name = input('Enter Employee name:\n')
        print(' \n')
        if validate_alpha_data(employee_name):
            checkout_list.append(employee_name)
            break
    while True:
        print(f'{employee_name}, please enter Laptop Number:')
        device_number = input('(This can be found labelled at the bottom of the device.)\n')
        print(' \n')
        if validate_device_number(device_number, laptop_list):
            checkout_list.append(device_number)
            break
    while True:
        print('Where will you be using this device?')
        device_location=input('(For example: home, office, onsite.)\n')
        print(' \n')
        if validate_alpha_data(device_location):
            checkout_list.append(device_location)
            break
    while True:
        print('Return date: ')
        global return_date
        return_date = input('(Please enter as DD-MM-YYYY)')
        print(' \n')
        if validate_date(return_date):
            checkout_list.append(return_date)
            break    
    print(f'NAME: {employee_name}')
    print(f'DEVICE NUMBER: {device_number}')
    print(f'LOCATION: {device_location}')
    print(f'RETURN: {return_date}')

def validate_alpha_data(data):
    """
    Function that validates wether data is an alphabetical string
    """
    try:
        if (data.isalpha()) == False:
            raise ValueError(
                f'You entered {data} which is not an alphabetical string.'
            )
    except ValueError as e:
        print(f'Invalid data: {e}')
        print(' \n')
        return False
    return True

def update_worksheet(data):
    """
    Update checkout worksheet, add new row with the list data provided
    """
    print("Updating ckeckout worksheet...\n")
    macpro = SHEET.worksheet('macpro')
    macpro.append_row(data)
    print("Checkout worksheet updated successfully.\n")


def validate_device_number(data, list):
    """
    Function that validates wether data is an alphabetical string
    """
    try:
        if data not in list:
            raise ValueError(
                f'You entered {data} which is not a valid laptop number.'
            )
    except ValueError as e:
        print(f'Invalid data: {e}')
        print(' \n')
        return False
    return True

def validate_date(data):
    """ 
    Function that validates user input is valid
    #format entry: DD-MM-YYYY
    """   
    date = data
    format = "%d-%m-%Y"

    t = datetime.datetime.now()
    time = t.strftime("%d-%m-%Y")

    try:
        if datetime.datetime.strptime(date, format) is False:
            raise ValueError(
                f"{date} is not in formar dd-mm-YYYY."
                )
        elif time > date:
            raise ValueError(
                f'Date entered is before today'
                )
    except ValueError as e:
        print(f'Invalid data: {e}')
        print(' \n')
        return False
    return True

input_details()
#update_worksheet(checkout_list)    





    
