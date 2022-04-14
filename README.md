## **Instructions on how to execute your code:**


First, create the virtual environment by executing this command. 
Please make sure you already have installed **python 3.8**.

    python -m venv venv

After creating the virtual environment, activate it and install the dependencies 
staying in the project directory by this command.

    pip install -r requirements.txt

**requirements.txt** file has all the external dependencies that are used or need to run your code.

After that, update your postgres database credentials 
and database name in settings.py file located in **musicalwork/** directory.
And create your database tables by running below commands.

	python manage.py makemigrations
	
	python manage.py migrate

After installing all the dependencies, run the server to use it locally by running below command

	python manage.py runserver

**Part-1:**

If the local server is running, Execute the below command to ingest your data into the database.

    python manage.py reconciled_work_data <csv_file_path>

Replace **<csv_file_path>** with the path where your CSV is present in your system. 
Please make sure that CSV file path is required to execute the command.

**Part-2:**

API to query the Works Single View by ISWC to get the work metadata, below is the endpoint for that.

    http://127.0.0.1:8000/musical/<ISWC>

Replace the **<**ISWC**>** with actual code you have to get the metadata.