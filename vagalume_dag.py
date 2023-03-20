from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from lyrics_etl import run_vagalume_etl
from rankings_etl import run_rankings_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023,3,14),
    'email' : ['airflow@example.com'],
    'email_on_failure': False, 
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'vagalume_dag',
    default_args=default_args,
    description='lyric music etl code'
)


run_rankings = PythonOperator(
    task_id='get_vagalume_rankings',
    python_callable=run_rankings_etl,
    dag=dag
)

run_etl = PythonOperator(
    task_id='complete_vagalume_etl',
    python_callable=run_vagalume_etl,
    dag=dag
)

run_rankings >> run_etl