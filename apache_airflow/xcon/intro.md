**XCom (Cross-Communication)** es una característica en **Apache Airflow** que permite la **comunicación entre tareas** dentro de un **DAG** (Directed Acyclic Graph). 

### ¿Qué hace XCom?

XCom se utiliza para **pasar datos entre tareas** de un DAG. Esto permite que una tarea **envíe resultados** a otras tareas que dependen de esos resultados para su ejecución.

### Características clave de XCom:
1. **Intercambio de datos**: Las tareas pueden **guardar datos** (como resultados de ejecución, estados, configuraciones, etc.) y otras tareas pueden **recuperarlos** posteriormente.
2. **Interacción**: XCom usa una base de datos para almacenar estos datos, y las tareas se comunican a través de la base de datos de Airflow.
3. **Almacenamiento temporal**: Los datos almacenados en XCom tienen una vida útil **temporal**, y no están pensados para almacenar grandes volúmenes de información a largo plazo.

### Ejemplo:

- **Tarea 1**: Realiza un cálculo y guarda el resultado en XCom.
- **Tarea 2**: Recupera ese resultado y lo usa para realizar otra operación.

### Funciones de XCom en Airflow:
- `task_instance.xcom_push(key, value)` – Para almacenar datos.
- `task_instance.xcom_pull(task_ids='task_name', key='key_name')` – Para recuperar datos.

### Resumen:
XCom permite la comunicación y el intercambio de datos entre tareas dentro de un DAG en Airflow, facilitando la coordinación de tareas dependientes.