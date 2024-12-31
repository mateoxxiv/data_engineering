En Apache Airflow, los **templates Jinja** son una característica poderosa que permite **interpolación dinámica de valores** en tus **DAGs** y tareas, utilizando **plantillas Jinja** (un motor de plantillas ampliamente usado en Python).

### **¿Qué son los Templates Jinja en Airflow?**

Jinja es un motor de plantillas en Python que se usa para generar cadenas de texto dinámicamente. En Airflow, los **templates Jinja** se utilizan para generar dinámicamente **valores en parámetros de las tareas** a partir de otras variables, expresiones, o datos de contexto durante la ejecución del DAG.

Estos templates te permiten **personalizar el comportamiento** de los operadores y tareas basadas en datos que pueden variar de una ejecución a otra, como fechas, identificadores, o variables de entorno. Airflow usa Jinja para reemplazar las plantillas dentro de las tareas y los DAGs con valores evaluados en el momento de la ejecución.

### **¿Cómo se usan los Templates Jinja en Airflow?**

1. **Interpolación en los parámetros de las tareas**:
   Airflow permite usar Jinja en **casi todos los parámetros de los operadores**. Las plantillas Jinja se expresan con llaves dobles, por ejemplo, `{{ variable }}`. Airflow reemplazará estas expresiones con los valores correspondientes en tiempo de ejecución.

2. **Ejemplo de uso en un operador**:

   Si tienes una variable que cambia dependiendo de la fecha de ejecución, como la fecha actual o la fecha de inicio de un DAG, puedes usar Jinja para incluirla en los parámetros de tus tareas.

   ```python
   from airflow import DAG
   from airflow.operators.dummy_operator import DummyOperator
   from airflow.utils.dates import days_ago

   dag = DAG('jinja_template_example', start_date=days_ago(1))

   start_task = DummyOperator(
       task_id='start',
       dag=dag
   )

   # Usando una plantilla Jinja para generar un valor dinámico
   task_with_template = DummyOperator(
       task_id='task_with_template',
       dag=dag,
       start_date="{{ ds }}"  # 'ds' es una variable de contexto que representa la fecha de ejecución
   )

   start_task >> task_with_template
   ```

   En el ejemplo anterior, la plantilla `{{ ds }}` es reemplazada por la fecha de ejecución del DAG cuando se ejecuta el DAG. Airflow proporciona varias variables de contexto predeterminadas, como `ds`, `execution_date`, `dag_run.conf`, etc., que se pueden utilizar en las plantillas Jinja.

3. **Variables de contexto en Airflow**:
   Airflow ofrece una serie de **variables de contexto** que se pueden usar dentro de las plantillas. Algunas de las más comunes son:

   - `ds`: Fecha en formato `YYYY-MM-DD` de ejecución del DAG.
   - `execution_date`: Fecha y hora exactas cuando se ejecuta el DAG.
   - `task_instance`: Instancia de la tarea en ejecución.
   - `dag`: El DAG que está ejecutando la tarea.
   - `params`: Parámetros adicionales definidos en el DAG.
   - `macros`: Funciones adicionales disponibles para las plantillas.

### **Ejemplo Avanzado: Uso de `params` y Jinja en un BashOperator**

Supongamos que quieres ejecutar un comando bash y pasarle un parámetro dinámico usando Jinja. Puedes usar `params` en el DAG para definir valores que luego se interpolarán en las tareas:

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    'jinja_bash_operator_example',
    start_date=datetime(2024, 1, 1),
    params={'my_param': 'dynamic_value'}
)

bash_task = BashOperator(
    task_id='bash_task',
    bash_command="echo 'El valor de mi parámetro es {{ params.my_param }}'",
    dag=dag
)
```

En este caso, el comando `echo` imprimirá:  
**`El valor de mi parámetro es dynamic_value`**, ya que Jinja reemplaza `{{ params.my_param }}` por el valor definido en el parámetro `params` del DAG.

### **Conclusión**

Los **templates Jinja** en Airflow permiten una gran flexibilidad y dinamismo al definir tus DAGs y tareas. Son ideales para casos donde los valores deben variar dinámicamente entre ejecuciones, y ayudan a personalizar tareas sin tener que escribir múltiples versiones estáticas de ellas. Al usar Jinja, puedes referenciar datos de contexto, parámetros y macros, lo que hace que tu pipeline sea más reutilizable y adaptable a diferentes situaciones.