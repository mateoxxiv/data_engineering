Se hace mediente un parametro de las tareas llamado trigger_rules

## Tipos de reglas
- all_failed
- all_success
- all_done
- one_success
- one_failed
- none_failed
- always

## Sintaxis
```python
from airflow.util.trigger_rule import TriggerRule

DAG (
    max_active_runs: 1 # numero de instancias que se ejecutan al mismo tiempo
)

tarea = PyhonOperator (
    trigger_rule = TriggerRule.All_SUCCESS,
    retry = 1,  # Cantidad de intentos
    retry_delay = 5, # Cantidad de segundos entre intentos
    depends_on_past = True, # Define que la tarea solo se ejecutará una vez su pasado se ejecutó correctamente 
)
```