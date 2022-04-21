## Instructions on how to execute your code:

<br/>

Create the virtual environment by executing this command. 
Please make sure that **Python 3.8** and **virtualenv** is installed.

    python3 -m venv env

After creating the virtual environment, activate it and install the 
dependencies while staying in the project directory, using 
this command.

    pip install -r requirements.txt

**requirements.txt** file has all the external dependencies that are
used or needed to run this code.

After that, update your **postgres** database credentials and set the 
database name in **settings.py** file located at **musicalwork/** directory. 
Create database tables by running the following commands. Please make
sure that **Postgres** is installed.

    python manage.py migrate

After performing all the prerequisites, run the server to use it 
locally by executing the command below:

    python manage.py runserver

Your local server is up and running now.

**Part-1:**

Execute the command below to ingest your work data into the database.

    python manage.py reconciled_work_data <csv_file_path>

Replace **<csv_file_path>** with the path where your CSV is placed 
in your system. CSV filepath is required to execute this command.

**Part-2:**

API Endpoint to make the query for the Works Single View by ISWC to 
get the work metadata is as under:

    http://127.0.0.1:8000/musical/<ISWC>
Please make sure that **memcached** is installed.

Replace the **< ISWC>** with actual code you have to get the metadata for.