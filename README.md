## Dockerfile Usage and Commands

This section covers the essential Docker commands needed to build and run the `unique_names_image` using the provided Dockerfile.

### Building the Docker Image
To build the Docker image, run the following command in the terminal where your Dockerfile is located:
```bash
docker build -t unique_names_image .
```
### Running the Docker Container
Once the image is built, you can run it with this command:
```bash
docker run --name unique_names unique_names_image
```
