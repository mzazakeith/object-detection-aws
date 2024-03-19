from credentials import get_aws_credentials
from select_image import list_images, select_image
from object_detection import detect_and_label_objects


def main():
    proceed = input("Would you like to proceed? (y/n): ")
    if proceed.lower() != 'y':
        print("Exiting...")
        return

    access_key_id, secret_access_key = get_aws_credentials()
    aws_region = input("Please enter the AWS region (default: us-east-1): ") or 'us-east-1'

    images = list_images()
    selected_image = select_image(images)
    image_path = f'images/{selected_image}'

    detect_and_label_objects(image_path, aws_region, access_key_id, secret_access_key)


if __name__ == "__main__":
    main()
