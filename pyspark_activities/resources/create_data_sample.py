from faker import Faker
import random
import pandas as pd

# Configuración de Faker y PySpark
faker = Faker()

# Función para generar datos de clientes
def generar_datos_clientes(n):
    clientes = []
    for i in range(1, n + 1):
        cliente = (
            i,  # cliente_id
            faker.name(),  # nombre
            faker.email(),  # correo
            faker.date_between(start_date="-5y", end_date="today"),  # fecha_registro
            faker.city()  # ciudad
        )
        clientes.append(cliente)
    return clientes

# Función para generar datos de órdenes
def generar_datos_ordenes(n, clientes):
    ordenes = []
    for i in range(1, n + 1):
        orden = (
            i,  # orden_id
            random.choice(clientes)[0],  # cliente_id (clave foránea)
            round(random.uniform(10.0, 1000.0), 2),  # monto
            faker.date_between(start_date="-3y", end_date="today"),  # fecha_orden
            random.choice(["Completada", "Pendiente", "Cancelada"])  # estado
        )
        ordenes.append(orden)
    return ordenes

# Generar datos
n_clientes = 100000  # Número de clientes
n_ordenes = 500000000  # Número de órdenes

clientes = generar_datos_clientes(n_clientes)
ordenes = generar_datos_ordenes(n_ordenes, clientes)

clientes_df = pd.DataFrame(clientes)
ordernes_df = pd.DataFrame(ordenes)

clientes_df.to_csv('./pyspark_activities/resources/clientes.csv')
ordernes_df.to_csv('./pyspark_activities/resources/ordenes.csv')

