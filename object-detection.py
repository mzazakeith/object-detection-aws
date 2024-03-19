import csv
import boto3
from PIL import Image, ImageDraw, ImageFont
import io

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

result_image = Image.open(io.BytesIO(source_bytes))
draw = ImageDraw.Draw(result_image)

for label in detect_objects['Labels']:
    print(label['Name'])
    print('Confidence:', label['Confidence'])

    for (instances) in label['Instances']:
        if 'BoundingBox' in instances:
            box = instances['BoundingBox']
            left = result_image.width * box['Left']
            top = result_image.height * box['Top']
            width = result_image.width * box['Width']
            height = result_image.height * box['Height']

            points = (
                (left, top),
                (left + width, top),
                (left + width, top + height),
                (left, top + height),
                (left, top)
            )

            draw.line(points, width=5, fill="#03fccf")

            result_image.show()