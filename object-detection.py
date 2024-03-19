import csv
import boto3

with open('credentials.csv', 'r') as credential_file:
    next(credential_file)
    reader = csv.reader(credential_file)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key)
