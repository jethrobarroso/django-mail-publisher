# Django Mail Publisher

This is a simple mail publisher that exposes an API that will queue and publish mails based on the API request data

## Getting Started

Create a new env:
```
py -m venv .venv
```
Activate the virtual environment when in the project's root directory
```
.\.venv\Scripts\activate
```
Install python packages:
```
py -m pip install -r .\requirements.txt
```
For development, create a `.env` file in you project's root directory, which will be used for development purposes. The following key value pairs will be used in your environment:
```
# Django
SECRET=<django generated secret>

# DB settings
DB_USER=<DB username>
DB_PASSWORD=<DB password>
DB_host=<DB hostname>

# Mail settings
EMAIL_HOST=<host FQDN>
EMAIL_PORT=<SMTP port e.g 465>
EMAIL_HOST_USER=<SMTP username>
EMAIL_HOST_PASSWORD=<mail username>
EMAIL_FROM=<from email address>
```
Ensure you have the database created as per DB name specified in the `.env` file located in your project's root folder, and the run the migrations:
```
py manage.py migrate
```
Create a super user. This user will be used to authenticate requests made to the API:
```
py manage.py createsuperuser
```
Finally, start the server:
```
py manage.py runserver
```