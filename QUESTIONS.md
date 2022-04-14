# Works Single View

### Part-1:

**1- Describe briefly the matching and reconciling method chosen?**

I have created two database tables named MusicalWork and Contributors
with the many-to-many relationship. Approach used for this task is 
as under:

* Read the CSV file row by row.

* Check the database table MusicalWork mentioned above, by title and ISWC.

* If found, get the object and if it is not found create it.

* Update the contributors using the result set.

* If the data is incomplete or ISWC is missing, check the work by 
title from DB, if found, fetch the contributors and compare them with
the contributors from the file, if there is at least one contributor 
that is the same, take union of them.
###

**2- We constantly receive metadata from our providers, how would you automate the process?**

There are multiple ways to do it. However, as per the requirement, 
Django Management Command must be used to ingest data into the 
database, and I have the following options to achieve this.

* Automate this command by simply adding it to your server’s crontab.

* Make a separate endpoint where every provider uploads their CSV file 
and upon uploading we can initiate a celery or celery-beat task/worker where we code to 
ingest our data.

* Options of S3 bucket and an FTP server from where we read the file 
and ingest the file data in the database can also be checked out.
###

### Part-2

**1- Imagine that the Single View has 20 million musical works, do you think your solution would have a similar response time?**

To handle this problem, I have applied indexing on columns on which 
I am performing the search. Moreover, I have used memory caching to 
store our results so that if same search is performed again or data 
is not updated, its response time would be lesser.

When records in database increases to a very large number, API 
response time would get affected to some extent.  
###

**2- If not, what would you do to improve it?**

I have also researched it on how we can improve it further and use of 
the ELK stack which is a combination of Elasticsearch, Logstash and 
Kibana, is also an option to make the searches on an advanced level.
###