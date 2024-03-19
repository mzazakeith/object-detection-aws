import csv

with open('credentials.csv', 'r') as credential_file:
    next(credential_file)
    reader = csv.reader(credential_file)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
