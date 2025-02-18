# This program asks the user to enter a phone number, social security number, and zip code. The program will then
# check the validity of the input (if it is in the correct format).
# The output will display whether the input is valid or not.

# Import the re method
import re

# valid_phone(phone) checks the validity of the entered phone number.
def valid_phone(phone):
    # Valid formats:
    # (123) 456-7890
    # 123-456-7890
    # 123.456.7890
    # 1234567890
    pattern = r"^(\(\d{3}\)\s?|\d{3}[-.]?)\d{3}[-.]?\d{4}$"
    return bool(re.match(pattern, phone))

# valid_ssn(ssn) checks the validity of the entered social security number.
def valid_ssn(ssn):
    # Valid format:
    # 123-45-6789v
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(pattern, ssn))

# valid_zip(zip) checks the validity of the entered zip code.
def valid_zip(zip):
    # Valid formats:
    # 12345
    pattern = r"^\d{5}$"
    return bool(re.match(pattern, zip))

# main() gets input from the user and displays the output.
def main():
    print('This program will check whether an entered phone number, Social Security number, and ZIP code are in their respective valid formats.')
    phone = input('Enter a phone number: ')
    ssn = input('Enter a social security number: ')
    zip = input('Enter a zip code: ')

    print(f"Phone Number Valid: {valid_phone(phone)}")
    print(f"Social Security Number Valid: {valid_ssn(ssn)}")
    print(f"ZIP Code Valid: {valid_zip(zip)}")

# Call main() to run program.
main()
