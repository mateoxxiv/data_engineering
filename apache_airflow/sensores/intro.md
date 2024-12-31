## Que son
Son un tipo de operadores que están diseñados para esperar a que ocurra una sola cosa.

### Tipos de sensores
- ExternalTaskSensor
- FileSensor
- HttpSensor
- S3KeySensor
- SqlSensor
- airflow.sensors.bash
- airflow.sensors.date_time
- airflow.sensors.external_task
- airflow.sensors.filesystem
- airflow.sensors.python
- airflow.sensors.time_delta
- airflow.sensors.time_sensor
- airflow.sensors.weekday
- airflow.sensors.base

### External task sensor
Son sensores que estan pendientes de ejecute un dag ó una tarea especifica del dag

```python
from airflow.sensors.external_task import ExternalTaskSensor

     t1 = ExternalTaskSensor(
        task_id = 'task1',
        external_dag_id = 'id_otro_dag',
        external_task_id = 'id_otra_tarea',
        poke_interval = 10 # segundos en donde el sensor pregunta si el proceso ha finalizado
        
     )
```


## Sensores poke vs reschedule

| **Aspecto**               | **Modo `poke`**                         | **Modo `reschedule`**                    |
|---------------------------|-----------------------------------------|-----------------------------------------|
| **Comportamiento**         | Bloquea la tarea mientras espera.       | Reprograma la tarea sin bloquear recursos. |
| **Uso de recursos**        | Consume recursos constantemente.        | No consume recursos mientras espera.      |
| **Intervalo de espera**    | Verificación periódica a intervalos.    | Reprogramación periódica a intervalos.    |
| **Escenario ideal**        | Esperas cortas o comprobaciones frecuentes. | Esperas largas sin necesidad de verificar constantemente. |