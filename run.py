import gspread
from google.oauth2.service_account import Credentials

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

def input_details():
    """ 
    Function tht
    """
    print('GODDARD LITTLEFAIR \n')
    print('Hybrid laptops Check-out System \n')
    print(' \n')
    while True:
        employee_name = input('Enter Employee name:\n')
        print(' \n')
        if validate_data(employee_name):
            break
    
    print(f'{employee_name}, please enter Laptop Number:')
    device_number = input('(This can be found labelled at the bottom of the device.)\n')
    print(' \n')
    while True:
        print('Where will you be using this device?')
        device_location=input('(For example: home, office, onsite.)\n')
        print(' \n')
        if validate_data(device_location):
            break
    print('Return date: ')
    return_date = input('(Please enter as dd/mm/yyyy)')
    print(' \n')
    print(f'NAME: {employee_name}')
    print(f'DEVICE NUMBER: {device_number}')
    print(f'LOCATION: {device_location}')
    print(f'RETURN: {return_date}')

def validate_data(data):
    """
    function
    """
    try:
        if (data.isalpha()) == False:
            raise ValueError(
                f'You entered {data} which is not an alphabetical string.'
            )
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    return True

input_details()

    





    
