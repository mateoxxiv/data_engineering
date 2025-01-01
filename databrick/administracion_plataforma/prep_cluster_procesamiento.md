## Creación del cluster
1. En el menu lateral ezquierdo seleccionar compute
2. Crear cluster (crear computo)

## Preparación del cluster de almacenamiento
Databricks os brinda una capa de almacenamiento (Databricks file system), que nos permite:
- Crear cuadernos y carpetas
- Subir datos

Todo en un espacio propio centralizado.

### Workspace
1. En el menu lateral ezquierdo seleccionar workspace

#### Carpetas
Son una herramienta que nos permite organizar nuestros recursos, con los que vamos a trabajar, dentro de nuestro
ecosistema de databricks.

#### Notebook

Un notebook en Databricks es un entorno interactivo basado en web que permite a los usuarios escribir, ejecutar y documentar código en múltiples lenguajes de programación como Python, Scala, SQL, R, y Markdown. Es una herramienta fundamental en Databricks para el desarrollo de proyectos de ciencia de datos, análisis de datos y tareas de ingeniería de datos.

#### Cargar archivos

Para poder interactuar con esta opción debemos habilitar Databricks File System:
1. Logo usuario
2. Settings
3. Advance
4. Habilitar DBFS File Browser
  

**Para cargar archivos:**  
  
1. Dirigirse a catalog
2. Seleccionar DBFS
3. Seleccionar upload
4. Especificar el directorio
5. Cargar los archivos  
  
Tambien pode,os crear tablas para importar nuestros datos.