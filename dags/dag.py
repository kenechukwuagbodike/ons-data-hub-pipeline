from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

with DAG('ons_data_pipeline', start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_data
    )

    extract >> transform >> load  # dependency chain
