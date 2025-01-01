## Comparten

- Son muy utlizadas en el contexto de bidata.
- Permiten almacenatr una gran cantidad de datos

## Data Lake

### Capa de landing ( capa zona de aterrizaje )
- Se alamacenan los datos en un formato de texto plano.
- Se tienen los conectores y origenes de datos externos para almacenarlos en su formato crudo
- Una vez tengamos los datos lso vamos a somenter a transfotmaciones para pasar la siguente capa

### Capa universal
- Se alamacenan en un formato paquet
- Se aplican todas las transformaciones encesarias.
    - limpieza.
    - modelación.
    - binarización.

### Capa solution
- se alamacena en dormato paquet
- Cuando los datos están listos para usarse se pasan a esta capa

## Delta Lake

### Capa bronze
- Se alamacenan los datos en un formato de texto plano.
- Se tienen los conectores y origenes de datos externos para almacenarlos en su formato crudo

### Capa silver
- Se almacenan los datos en un formato delta
- Se aplican todas las transformaciones encesarias.
    - limpieza.
    - modelación.
    - binarización.

### Capa gold
- Se almacenan los datos en un formato delta
- Cuando los datos están listos para usarse en un contexto de negocio se pasan a esta capa


# Delta Lake: Solución de Almacenamiento de Datos

Delta Lake es una solución de almacenamiento de datos basada en un sistema de archivos distribuido diseñada para mejorar la calidad, la confiabilidad y el rendimiento de los datos en entornos de big data.

## Características de Delta Lake

### Transacciones ACID
Delta Lake proporciona soporte nativo para transacciones ACID (atomicidad, consistencia, aislamiento y durabilidad), lo que garantiza un rendimiento fluido de lectura y escritura, y consistente incluso en entornos distribuidos.

### Control de versiones
Admite un historial de versiones completo de los datos almacenados, lo que le permite analizar los cambios a lo largo del tiempo y volver a versiones anteriores si es necesario.

### Operaciones de fusión y actualización
Facilita las operaciones de fusión y actualización de datos, lo que simplifica el procesamiento y la edición de datos.

### Optimizaciones de lectura y escritura
Contiene optimizaciones que aceleran las operaciones de lectura y escritura, como la indexación y la gestión de estadísticas que mejoran el rendimiento en comparación con el uso del sistema de archivos directamente sin estas optimizaciones.

### Compatibilidad con Apache Spark
Delta Lake es totalmente compatible con Apache Spark, lo que facilita la integración en el ecosistema Spark y aprovecha las capacidades de procesamiento distribuido.

### Evolución del esquema
Facilita la evolución del esquema de datos a lo largo del tiempo, permitiendo cambios en la estructura de datos sin afectar la compatibilidad con versiones anteriores.

### Gestión de metadatos
Delta Lake almacena metadatos internos que proporcionan información sobre los datos, facilitando la gestión y el control de los datos.

## Beneficios del Delta Lake

### Integridad y coherencia de los datos
La gestión de transacciones ACID garantiza la integridad y la coherencia de los datos, lo cual es fundamental en entornos donde la precisión de los datos es esencial.

### Mejor rendimiento
Las optimizaciones internas, como la indexación y la gestión de estadísticas, mejoran el rendimiento de las operaciones de lectura y escritura y permiten un acceso más eficiente a los datos.

### Historial de versiones para revisión
El historial de versiones le permite monitorear y analizar los cambios de datos a lo largo del tiempo y proporciona una descripción detallada de la evolución de los conjuntos de datos.

### Flexibilidad en el desarrollo de esquemas
La capacidad de evolucionar sin problemas el esquema de datos facilita una adaptación perfecta a los cambios comerciales.

### Operaciones simplificadas
Delta Lake simplifica operaciones como la fusión y la actualización, lo que facilita el trabajo con datos.

### Compatibilidad con herramientas de big data
Al admitir Apache Spark, Delta Lake se puede utilizar fácilmente con otras herramientas de big data, ampliando su aplicabilidad en entornos distribuidos.

---

## Conclusión
Estas características y beneficios hacen que Delta Lake sea una solución poderosa para el almacenamiento y la gestión de datos en entornos de big data, proporcionando un conjunto de funcionalidades avanzadas para abordar desafíos comunes en la administración de grandes volúmenes de datos.


