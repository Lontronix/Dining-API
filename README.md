# Dining-API

A webscraper + API that returns the hours of operation for the dining locations
on the RIT campus.

## Setup
### Python dependencies
Activate a Python Virtual Environment and run `pip3 install -r
requirements.txt` to install the required dependencies.

### Running the Dockerfile
If your running on linux:
- build the container using `podman build -t dining .`
- run the container using `podman run -p 8080:8080 dining` 
