#  Malicious Text System

##  A system designed to detect and manage malicious text content.  

### This project uses FastAPI for the REST API, MongoDB for data storage, and custom text processing to identify malicious content.



##  Features
- Fetches data from MongoDB.
- Processes text data to identify malicious content.
- Provides a REST API using FastAPI.



## Project structure
```
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── fetcher.py # Mongo fetch logic
│ ├── processor.py # Text Processing logic
│ └── manager.py # Manages fetcher+processor
│
├── data/
│ └── weapons.txt # list of weapons (blacklist)
│
├── infra/ # OpenShift/K8s manifests (yaml files)
│ ├── deployment.yaml
│ ├── service.yaml
│ ├── route.yaml
│ ├── secrets.yaml
│ └── configmap.yaml
│
├── scripts/
│ └── commands.bat #
│
├── Dockerfile
├── requirements.txt
└── README.md
```


