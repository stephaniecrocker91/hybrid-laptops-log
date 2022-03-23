import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hybrid-laptops')

checkout = SHEET.worksheet('checkout')
macpro_1 = SHEET.worksheet('macpro1')

laptop_list='1 2 3 4 5'
yes_no = ["Y", "N"]

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
        try:
            print('Return date: ')
            global my_string
            my_string = str(input('Enter date: dd-mm-YYYY '))
            global my_date
            my_date = datetime.strptime(my_string, "%d-%m-%Y")
            global d
            d = datetime.now()
            global today_date
            today_date = d.strftime("%d-%m-%Y")
            format = "%d-%m-%Y"
            if d < my_date:
                break
            raise ValueError(f'{my_date} is before today')
            if datetime.strptime(my_string, format):
                break 
            raise ValueError(f"{my_date} is not in format dd-mm-YYYY.")
        except ValueError as e:
            print(e)
        # print(my_date)
        # print(today_date)
        # print(d > my_date)
        # if validate_date(my_date, d, my_string):
          #   checkout_list.append(my_string)
            # break    
    print(f'NAME: {employee_name}')
    print(f'DEVICE NUMBER: {device_number}')
    print(f'LOCATION: {device_location}')
    print(f'RETURN: {today_date}')

def confirm_input():
    """ 
    Function to confirm user wants to submit data
    """
    print("Are the details displayed above correct?")
    while True:
        data_confirmation = input('Y or N?\n').upper()
        if validate_key(data_confirmation, yes_no):
            break

def update_worksheet(data):
    """
    Update checkout worksheet, add new row with the list data provided
    """
    print("Updating ckeckout worksheet...\n")
    macpro_1 = SHEET.worksheet('macpro1')
    macpro_1.append_row(data)
    print("Checkout worksheet updated successfully.\n")




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




def validate_key(data, keys):
    """
    Function that validates data.
    """
    try:
        if data not in keys:
            raise ValueError(
                f"Input--> {data}. Only {keys} are valid inputs."
            )
        elif (data.isalpha()) is False:
            raise ValueError(
                f'You entered {data} which is not an alphabetical string.'
            )
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    return True



input_details()
confirm_input()
update_worksheet(checkout_list)    
confirm_input()