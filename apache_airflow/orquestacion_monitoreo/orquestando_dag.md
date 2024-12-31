## Podemos ejecutar un DAG en frecuencias diferentes de tiempo

Esto se hace mediante el parametro schedule_interval, el cual puede recibir los siguientes valores:
- 'None'
- '@once'
- '@hourly'
- '@daily'
- '@weekly'
- '@monthly'
- '@quarterly'
- '@yearly'

## Formato cron
https://crontab.guru/
minuto hora dia_mes mes dia_semana

## Parametros DAG para orquestacion
- start_date
- end_date
- default_args={depends_on_past:True,  (Tareas se ejecutan solo si la anterior se ejecutó)
    max_active_runs:1}  (Se ejecuta uno a la vez)