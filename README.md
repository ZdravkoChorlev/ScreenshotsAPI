### Screenshots Service

This is a simple service for scraping web pages and taking screenshots by given url and number of links to follow.
The service contains 5 basic endpoints for executing the operations - checking version, service health, taking zip of screenshots and making the screenshots by give url.

#### How to use

*How to run locally.*

Steps:

1. Run local mongoDB instance
2. Setup the `.env` file to match your specific case
3. Run `python -m venv venv` to create virtual env
4. Run `source venv/bin/activate`
5. Run `pip install -r requirements.txt`
6. Run `fastapi run app/main.py`

*How to run it from docker container.*

Steps:

1. Run `docker build -t screenshots .`
2. Run `docker run -d -p 8000:8000 screenshots` to run the service in daemon mode.

#### Endpoints

* GET `/` - default returns the version of the service
* GET `/isalive` - returns status of the service
* GET `/screenshots/{id}` - returns zip file with all screenshots that were downloaded
* POST `/screenshots` - executes scrapping of the service and makes screenshots of theweb pages
* GET `/docs` - default endpoint for FastAPI applications shows the documentation of endpoints and usage