import csv
import boto3
from PIL import Image, ImageDraw, ImageFont

with open('credentials.csv', 'r') as credential_file:
    next(credential_file)
    reader = csv.reader(credential_file)
    for line in reader:
        access_key_id = line[0]
        secret_access_key = line[1]

client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key)


photo = 'images/person.jpg'

with open(photo, 'rb') as image:
    source_bytes = image.read()

detect_objects = client.detect_labels(Image={'Bytes': source_bytes})

for label in detect_objects['Labels']:
    print(label['Name'])
    print('Confidence:', label['Confidence'])

    for(instances) in label['Instances']:
        if 'BoundingBox' in instances:
            box = instances['BoundingBox']
            left = image.width * box['Left']
            top = image.height * box['Top']
            width = image.width * box['Width']
            height = image.height * box['Height']