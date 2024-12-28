from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from operador_personalizado_op import HelloOperator


def saludar ():
    print('hello platzi')

# Crear DAG
with DAG(
    dag_id='my_first_custom_operator',
    description='Mi primer operador personalizado',
    start_date=datetime(2023, 12, 28),  # Ajusta la fecha para evitar un inicio en el futuro
    schedule_interval='@once'  # Usar 'schedule_interval' para versiones de Airflow previas a la 3.x
) as dag:
    
    t1 = HelloOperator(
        task_id='hello_world',
        name = 'Mateo Ochoa'
    )

    # Ejecutar el task
    t1
