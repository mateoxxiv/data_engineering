## Standar constructor
```bash
my_dag = DAG(
    "DAG name",
    start_date = pendulum.datetime(2021,01,01,tz='utc')
    schedule_interval = "@daily",
    catchup = False
)
op = EmptyOperator(
    task_id = "task",
    dag = my_dag
)
```

## context manager
```bash
with DAG (
    "DAG name",
    start_date = pendulum.datetime(2021,01,01,tz='utc')
    schedule_interval = "@daily",
    catchup = False
) as dag :
    op = EmptyOperator(
    task_id = "task"
    )
```

## decorators
```bash
@dag(
    "DAG name",
    start_date = pendulum.datetime(2021,01,01,tz='utc')
    schedule_interval = "@daily",
    catchup = False
)
def generate_dag ():
    op = EmptyOperator(
        task_id = "task"
    )

dag = generate_dag()
```

## Nota:
Para crear un DAGT en airflow es necesario crear el archivo .py y ubicarlo en la carpeta dags cuando se generó el contenedor