# **Works Single View**

**Part-1:**

**1- Describe briefly the matching and reconciling method chosen?**

I have created two database tables MusicalWork and Contributors with the many-to-many relationship.
I have implemented the simple solution, read the CSV row by row and check the data from the database by title and ISWC. If it is present, get the object and if not create it, and then add or update the contributors with it as per the result.
Secondly, if the data is incomplete or ISWC is missing, I am checking the work by title and then fetching the contributors and comparing them with contributors that are in file, if there is at least one contributor that is the same, I am taking the union of them.


**2- We constantly receive metadata from our providers, how would you automate the process?**

There are multiple ways to do it, like as per the requirement django management command must be used to ingest data into the database, we can automate this command by simply adding it to your server’s crontab.
Other than that, we can make a separate endpoint where every provider uploads their CSV file and upon uploading we can initiate a celery task where we code to ingest our data.
There is also an option of s3 bucket and a FTP server from where we read the file and ingest the file data in the database.
 

**Part-2**

**1- Imagine that the Single View has 20 million musical works, do you think your solution would have a similar response time?**

Yes, so far my solution will give a similar response as I have applied indexing on search a column and also I have used memory caching to store our results that are not updating frequently.


**2- If not, what would you do to improve it?**

Yes, We can improve it by using the ELK stack. I have not worked on it but I have read about it. It is actually Elasticsearch, Logstash, Kibana to make the searches on an advanced level.
