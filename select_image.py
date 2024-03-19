import os


def list_images():
    images = os.listdir('images/')
    print("Available images for object detection:")
    for idx, image in enumerate(images, start=1):
        print(f"{idx}. {image}")
    return images


def select_image(images):
    while True:
        try:
            image_choice = int(input("Please select an image to perform object detection (by index): "))
            if 1 <= image_choice <= len(images):
                return images[image_choice - 1]
            else:
                print("Invalid choice. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
