# proj-vagalume-airflow
Simple pipeline connecting Vagalume API, Airflow and AWS

The first step is to create an Python Script that will get songs lyrics from Vagalume. This was done providing artist and song name.
Second, we created an Apache Airflow DAG with the function above.
After that, the code was adapted to search for the Top 10 songs in Vagalume for a given week, where it would GET the top 10 songs for that week.
The result of this request it is saved in a file, which will be used as input for the first task, now adapted to receive this input.
Lastly, the results will be saved in another file and a Python function will transform the lyrics in Braille.
The idea was to save the results in a database by the end.
