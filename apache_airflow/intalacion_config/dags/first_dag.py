from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

# Crear DAG
with DAG(
    dag_id='my_first_dag',
    description='Mi primer DAG',
    start_date=datetime(2025, 1, 1),
    schedule='@once'  # Usar 'schedule' en lugar de 'schedule_interval'
) as dag:
    t1 = EmptyOperator(task_id='dummy')

# DAG creado con un solo operador vacío (dummy)
    t1
