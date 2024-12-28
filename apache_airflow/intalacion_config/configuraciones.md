## Todas las configuraciones
https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html

### acceder a las configuraciones
#### Listar contenedores
```bash
docker ps
```
#### ejecentrar al contenedor
```bash
docker exec -it id bash
```

### Podemos configurar

**Tipo de Ejecutor:**
Define si las tareas se ejecutan de una en una (pruebas locales) o de manera paralela/distribuida.
Ejemplo: SequentialExecutor, CeleryExecutor.

**Base de Datos:**
Configura dónde se almacenan los datos de Airflow (logs, DAGs, etc.). Puedes usar PostgreSQL o MySQL.

**Mensajería:**
Si usas un sistema distribuido, necesitas un "broker" como Redis para que las tareas se comuniquen entre sí.

**Interfaz Web:**
Ajusta cosas como cuántos usuarios pueden acceder al mismo tiempo, credenciales predeterminadas o si se muestra la configuración en la interfaz.

**DAGs y Logs:**
Define dónde se guardan los DAGs (código de los flujos de trabajo) y los logs (archivos de registro).

**Recursos:**
Controla el uso de memoria, número de trabajadores o procesos en el programador.

**Autenticación:**
Configura cómo los usuarios se conectan y verifican (por ejemplo, con contraseñas básicas o autenticación por token).

**Extensiones:**
Puedes agregar plugins o dependencias adicionales que Airflow necesite para trabajar con otras herramientas.
