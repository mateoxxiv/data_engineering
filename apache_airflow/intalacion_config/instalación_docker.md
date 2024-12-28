## Crear archivo docker compose

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.4/docker-compose.yaml'
```

## Ejecutar contenedor
```bash
docker compose up airflow-init
```

## Crear el contenedor
```bash
docker compose up -d
```