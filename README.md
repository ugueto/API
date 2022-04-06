## Getting started:

1. Download and install PyCharm -> https://www.jetbrains.com/pycharm/download/
2. Download and install Docker (Desktop preferably) -> https://docs.docker.com/get-docker/
3. Connect GitHub to Pycharm & clone repo.
4. Docker commands:
    -> docker build --tag api .
    -> docker run api
    
NOTES: 
The application includes sample "customers" data for testing purposes.

In order to invoke requests, read the comments on main.py, endpoints:
    -> (base)/customers/ access all users
    -> (base)/customers/email access specific users
