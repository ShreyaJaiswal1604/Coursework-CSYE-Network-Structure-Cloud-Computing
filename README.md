# Coursework-CSYE-Network-Structure-Cloud-Computing
This graduate-level course covers topics and technologies related to cloud computing and its practical implementations

---
---

## 1. Health App Check
---
DESCRIPTION : create a backend RESTful API application with a health check endpoint (/healthz), fulfilling the following requirements:
Check if the application has connectivity to the database.
* Return HTTP 200 OK if the connection is successful.
* Return HTTP 503 Service Unavailable if the connection is unsuccessful.
* The API response should not be cached. Make sure to add cache-control: 'no-cache' header to the response.
* The API request should not allow for any payload. The response code should be 400 Bad Request if the request includes any payload.
* The API response should not include any payload.
* Only HTTP GET method is supported for the /healthz endpoint.

## Create Virtual Env
```bash
python3 -m venv henv
```

## Activate Virtual Env
```bash
source henv/bin/activate
```

## Add all requirement
```bash
pip install -r requirements.txt
```

## Install packages in the Virtual Env
```bash
pip install Flask SQLAlchemy
```

```bash
pip install python-dotenv
```

```bash
pip install psycopg2-bina```

## Run Docker-compose file
```bash
docker-compose up
```
## Stop Docker-compose file
```bash
docker-compose down
```
## Run the python application
```bash
uvicorn app:app --reload```

---


