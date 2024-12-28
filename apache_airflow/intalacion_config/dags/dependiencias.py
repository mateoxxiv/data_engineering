from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def saludar():
    value = 'Hello Platzi'
    print(value)
    return value

def check_saludar(**kwargs):
    # Obtener el valor de la tarea 'python_ope' usando XComs
    value = kwargs['ti'].xcom_pull(task_ids='python_ope')
    print('Verificamos el valor de saludar: ', value)

# Crear DAG
with DAG(
    dag_id='my_first_dependecies_dag',
    description='Creando mi primera dependencia entre tareas',
    start_date=datetime(2023, 12, 28),  # Ajusta la fecha para evitar un inicio en el futuro
    schedule_interval='@once'  # Usar 'schedule_interval' para versiones de Airflow previas a la 3.x
) as dag:
    
    # Tarea 1: PythonOperator para ejecutar la función saludar
    t1 = PythonOperator(
        task_id='python_ope',
        python_callable=saludar
    )
    
    # Tarea 2: Ejecutar un comando bash
    t2 = BashOperator(
        task_id='bash_ope',
        bash_command='echo "holasssss"'
    )
    
    # Tarea 3: Otro comando bash
    t3 = BashOperator(
        task_id='bash2_ope',
        bash_command='echo "holasssss2"'
    )
    
    # Tarea 4: Verificar el valor de saludar utilizando PythonOperator
    t4 = PythonOperator(
        task_id='check_saludar_ope',  # Nombre descriptivo de la tarea
        python_callable=check_saludar,
        provide_context=True  # Necesario para usar kwargs y acceder a 'ti'
    )

    # Dependencias entre tareas
    t1 >> t2 >> [t3, t4]  # t1 se ejecuta antes de t2, t3 y t4, luego t3 y t4 se ejecutan en paralelo
