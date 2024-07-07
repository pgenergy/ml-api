# ml-api
Machine Learning API for Energyleaf WebApp with FastAPI and Docker

## The resulting directory structure

The directory structure looks like this: 

```
├── README.md           <- Top-level README.
├── requirements.txt    <- Requirements from which the environment can be built.
├── docker-compose.yaml
├── Dockerfile          <- Central Dockerfile for the Project
│
├── app                 <- App Folder which defines the Application.
│   ├── __init__.py
│   ├── main.py         <- Main Function for the Microservice Application.
│   ├── settings.py     <- Setting File for the Mircroservice which shows Input and Output 
│   │                      for the application interface.
│   ├── models          <- Defines internal data structures.
│   │   ├── __init__.py
│   │   └── models.py
│   ├── routers         <- Contains all routers as well as their corresponding Input and Output Models
│   │   ├── __init__.py
│   │   └── ds_api
│   │       ├── __init__.py
│   │       └── ds_api.py
│   │       └── models.py
│   ├── services          <- The core services that are used for any microservice process.
│   │   ├── __init__.py
│   │   └── services.py
│   └── tasks           <- Subtasks which are part of the applications.
│       ├── __init__.py
│       └── load_models <- Basic Task which loads a ML Model.
│           ├── __init__.py
│           └── load_models.py
│
├── code                <- Experiment Code from the Start of the Project.
│   ├── archive         <- Outdated Code, which will not be part of the Project.
│   └── main            <- Experiments which are part of the result.
│
├── data                <- Storage for Data and Scripts to download or create data.
``` 

## Install dependencies

It is assumed that Python is installed on the device.
Create a virtual python3 environment at top level of folder structure and install requirements.text inside that environment, e.g:  
````
$ python3 -m venv env
$ source env/bin/activate (Sometimes the activate function is located in another folder)
$ pip install -r requirements.txt
````
## Running in Docker container

Install docker and run in command line
````
$ docker-compose up
````

After the image is built and the container has started you can start interacting with it under `http://localhost:80/`


## Access OpenAPI/Swagger Interface

See `http://localhost:80/docs` 