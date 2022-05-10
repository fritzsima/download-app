# Download App

## Prerequisites

- Python 3.8.10
- Docker

## Required Packages

- fastapi==0.77.1
- uvicorn==0.17.6
- requests==2.27.1
- click==8.1.3
- tqdm==4.64.0

## Execute

### Local

- Install the python packages.
    ```shell
    pip install -r requirements.txt
    ```

- Execute the `main.py` file.
    ```shell
    python main.py
    ```

### Docker

- Build the docker image
    ```shell
    docker build -t myimage .
    ```
  
- Run the docker container
  ```shell
  docker run -d --name mycontainer -p 8000:8000 myimage
  ```

### Heroku

The [demo](https://download-app-0018.herokuapp.com/api/archive/status/f395b914-fed3-432a-961a-d3d911e46704) is deployed on Heroku platform.

## Test

### Local & Docker

- Archive
  ```shell
  curl --location --request POST 'http://localhost:8000/api/archive/create' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "urls": [
          "https://www.learningcontainer.com/wp-content/uploads/2020/08/Sample-Small-Image-PNG-file-Download.png",
          "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
      ]
  }'
  ```
  
- Staus
  ```shell
  curl --location --request GET 'http://localhost:8000/api/archive/status/d7bf9cf9-6089-4113-bbb8-09255f068862'
  ```
  
### Heroku
- Archive
  ```shell
  curl --location --request POST 'https://download-app-0018.herokuapp.com/api/archive/create' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "urls": [
          "https://www.learningcontainer.com/wp-content/uploads/2020/08/Sample-Small-Image-PNG-file-Download.png",
          "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
      ]
  }'
  ```
  
- Status
  ```shell
  curl --location --request GET 'https://download-app-0018.herokuapp.com/api/archive/status/f395b914-fed3-432a-961a-d3d911e46704'
  ```
