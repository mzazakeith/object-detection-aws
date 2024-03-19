import csv


def get_aws_credentials():
    option = input("How would you like to provide AWS credentials? Enter '1' key-in/paste credentials or '2' use "
                   "credentials.csv file: ")
    if option == '1':
        access_key_id = input("Enter your AWS access key ID: ")
        secret_access_key = input("Enter your AWS secret access key: ")
    elif option == '2':
        access_key_id, secret_access_key = read_credentials_from_file()
    else:
        print("Invalid option. Please enter '1' for key-in/paste or '2' for using credentials.csv file.")
        return None, None
    return access_key_id, secret_access_key


def read_credentials_from_file():
    with open('credentials.csv', 'r') as credential_file:
        next(credential_file)
        reader = csv.reader(credential_file)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]
    return access_key_id, secret_access_key
