## Arquitectura centralizada de datos
Un solo equipo es el encargado de procesar un conjunto de datos
- Se requiere mucho tiempo
- Tiene un nunico punto de falla
- No esta pensada apra crecer cuando queremos procesar mas datos

## Arquitectura descentralizada de datos
Varios equipos (nodos) son los encargado de procesar un conjunto de datos, dividiendolo en pequeños fragmentos:
- Las partes se llaman particiones
- Nodos (esclavos): procrsan las particiones
- Nodo master: orquesta todo el trabajo hacia los esclavos
- Cluster: Conjunto de master, esclavo
- La arquitectura se llama maestro-esclavo

### Beneficios
- Paralelismo (tiempo de procesamiento se reduce)
- Escalabilidad (podemos aumentar recursos horizontal y verticalmente)
- Tolerancia al fallo
- Mejor manejo de grandes volumenes de datos

## Almacenamiento y procesamiento
Tienen dos capas:
- Almacenamiento (disco)
- Procenamiento (cpu y ram)