# OBJECT DETECTION USING AWS REKOGNITION

This is a simple Python application for object detection using AWS Rekognition.

## Features

- Detects objects in images using AWS Rekognition service.
- Dockerized for easy deployment and usage.

## Prerequisites

- Python 3.6 or higher installed on your system.
- Docker installed (if running with Docker).
- An IAM user with access to AWS Rekognition. Ensure the user has appropriate permissions to use the Rekognition service.


## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/mzazakeith/object-detection-aws.git
   cd object-detection
   ```
   
2. Install dependencies:
 
   ```bash
      pip install -r requirements.txt
      ```
   
## Usage
### 1. Run Locally

Using credentials.csv file:
1. Ensure your AWS credentials are stored in the credentials.csv file in the root directory of the project, with the format:

```text
access_key_id,secret_access_key
111111111111,7838383983892387uhw
```

2. Run the application:

```bash
python3 main.py
```

### 2. Running with Docker
1. Build the Docker image:

```bash
docker build -t object-detection .
```

2. Run the Docker container:

```bash
docker run -it --rm object-detection
```

### 3. Adding New Images
Add your new images to the images/ directory.

Run the application and select the newly added image for object detection.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

