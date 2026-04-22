from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def preprocess():
    os.system("python notebooks/preprocess.py")

def feature_engineering():
    os.system("python notebooks/feature_engineering.py")

def train_model():
    os.system("python src/train_model.py")

dag = DAG(
    'churn_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

task1 = PythonOperator(
    task_id='preprocess',
    python_callable=preprocess,
    dag=dag
)

task2 = PythonOperator(
    task_id='feature_engineering',
    python_callable=feature_engineering,
    dag=dag
)

task3 = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag
)

task1 >> task2 >> task3