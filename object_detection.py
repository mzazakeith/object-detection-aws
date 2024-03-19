import boto3
from PIL import Image, ImageDraw, ImageFont
import io


def detect_and_label_objects(image_path, aws_region, access_key_id, secret_access_key):

    client = boto3.client('rekognition', region_name=aws_region, aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key)

    with open(image_path, 'rb') as image_file:
        source_bytes = image_file.read()

    detect_objects = client.detect_labels(Image={'Bytes': source_bytes})

    result_image = Image.open(io.BytesIO(source_bytes))
    draw = ImageDraw.Draw(result_image)

    for label in detect_objects['Labels']:
        print(label['Name'])
        print('Confidence:', label['Confidence'])

        for instances in label.get('Instances', []):
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
                shape = [(left - 2, top - 35), (width + 2 + left, top)]
                draw.rectangle(shape, fill="#69f5d9")

                font = ImageFont.truetype("font/Urbanist.ttf", 50)

                draw.text((left + 170, top - 50), label["Name"], font=font, fill='#000000')

    result_image.show()
