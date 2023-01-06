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
For development, create a `.env` file in you project's root directory, which will be used for development purposes. In you production environment, these should be configured as environment variables on the host machine. Many of these key value pairs can be configured straight in the `settings.py` file, but sensitive information like passwords and tokens should at least be kept as environment variables or even better, stored in some sort of password vault. The following key value pairs will be used in your environment:
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

```console
py manage.py migrate
```

Create a super user. This user will be used to authenticate requests made to the API:

```console
py manage.py createsuperuser
```

Finally, start the server:

```console
py manage.py runserver
```

**NOTE**
Remember to run `python manage.py collectstatic` in you production environment.

## How to use

The project exposes `POST /mails/` endpoint where the mail information will be passed through into the request body. Basic authentication will be used upon request, so a user needs to be created.

Mails won't be sent immediately. They are queued and it's up to the user of the project to setup cron jobs that will send the queued mails in batches.

Sample of the cron jobs that can be used to send the mails in batches and also perform a cleanup after specified amount of days:

```console
* * * * * (cd $PROJECT; python manage.py send_queued_mail --processes=1 >> $PROJECT/cron_mail.log 2>&1)
0 1 * * * (cd $PROJECT; python manage.py cleanup_mail --days=30 --delete-attachments >> $PROJECT/cron_mail_cleanup.log 2>&1)
```
