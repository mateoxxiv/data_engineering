from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def saludar ():
    print('hello platzi')

# Crear DAG
with DAG(
    dag_id='my_first_python_dag',
    description='Mi primer DAG',
    start_date=datetime(2023, 12, 28),  # Ajusta la fecha para evitar un inicio en el futuro
    schedule_interval='@once'  # Usar 'schedule_interval' para versiones de Airflow previas a la 3.x
) as dag:
    t1 = PythonOperator(
        task_id='bash_operator',
        python_callable = saludar
    )

    # Ejecutar el task
    t1
