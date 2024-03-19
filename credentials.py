import csv


def get_aws_credentials():
    with open('credentials.csv', 'r') as credential_file:
        next(credential_file)
        reader = csv.reader(credential_file)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]
    return access_key_id, secret_access_key
